#!/usr/bin/env python3
"""
Best-effort Reddit thread extractor without OAuth.

Strategy:
- Fetch canonical post JSON listing via reddit.com/.../comments/<id>.json
- Recursively collect comments and "more" placeholders
- Expand "more" via /api/morechildren (best-effort, unauthenticated)
- Emit:
  1) raw JSON (all extracted comments + metrics)
  2) analysis input Markdown (small, high-signal subset for LLM analysis)
"""

from __future__ import annotations

import argparse
import datetime as dt
import gzip
import json
import math
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import deque
from typing import Any, Deque, Dict, Iterable, List, Optional, Sequence, Set, Tuple


DEFAULT_SORT = "top"
DEFAULT_LIMIT = 500
DEFAULT_DEPTH = 10

DEFAULT_MAX_MORECHILDREN_REQUESTS = 120
DEFAULT_MAX_SECONDS = 240

DEFAULT_BASE_DELAY_SECONDS = 1.3
DEFAULT_JITTER_SECONDS = 0.7

MAX_CHILDREN_PER_MORECHILDREN = 100


RE_POST_PATH = re.compile(r"/r/([^/]+)/comments/([^/]+)")
BLOCK_MARKERS = [
    "You've been blocked by network security.",
    "To continue, log in to your Reddit account or use your developer token",
]

FREE_SOLUTION_PATTERNS = [
    r"\bjust use\b",
    r"\buse (google sheets|excel)\b",
    r"\bopen[- ]source\b",
    r"\bfree tier\b",
    r"\bis free\b",
    r"\bfree\b",
    r"\bgoogle sheets\b",
]

WORKFLOW_PATTERNS = [
    r"\bexport\b",
    r"\bimport\b",
    r"\bmanual(ly)?\b",
    r"\bcopy\b",
    r"\bpaste\b",
    r"\bspreadsheet\b",
    r"\bexcel\b",
    r"\bgoogle sheets\b",
    r"\bzapier\b",
    r"\bmake\.com\b",
    r"\bairtable\b",
    r"\bworkflow\b",
    r"\bprocess\b",
    r"\bpipeline\b",
    r"\bintegrat(e|ion)\b",
]

QUANTIFIED_PATTERNS = [
    r"\$\s?\d[\d,]*(\.\d+)?",
    r"\b\d+\s*(hours?|hrs?)\b",
    r"\b\d+\s*(days?)\b",
    r"\b\d+\s*(weeks?)\b",
    r"\b\d+\s*(months?)\b",
    r"\b\d+\s*(clients?|users?|customers?)\b",
    r"\b\d+%\b",
]

WTP_PATTERNS = [
    r"\bwould pay\b",
    r"\bhappy to pay\b",
    r"\bpay for\b",
]

FRUSTRATION_PATTERNS = [
    r"\bhate\b",
    r"\bfrustrat(e|ed|ing)\b",
    r"\bannoy(ed|ing)?\b",
    r"\btedious\b",
    r"\bwaste\b",
    r"\bpain\b",
]


def utc_now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def build_user_agent(app: str) -> str:
    rand = random.randint(1000, 9999)
    return f"{app}/1.0 (no-oauth; best-effort; rand={rand})"


def clean_child_id(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    if "_" in value:
        return value.split("_", 1)[1]
    return value


def safe_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return default


def safe_float(value: Any) -> Optional[float]:
    try:
        return float(value)
    except Exception:
        return None


def normalize_post_url(input_url: str, timeout_seconds: float, headers: Dict[str, str]) -> Tuple[str, str, str]:
    url = (input_url or "").strip()
    if not url:
        raise ValueError("empty url")

    parsed = urllib.parse.urlparse(url)
    if not parsed.scheme:
        url = "https://" + url
        parsed = urllib.parse.urlparse(url)

    resolved_url = url
    if parsed.netloc.endswith("redd.it") or "/comments/" not in parsed.path:
        request = urllib.request.Request(url, headers=headers, method="GET")
        with urllib.request.urlopen(request, timeout=timeout_seconds) as resp:
            resolved_url = resp.geturl()

    match = RE_POST_PATH.search(urllib.parse.urlparse(resolved_url).path)
    if not match:
        raise ValueError(f"unsupported reddit url path: {resolved_url}")

    subreddit = match.group(1)
    post_id = match.group(2)
    canonical_post_url = f"https://www.reddit.com/r/{subreddit}/comments/{post_id}/"
    return canonical_post_url, subreddit, post_id


def build_listing_json_url(post_url: str, sort: str, limit: int, depth: int) -> str:
    parsed = urllib.parse.urlparse(post_url)
    match = RE_POST_PATH.search(parsed.path)
    if not match:
        raise ValueError(f"unsupported reddit url path: {post_url}")
    subreddit = match.group(1)
    post_id = match.group(2)

    base = f"https://www.reddit.com/r/{subreddit}/comments/{post_id}.json"
    params = {
        "raw_json": "1",
        "sort": sort,
        "limit": str(limit),
        "depth": str(depth),
    }
    return base + "?" + urllib.parse.urlencode(params)


def read_response_bytes(resp: urllib.response.addinfourl) -> bytes:
    raw = resp.read()
    encoding = (resp.headers.get("Content-Encoding") or "").lower()
    if "gzip" in encoding:
        return gzip.decompress(raw)
    return raw


def http_fetch_json(
    url: str,
    headers: Dict[str, str],
    timeout_seconds: float,
    method: str = "GET",
    data: Optional[bytes] = None,
) -> Tuple[Any, str]:
    request = urllib.request.Request(url, headers=headers, method=method, data=data)
    with urllib.request.urlopen(request, timeout=timeout_seconds) as resp:
        final_url = resp.geturl()
        body = read_response_bytes(resp)
    try:
        return json.loads(body.decode("utf-8")), final_url
    except Exception as e:
        preview = body[:400].decode("utf-8", errors="replace")
        raise ValueError(f"json parse failed: {e}; body preview: {preview}") from e


def read_http_error_body(e: urllib.error.HTTPError, max_bytes: int = 250_000) -> str:
    try:
        body = e.read(max_bytes) or b""
    except Exception:
        return ""
    return body.decode("utf-8", errors="replace")


def detect_blocked(body_text: str) -> bool:
    if not body_text:
        return False
    for marker in BLOCK_MARKERS:
        if marker.lower() in body_text.lower():
            return True
    return False


def load_cookie_from_args(args: argparse.Namespace) -> str:
    cookie = (getattr(args, "cookie", "") or "").strip()
    if cookie:
        return cookie.split(":", 1)[1].strip() if cookie.lower().startswith("cookie:") else cookie

    env_cookie = (os.environ.get("REDDIT_COOKIE") or "").strip()
    if env_cookie:
        return env_cookie.split(":", 1)[1].strip() if env_cookie.lower().startswith("cookie:") else env_cookie

    cookie_file = (getattr(args, "cookie_file", "") or "").strip() or (os.environ.get("REDDIT_COOKIE_FILE") or "").strip()
    if not cookie_file:
        return ""
    try:
        raw = open(cookie_file, "r", encoding="utf-8").read().strip()
        return raw.split(":", 1)[1].strip() if raw.lower().startswith("cookie:") else raw
    except Exception:
        return ""


def extract_post(payload: Any) -> Dict[str, Any]:
    post: Dict[str, Any] = {}
    if not isinstance(payload, list) or len(payload) < 1:
        return post

    listing = payload[0]
    if not isinstance(listing, dict):
        return post
    data = listing.get("data") or {}
    children = data.get("children") or []
    if not children or not isinstance(children, list):
        return post
    first = children[0]
    if not isinstance(first, dict):
        return post
    if first.get("kind") != "t3":
        return post
    d = first.get("data") or {}
    post_id = d.get("id")
    fullname = d.get("name") or (f"t3_{post_id}" if post_id else None)
    post = {
        "id": post_id,
        "fullname": fullname,
        "subreddit": d.get("subreddit"),
        "title": d.get("title"),
        "selftext": d.get("selftext"),
        "author": d.get("author"),
        "created_utc": d.get("created_utc"),
        "permalink": d.get("permalink"),
        "url": d.get("url"),
        "num_comments": d.get("num_comments"),
        "score": d.get("score"),
        "upvote_ratio": d.get("upvote_ratio"),
        "is_self": d.get("is_self"),
        "locked": d.get("locked"),
        "over_18": d.get("over_18"),
    }
    return post


def add_pending_children(
    pending_queue: Deque[str],
    pending_set: Set[str],
    extracted_ids: Set[str],
    children: Sequence[Any],
) -> int:
    added = 0
    for raw_id in children:
        if not isinstance(raw_id, str):
            continue
        cid = clean_child_id(raw_id)
        if not cid:
            continue
        if cid in extracted_ids:
            continue
        if cid in pending_set:
            continue
        pending_set.add(cid)
        pending_queue.append(cid)
        added += 1
    return added


def collect_from_nodes(
    nodes: Iterable[Any],
    comments_by_fullname: Dict[str, Dict[str, Any]],
    extracted_ids: Set[str],
    pending_queue: Deque[str],
    pending_set: Set[str],
) -> Dict[str, int]:
    stack: List[Any] = []
    for n in nodes:
        stack.append((n, 0))

    seen_more_nodes = 0
    added_comments = 0
    added_pending_ids = 0

    while stack:
        node, depth = stack.pop()
        if not isinstance(node, dict):
            continue
        kind = node.get("kind")
        data = node.get("data") or {}

        if kind == "t1":
            comment_id = data.get("id")
            fullname = data.get("name") or (f"t1_{comment_id}" if comment_id else None)
            if fullname and fullname not in comments_by_fullname:
                extracted_ids.add(comment_id) if isinstance(comment_id, str) else None
                comments_by_fullname[fullname] = {
                    "id": comment_id,
                    "fullname": fullname,
                    "parent_fullname": data.get("parent_id"),
                    "link_fullname": data.get("link_id"),
                    "author": data.get("author"),
                    "body": data.get("body"),
                    "score": data.get("score"),
                    "created_utc": data.get("created_utc"),
                    "permalink": data.get("permalink"),
                    "depth": None,
                    "is_submitter": data.get("is_submitter"),
                    "distinguished": data.get("distinguished"),
                    "stickied": data.get("stickied"),
                }
                added_comments += 1

            replies = data.get("replies")
            if isinstance(replies, dict):
                rd = replies.get("data") or {}
                children = rd.get("children") or []
                if isinstance(children, list):
                    for child in children:
                        stack.append((child, depth + 1))

        elif kind == "more":
            seen_more_nodes += 1
            children = data.get("children") or []
            if isinstance(children, list):
                added_pending_ids += add_pending_children(
                    pending_queue=pending_queue,
                    pending_set=pending_set,
                    extracted_ids=extracted_ids,
                    children=children,
                )

    return {
        "seen_more_nodes": seen_more_nodes,
        "added_comments": added_comments,
        "added_pending_ids": added_pending_ids,
    }


def compute_comment_depths(
    comments_by_fullname: Dict[str, Dict[str, Any]],
    link_fullname: Optional[str],
) -> None:
    depth_cache: Dict[str, Optional[int]] = {}
    visiting: Set[str] = set()

    def depth_of(fullname: str) -> Optional[int]:
        if fullname in depth_cache:
            return depth_cache[fullname]
        if fullname in visiting:
            depth_cache[fullname] = None
            return None
        visiting.add(fullname)
        c = comments_by_fullname.get(fullname)
        parent = (c or {}).get("parent_fullname")
        depth: Optional[int]
        if not parent:
            depth = None
        elif parent == link_fullname or (isinstance(parent, str) and parent.startswith("t3_")):
            depth = 0
        elif isinstance(parent, str) and parent.startswith("t1_") and parent in comments_by_fullname:
            pd = depth_of(parent)
            depth = None if pd is None else pd + 1
        else:
            depth = None
        visiting.remove(fullname)
        depth_cache[fullname] = depth
        return depth

    for fullname in list(comments_by_fullname.keys()):
        comments_by_fullname[fullname]["depth"] = depth_of(fullname)


def match_count(patterns: Sequence[str], text: str) -> int:
    if not text:
        return 0
    total = 0
    for p in patterns:
        if re.search(p, text, flags=re.IGNORECASE):
            total += 1
    return total


def signal_score(comment: Dict[str, Any]) -> float:
    body = (comment.get("body") or "") if isinstance(comment.get("body"), str) else ""
    score = safe_int(comment.get("score"), 0)
    score_part = math.log(max(score, 0) + 1.0)
    free = match_count(FREE_SOLUTION_PATTERNS, body)
    workflow = match_count(WORKFLOW_PATTERNS, body)
    quantified = match_count(QUANTIFIED_PATTERNS, body)
    wtp = match_count(WTP_PATTERNS, body)
    frustration = match_count(FRUSTRATION_PATTERNS, body)
    return (
        1.2 * score_part
        + 5.0 * quantified
        + 3.0 * workflow
        + 4.0 * wtp
        + 2.5 * free
        + 1.0 * frustration
    )


def select_comments_for_analysis(
    comments: List[Dict[str, Any]],
    comments_by_fullname: Dict[str, Dict[str, Any]],
    min_score: int,
    max_selected: int,
    max_parent_hops: int,
) -> List[Dict[str, Any]]:
    scored = []
    for c in comments:
        s = safe_int(c.get("score"), 0)
        if s < 0:
            continue
        scored.append((c, signal_score(c)))

    top_by_score = sorted(scored, key=lambda x: safe_int(x[0].get("score"), 0), reverse=True)[:60]
    top_by_signal = sorted(scored, key=lambda x: x[1], reverse=True)[:60]
    free_hits = [x for x in scored if match_count(FREE_SOLUTION_PATTERNS, x[0].get("body") or "") > 0]
    top_free = sorted(free_hits, key=lambda x: (x[1], safe_int(x[0].get("score"), 0)), reverse=True)[:30]

    selected_fullnames: Set[str] = set()
    selected: List[Dict[str, Any]] = []

    def add_comment(c: Dict[str, Any]) -> None:
        fullname = c.get("fullname")
        if not isinstance(fullname, str) or not fullname:
            return
        if fullname in selected_fullnames:
            return
        selected_fullnames.add(fullname)
        selected.append(c)

    for c, _ in top_by_score:
        if safe_int(c.get("score"), 0) >= min_score:
            add_comment(c)
    for c, _ in top_by_signal:
        if safe_int(c.get("score"), 0) >= min_score or signal_score(c) >= 6.0:
            add_comment(c)
    for c, _ in top_free:
        add_comment(c)

    if max_parent_hops > 0:
        to_expand = list(selected)
        for _ in range(max_parent_hops):
            new_parents: List[Dict[str, Any]] = []
            for c in to_expand:
                parent = c.get("parent_fullname")
                if isinstance(parent, str) and parent.startswith("t1_"):
                    pc = comments_by_fullname.get(parent)
                    if pc and pc.get("fullname") not in selected_fullnames:
                        new_parents.append(pc)
            for pc in new_parents:
                add_comment(pc)
            to_expand = new_parents

    def sort_key(c: Dict[str, Any]) -> Tuple[float, int]:
        return (signal_score(c), safe_int(c.get("score"), 0))

    selected_sorted = sorted(selected, key=sort_key, reverse=True)
    return selected_sorted[:max_selected]


def to_full_permalink(permalink: Any) -> Optional[str]:
    if not isinstance(permalink, str) or not permalink:
        return None
    if permalink.startswith("http://") or permalink.startswith("https://"):
        return permalink
    return "https://www.reddit.com" + permalink


def truncate_text(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 1)] + "…"


def write_json(path: str, payload: Any) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def write_analysis_md(
    path: str,
    *,
    post: Dict[str, Any],
    metrics: Dict[str, Any],
    json_url: str,
    selected_comments: List[Dict[str, Any]],
    min_score: int,
) -> None:
    title = post.get("title") or "[Unknown Title]"
    post_url = post.get("url") or post.get("permalink") or ""
    if isinstance(post_url, str) and post_url.startswith("/r/"):
        post_url = "https://www.reddit.com" + post_url

    lines: List[str] = []
    lines.append("# Reddit Comment Extraction (Best-effort, No OAuth)")
    lines.append("")
    lines.append(f"**Post Title:** {title}")
    lines.append(f"**Post URL:** {post_url}")
    lines.append(f"**JSON URL:** {json_url}")
    lines.append("")
    lines.append("## Coverage metrics")
    lines.append("")
    for k in [
        "expected_num_comments",
        "extracted_unique_comments",
        "remaining_pending_child_ids",
        "missing_children_ids",
        "coverage_estimate",
        "stop_reason",
        "requests_total",
        "requests_morechildren",
    ]:
        if k in metrics:
            lines.append(f"- **{k}:** {metrics[k]}")
    if metrics.get("warnings"):
        lines.append("- **warnings:**")
        for w in metrics["warnings"]:
            lines.append(f"  - {w}")
    if metrics.get("errors"):
        lines.append("- **errors:**")
        for e in metrics["errors"]:
            lines.append(f"  - {e}")
    lines.append("")
    lines.append("## Analysis instructions")
    lines.append("")
    lines.append(f"- Filter baseline: `score >= {min_score}` (unless signal is strong)")
    lines.append("- Keep parent context when a reply is selected")
    lines.append("- Run free solution check on top visible suggestions")
    lines.append("")
    lines.append(f"## Selected comments ({len(selected_comments)})")
    lines.append("")

    for c in selected_comments:
        author = c.get("author")
        author_str = f"u/{author}" if isinstance(author, str) and author else "u/[deleted]"
        score = safe_int(c.get("score"), 0)
        depth = c.get("depth")
        depth_str = str(depth) if isinstance(depth, int) else "?"
        link = to_full_permalink(c.get("permalink")) or ""
        fullname = c.get("fullname") or ""
        parent = c.get("parent_fullname") or ""
        body = c.get("body") if isinstance(c.get("body"), str) else ""
        body = truncate_text(body.replace("\r", ""), 1600)

        lines.append(f"### {fullname} (score={score}, depth={depth_str})")
        lines.append(f"- **Author:** {author_str}")
        lines.append(f"- **Parent:** {parent}")
        lines.append(f"- **Link:** {link}")
        lines.append("")
        if body:
            lines.append("> " + body.replace("\n", "\n> "))
        else:
            lines.append("> [no body]")
        lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def run(args: argparse.Namespace) -> int:
    user_agent = args.user_agent or build_user_agent("GetPainRedditExtractor")
    cookie = load_cookie_from_args(args)
    headers = {
        "User-Agent": user_agent,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "application/json,text/plain;q=0.9,*/*;q=0.8",
    }
    if cookie:
        headers["Cookie"] = cookie

    errors: List[str] = []
    warnings: List[str] = []

    post: Dict[str, Any] = {}
    comments_by_fullname: Dict[str, Dict[str, Any]] = {}
    extracted_ids: Set[str] = set()
    pending_queue: Deque[str] = deque()
    pending_set: Set[str] = set()
    missing_children_ids: Set[str] = set()

    seen_more_nodes_total = 0
    requests_morechildren = 0
    requests_total = 0

    canonical_post_url = ""
    json_url = ""
    resolved_post_url = ""

    stop_reason = "error"
    auth_mode = "cookie" if cookie else "none"
    initial_fetch_ok = False

    start = time.monotonic()
    try:
        resolved_post_url, subreddit, post_id = normalize_post_url(
            args.url,
            timeout_seconds=args.timeout,
            headers=headers,
        )
        canonical_post_url = resolved_post_url
        json_url = build_listing_json_url(
            canonical_post_url,
            sort=args.sort,
            limit=args.limit,
            depth=args.depth,
        )

        try:
            payload, final_json_url = http_fetch_json(
                json_url,
                headers=headers,
                timeout_seconds=args.timeout,
                method="GET",
            )
            requests_total += 1
            json_url = final_json_url
            initial_fetch_ok = True
        except urllib.error.HTTPError as e:
            body_text = read_http_error_body(e)
            if e.code in (403, 451) and detect_blocked(body_text):
                errors.append("blocked by reddit network security; use login cookie (REDDIT_COOKIE_FILE) or OAuth token")
                stop_reason = "blocked_requires_login_or_oauth"
            else:
                errors.append(f"initial fetch HTTP error: {e.code}")
                if body_text:
                    errors.append("initial fetch body preview: " + body_text[:400].replace("\n", " ").strip())
                stop_reason = "initial_http_error"
            payload = []
            final_json_url = json_url
        except Exception as e:
            errors.append(f"initial fetch error: {e}")
            stop_reason = "initial_error"
            payload = []
            final_json_url = json_url

        post = extract_post(payload)
        if not post:
            warnings.append("post data missing or unexpected; continuing best-effort")

        link_fullname = post.get("fullname") if isinstance(post.get("fullname"), str) else None

        if isinstance(payload, list) and len(payload) >= 2 and isinstance(payload[1], dict):
            listing = payload[1]
            data = listing.get("data") or {}
            children = data.get("children") or []
            if isinstance(children, list):
                cstats = collect_from_nodes(
                    nodes=children,
                    comments_by_fullname=comments_by_fullname,
                    extracted_ids=extracted_ids,
                    pending_queue=pending_queue,
                    pending_set=pending_set,
                )
                seen_more_nodes_total += cstats["seen_more_nodes"]
        else:
            warnings.append("comments listing missing; no initial comments collected")

        budget_hit = False
        backoff = 0.0
        while pending_queue:
            elapsed = time.monotonic() - start
            if elapsed >= args.max_seconds:
                stop_reason = "max_seconds"
                budget_hit = True
                break
            if requests_morechildren >= args.max_morechildren_requests:
                stop_reason = "max_requests"
                budget_hit = True
                break

            batch: List[str] = []
            while pending_queue and len(batch) < MAX_CHILDREN_PER_MORECHILDREN:
                cid = pending_queue.popleft()
                pending_set.discard(cid)
                if cid in extracted_ids:
                    continue
                batch.append(cid)
            if not batch:
                continue

            link_id = link_fullname or (f"t3_{post.get('id')}" if post.get("id") else None)
            if not isinstance(link_id, str) or not link_id:
                warnings.append("missing link_id; cannot call morechildren")
                stop_reason = "missing_link_id"
                budget_hit = True
                break

            params = {
                "api_type": "json",
                "link_id": link_id,
                "children": ",".join(batch),
                "raw_json": "1",
                "sort": args.sort,
            }
            endpoint = "https://www.reddit.com/api/morechildren.json"
            url = endpoint + "?" + urllib.parse.urlencode(params)

            try:
                more_payload, _ = http_fetch_json(
                    url,
                    headers=headers,
                    timeout_seconds=args.timeout,
                    method="GET",
                )
            except urllib.error.HTTPError as e:
                code = e.code
                if code == 405:
                    try:
                        data = urllib.parse.urlencode(params).encode("utf-8")
                        more_payload, _ = http_fetch_json(
                            endpoint,
                            headers={**headers, "Content-Type": "application/x-www-form-urlencoded"},
                            timeout_seconds=args.timeout,
                            method="POST",
                            data=data,
                        )
                    except Exception as e2:
                        errors.append(f"morechildren HTTP 405 then POST failed: {e2}")
                        stop_reason = "morechildren_failed"
                        pending_queue.extendleft(reversed(batch))
                        for cid in batch:
                            pending_set.add(cid)
                        break
                elif code in (403, 451):
                    errors.append(f"morechildren blocked: HTTP {code}")
                    stop_reason = "blocked"
                    pending_queue.extendleft(reversed(batch))
                    for cid in batch:
                        pending_set.add(cid)
                    break
                elif code == 429:
                    backoff = max(backoff, 2.0)
                    errors.append("rate limited (HTTP 429); backing off")
                    pending_queue.extendleft(reversed(batch))
                    for cid in batch:
                        pending_set.add(cid)
                    if backoff > 60.0:
                        stop_reason = "rate_limited"
                        break
                    time.sleep(backoff + random.random())
                    backoff = min(60.0, backoff * 2.0)
                    continue
                else:
                    errors.append(f"morechildren HTTP error: {code}")
                    stop_reason = "morechildren_failed"
                    pending_queue.extendleft(reversed(batch))
                    for cid in batch:
                        pending_set.add(cid)
                    break
            except Exception as e:
                errors.append(f"morechildren request failed: {e}")
                stop_reason = "morechildren_failed"
                pending_queue.extendleft(reversed(batch))
                for cid in batch:
                    pending_set.add(cid)
                break

            requests_morechildren += 1
            requests_total += 1
            backoff = 0.0

            returned_ids: Set[str] = set()
            mjson = more_payload.get("json") if isinstance(more_payload, dict) else None
            if isinstance(mjson, dict):
                merrors = mjson.get("errors") or []
                if merrors:
                    errors.append(f"morechildren errors: {merrors}")
                mdata = mjson.get("data") or {}
                things = mdata.get("things") or []
                if isinstance(things, list):
                    for t in things:
                        if isinstance(t, dict) and t.get("kind") == "t1":
                            td = t.get("data") or {}
                            tid = td.get("id")
                            if isinstance(tid, str) and tid:
                                returned_ids.add(tid)
                    cstats = collect_from_nodes(
                        nodes=things,
                        comments_by_fullname=comments_by_fullname,
                        extracted_ids=extracted_ids,
                        pending_queue=pending_queue,
                        pending_set=pending_set,
                    )
                    seen_more_nodes_total += cstats["seen_more_nodes"]

            for cid in batch:
                if cid not in returned_ids and cid not in extracted_ids:
                    missing_children_ids.add(cid)

            delay = args.base_delay + random.random() * args.jitter
            time.sleep(delay)

        if initial_fetch_ok and not budget_hit and stop_reason == "error":
            stop_reason = "completed"

        compute_comment_depths(comments_by_fullname, link_fullname=post.get("fullname"))

    except Exception as e:
        errors.append(f"initial error: {e}")
        stop_reason = "initial_error"

    comments: List[Dict[str, Any]] = list(comments_by_fullname.values())
    comments.sort(
        key=lambda c: (
            safe_int(c.get("created_utc"), 0),
            str(c.get("id") or ""),
        )
    )

    expected = safe_int(post.get("num_comments"), 0) if post else 0
    extracted_count = len(comments)
    coverage = None
    if expected > 0:
        coverage = round(extracted_count / float(expected), 4)

    metrics: Dict[str, Any] = {
        "expected_num_comments": expected if expected > 0 else None,
        "extracted_unique_comments": extracted_count,
        "remaining_pending_child_ids": len(pending_queue),
        "missing_children_ids": len(missing_children_ids),
        "coverage_estimate": coverage,
        "stop_reason": stop_reason,
        "auth_mode": auth_mode,
        "requests_total": requests_total,
        "requests_morechildren": requests_morechildren,
        "seen_more_nodes_total": seen_more_nodes_total,
        "pending_child_ids_sample": list(list(pending_queue)[:20]),
        "missing_child_ids_sample": list(sorted(list(missing_children_ids))[:20]),
        "warnings": warnings,
        "errors": errors,
    }

    output = {
        "version": "1.0",
        "extracted_at_utc": utc_now_iso(),
        "input_url": args.url,
        "canonical_post_url": canonical_post_url or None,
        "json_url": json_url or None,
        "extraction_method": "json+morechildren-session-cookie" if cookie else "json+morechildren-no-auth",
        "post": post,
        "comments": comments,
        "metrics": metrics,
    }

    if args.output_raw:
        write_json(args.output_raw, output)

    if args.output_analysis_md:
        selected = select_comments_for_analysis(
            comments=comments,
            comments_by_fullname=comments_by_fullname,
            min_score=args.min_score,
            max_selected=args.max_selected,
            max_parent_hops=args.max_parent_hops,
        )
        write_analysis_md(
            args.output_analysis_md,
            post=post,
            metrics=metrics,
            json_url=json_url or "",
            selected_comments=selected,
            min_score=args.min_score,
        )

    if stop_reason in (
        "blocked_requires_login_or_oauth",
        "initial_http_error",
        "initial_error",
        "missing_link_id",
    ):
        return 1
    return 0


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Best-effort Reddit thread extraction without OAuth app credentials (JSON + morechildren).",
    )
    parser.add_argument("url", help="Reddit post URL (supports redd.it short links)")
    parser.add_argument("--sort", default=DEFAULT_SORT, help=f"Sort (default: {DEFAULT_SORT})")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help=f"Initial JSON limit (default: {DEFAULT_LIMIT})")
    parser.add_argument("--depth", type=int, default=DEFAULT_DEPTH, help=f"Initial JSON depth (default: {DEFAULT_DEPTH})")
    parser.add_argument(
        "--max-morechildren-requests",
        type=int,
        default=DEFAULT_MAX_MORECHILDREN_REQUESTS,
        help=f"Max morechildren requests (default: {DEFAULT_MAX_MORECHILDREN_REQUESTS})",
    )
    parser.add_argument(
        "--max-seconds",
        type=int,
        default=DEFAULT_MAX_SECONDS,
        help=f"Max wall time seconds (default: {DEFAULT_MAX_SECONDS})",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=15.0,
        help="Per-request timeout seconds (default: 15)",
    )
    parser.add_argument(
        "--base-delay",
        type=float,
        default=DEFAULT_BASE_DELAY_SECONDS,
        help=f"Delay between morechildren requests (default: {DEFAULT_BASE_DELAY_SECONDS})",
    )
    parser.add_argument(
        "--jitter",
        type=float,
        default=DEFAULT_JITTER_SECONDS,
        help=f"Random jitter seconds (default: {DEFAULT_JITTER_SECONDS})",
    )
    parser.add_argument("--user-agent", default="", help="Custom User-Agent (recommended if you get blocked)")
    parser.add_argument(
        "--cookie",
        default="",
        help="Cookie header value (discouraged; prefer REDDIT_COOKIE_FILE)",
    )
    parser.add_argument(
        "--cookie-file",
        default="",
        help="Path to file containing Cookie header value (or set REDDIT_COOKIE_FILE)",
    )

    parser.add_argument("--output-raw", default="", help="Write raw extraction JSON to this path")
    parser.add_argument("--output-analysis-md", default="", help="Write analysis input Markdown to this path")

    parser.add_argument("--min-score", type=int, default=5, help="Baseline score threshold for analysis selection")
    parser.add_argument("--max-selected", type=int, default=120, help="Max selected comments for analysis input")
    parser.add_argument("--max-parent-hops", type=int, default=2, help="Include up to N parent hops for context")

    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    if args.limit < 1:
        print("Error: --limit must be >= 1", file=sys.stderr)
        return 2
    if args.depth < 1:
        print("Error: --depth must be >= 1", file=sys.stderr)
        return 2
    if args.max_morechildren_requests < 0:
        print("Error: --max-morechildren-requests must be >= 0", file=sys.stderr)
        return 2
    if args.max_seconds < 1:
        print("Error: --max-seconds must be >= 1", file=sys.stderr)
        return 2

    return run(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
