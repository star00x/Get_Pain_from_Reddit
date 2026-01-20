# Comment Extraction Technical Reference

Deep technical reference for Reddit comment extraction via JSON API, including best-effort expansion of `more` placeholders without OAuth.

## Contents

- [JSON structure navigation](#json-structure-navigation)
- [Comment object fields](#comment-object-fields)
- [Handling more placeholders](#handling-more-placeholders)
- [Signal patterns](#signal-patterns)
- [High-value filtering](#high-value-filtering)
- [Rate limiting and workarounds](#rate-limiting-and-workarounds)
- [Practical examples](#practical-examples)
- [Quick reference](#quick-reference)

---

## JSON structure navigation

### Response structure

Reddit returns an array with two Listing objects:

```json
[
  {
    "kind": "Listing",
    "data": {
      "children": [
        {
          "kind": "t3",
          "data": { /* POST DATA */ }
        }
      ]
    }
  },
  {
    "kind": "Listing",
    "data": {
      "children": [
        { "kind": "t1", "data": { /* COMMENT 1 */ } },
        { "kind": "t1", "data": { /* COMMENT 2 */ } },
        { "kind": "more", "data": { /* UNEXPANDED CHILDREN */ } }
      ]
    }
  }
]
```

### Navigation paths

| Data | JSON Path |
|------|-----------|
| Post title | `[0].data.children[0].data.title` |
| Post body | `[0].data.children[0].data.selftext` |
| Post score | `[0].data.children[0].data.score` |
| Post author | `[0].data.children[0].data.author` |
| Post comment count | `[0].data.children[0].data.num_comments` |
| Comments array | `[1].data.children` |
| Comment body | `[1].data.children[i].data.body` |
| Comment score | `[1].data.children[i].data.score` |
| Nested replies | `[1].data.children[i].data.replies.data.children` |

### URL construction

```
https://www.reddit.com/r/{subreddit}/comments/{post_id}.json?sort=top&limit=500&depth=10&raw_json=1
```

| Parameter | Function | Recommended |
|-----------|----------|-------------|
| `sort` | Comment ordering | `top` |
| `limit` | Best-effort cap | `500` |
| `depth` | Nesting depth | `10` |
| `raw_json` | Disable HTML escaping | `1` |

---

## Comment object fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Comment ID (without `t1_` prefix) |
| `name` | string | Fullname (`t1_{id}`) |
| `parent_id` | string | Parent fullname (`t1_` for reply, `t3_` for top-level) |
| `link_id` | string | Post fullname (`t3_{post_id}`) |
| `body` | string | Comment text (Markdown) |
| `body_html` | string | Comment text (HTML) |
| `score` | number | Net upvotes (upvotes - downvotes) |
| `author` | string | Username |
| `created_utc` | number | Unix timestamp |
| `permalink` | string | Relative URL path to comment |
| `depth` | number | Nesting level (0 = top-level) |
| `is_submitter` | boolean | True if comment by OP |
| `distinguished` | string/null | `"moderator"` or `"admin"` if special |
| `stickied` | boolean | Pinned by moderator |
| `controversiality` | number | 1 = controversial, 0 = normal |

### Special cases

**Deleted comments**:
```json
{ "body": "[deleted]", "author": "[deleted]" }
```

**Removed comments**:
```json
{ "body": "[removed]", "author": "[deleted]" }
```

**Empty replies**: `replies` may be an empty string `""` instead of an object.

---

## Handling more placeholders

### What are more nodes?

When a thread has many comments, Reddit truncates the response and includes `kind: "more"` placeholder nodes:

```json
{
  "kind": "more",
  "data": {
    "count": 42,
    "name": "t1__",
    "id": "_",
    "parent_id": "t1_abc123",
    "depth": 2,
    "children": ["def456", "ghi789", "jkl012", ...]
  }
}
```

### Expansion via /api/morechildren

To retrieve these comments, call `/api/morechildren` with batched IDs:

```
GET https://www.reddit.com/api/morechildren.json?api_type=json&link_id=t3_{post_id}&children=id1,id2,id3&raw_json=1&sort=top
```

| Parameter | Value |
|-----------|-------|
| `api_type` | `json` |
| `link_id` | Post fullname (`t3_{post_id}`) |
| `children` | Comma-separated comment IDs (max 100 per request) |
| `raw_json` | `1` |
| `sort` | Same as initial fetch |

### Response structure

```json
{
  "json": {
    "errors": [],
    "data": {
      "things": [
        { "kind": "t1", "data": { /* COMMENT */ } },
        { "kind": "more", "data": { /* NESTED MORE */ } }
      ]
    }
  }
}
```

### Best-effort extraction strategy

The `tools/reddit_thread_best_effort.py` extractor implements:

1. **Initial fetch**: Get main listing with `?sort=top&limit=500&depth=10`
2. **Queue pending IDs**: Collect all IDs from `more` nodes
3. **Batch expansion**: Call `/api/morechildren` with up to 100 IDs per request
4. **Recursive collection**: New `more` nodes in responses add to queue
5. **Budget limits**: Stop after max requests or max time
6. **Delay and jitter**: 1.3s base + 0.7s random between requests

### Stop reasons

| Reason | Meaning |
|--------|---------|
| `completed` | Queue exhausted, all accessible comments extracted |
| `max_seconds` | Time budget (default 240s) reached |
| `max_requests` | Request budget (default 120) reached |
| `blocked` | HTTP 403/451 from Reddit |
| `blocked_requires_login_or_oauth` | Initial fetch blocked |
| `rate_limited` | Too many 429 responses |

---

## Signal patterns

The extractor uses regex patterns to score comments for analysis relevance. These patterns are defined in `tools/reddit_thread_best_effort.py`.

### Free solution indicators (DISQUALIFY if found in top comments)

```regex
\bjust use\b
\buse (google sheets|excel)\b
\bopen[- ]source\b
\bfree tier\b
\bis free\b
\bfree\b
\bgoogle sheets\b
```

### Workflow description indicators (HIGH VALUE)

```regex
\bexport\b
\bimport\b
\bmanual(ly)?\b
\bcopy\b
\bpaste\b
\bspreadsheet\b
\bexcel\b
\bgoogle sheets\b
\bzapier\b
\bmake\.com\b
\bairtable\b
\bworkflow\b
\bprocess\b
\bpipeline\b
\bintegrat(e|ion)\b
```

### Quantified cost indicators (VERY HIGH VALUE)

```regex
\$\s?\d[\d,]*(\.\d+)?          # Dollar amounts: $500, $1,200.00
\b\d+\s*(hours?|hrs?)\b        # Time: 4 hours, 10 hrs
\b\d+\s*(days?)\b              # Days: 3 days
\b\d+\s*(weeks?)\b             # Weeks: 2 weeks
\b\d+\s*(months?)\b            # Months: 6 months
\b\d+\s*(clients?|users?|customers?)\b  # Scale: 200 clients
\b\d+%\b                       # Percentages: 50%
```

### Willingness to pay indicators

```regex
\bwould pay\b
\bhappy to pay\b
\bpay for\b
```

### Frustration indicators

```regex
\bhate\b
\bfrustrat(e|ed|ing)\b
\bannoy(ed|ing)?\b
\btedious\b
\bwaste\b
\bpain\b
```

### Signal scoring formula

The extractor computes a composite score:

```
signal_score = 1.2 × log(score + 1)
             + 5.0 × quantified_matches
             + 3.0 × workflow_matches
             + 4.0 × wtp_matches
             + 2.5 × free_solution_matches
             + 1.0 × frustration_matches
```

Comments are selected by combining:
- Top 60 by Reddit score
- Top 60 by signal score
- Top 30 containing free solution patterns
- Parent comments for context (up to 2 hops)

---

## High-value filtering

### Score-based thresholds

| Threshold | Use Case |
|-----------|----------|
| `score >= 10` | High community consensus |
| `score >= 5` | Solid signal (default) |
| `score >= 3` | B2B/niche communities |
| `score >= 1` | All non-downvoted |

### Filtering decision matrix

| Score | Free solution? | Pain signal? | Action |
|-------|---------------|--------------|--------|
| ≥10 | Yes | - | ❌ DISQUALIFY opportunity |
| ≥10 | No | Yes | ✅ HIGH PRIORITY |
| ≥5 | No | Yes | ✅ INCLUDE |
| ≥5 | No | No | ⚠️ REVIEW |
| <5 | - | - | Skip unless OP reply |

### Free solution test process

1. Find complaint threads about target pain point
2. Extract top comments via JSON extraction
3. Check if any high-scored comment provides free, complete solution
4. Check if replies confirm "Thanks, this solved it!"

**If perfect free solution exists and is well-known → DISQUALIFY**

---

## Rate limiting and workarounds

### Reddit rate limits

| Type | Approximate Limit |
|------|-------------------|
| Unauthenticated | ~60 requests/minute |
| With User-Agent | More lenient |
| With session cookie | Higher limits |

### Common HTTP errors

| Code | Meaning | Action |
|------|---------|--------|
| 429 | Rate limited | Exponential backoff (2s → 4s → 8s...) |
| 403 | Blocked | Use session cookie via `REDDIT_COOKIE_FILE` |
| 451 | Unavailable for legal reasons | Usually requires authentication |
| 405 | Method not allowed | Try POST instead of GET |

### Using session cookies

When blocked, provide a logged-in browser session cookie:

1. Log in to Reddit in your browser
2. Open DevTools → Network → copy the `Cookie:` header value
3. Save to a text file (single line)
4. Set `REDDIT_COOKIE_FILE=/path/to/cookie.txt`

The extractor will include this cookie in all requests.

### 🏆 Cookie Maintenance (Best Practice #3)

**Why this matters**: Reddit session cookies typically expire after ~7 days. Stale cookies trigger `blocked_requires_login_or_oauth`, halting extraction entirely.

#### Pre-flight checklist

Run these checks before **every** extraction session:

| Check | Command | Pass condition |
|-------|---------|----------------|
| File exists | `test -f cookie.txt && echo OK` | Returns `OK` |
| Not empty | `test -s cookie.txt && echo OK` | Returns `OK` |
| Freshness | `find cookie.txt -mtime -7 \| grep -q . && echo OK` | Returns `OK` (modified < 7 days ago) |

#### Refresh procedure

1. Open browser where you're **logged in** to Reddit
2. Open DevTools (F12 or Cmd+Opt+I)
3. Go to Network tab
4. Navigate to any reddit.com page
5. Click any request → Headers → Request Headers
6. Copy the entire `Cookie:` value (starts with `csv=2;...` or similar)
7. Save to project root as `cookie.txt` (single line, no newlines)
8. Verify: `head -c 50 cookie.txt` should show cookie data

#### Validity test

Before running full extraction, test with a small request:

```bash
REDDIT_COOKIE_FILE=cookie.txt python3 tools/reddit_thread_best_effort.py \
  "https://www.reddit.com/r/test/comments/1abc123/" \
  --max-seconds 10 --max-morechildren-requests 2 \
  --output-raw /dev/null
```

| `stop_reason` | Interpretation | Action |
|---------------|----------------|--------|
| `completed` or `max_seconds` | ✅ Cookie valid | Proceed with full extraction |
| `blocked_requires_login_or_oauth` | ❌ Cookie invalid/expired | Refresh cookie (step 1-8 above) |
| `rate_limited` | ⚠️ Too many requests | Wait 10+ minutes, then retry |

#### Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Immediate 403 | Cookie expired | Refresh from browser |
| Works then fails | Session invalidated | Log out/in on browser, refresh cookie |
| Inconsistent failures | Multiple Reddit accounts | Ensure single account, clear other sessions |
| `REDDIT_COOKIE_FILE` not found | Path issue | Use absolute path or verify relative path from CWD |

### Completeness guarantees

Even with `/api/morechildren`, completeness is NOT guaranteed:
- Some comment IDs may return empty (deleted/removed/moderator-only)
- Rate limiting may prevent full expansion
- Time/request budgets may be exhausted

**Always check `coverage_estimate` and `stop_reason` in output metrics.**

---

## Practical examples

### Example 1: Basic extraction

**Input URL**:
```
https://www.reddit.com/r/accounting/comments/abc123/why_is_quickbooks_so_expensive_now/
```

**Command**:
```bash
python3 tools/reddit_thread_best_effort.py \
  "https://www.reddit.com/r/accounting/comments/abc123/" \
  --sort top \
  --limit 500 \
  --depth 10 \
  --max-morechildren-requests 120 \
  --max-seconds 240 \
  --min-score 5 \
  --output-raw out.json \
  --output-analysis-md out.md
```

**Output files**:
- `out.json`: Full extraction with all comments + metrics
- `out.md`: Curated subset for LLM analysis

### Example 2: High-value comment found

```json
{
  "body": "Every month I export from QuickBooks to Excel, then manually match against our CRM export. Takes about 4 hours for 200 clients. Been doing this for 3 years and hate every minute of it.",
  "score": 23,
  "author": "frustrated_accountant"
}
```

**Extracted signals**:
- ✅ Quantified time: "4 hours for 200 clients"
- ✅ Recurring pain: "Every month", "3 years"
- ✅ Emotional signal: "hate every minute"
- ✅ Workflow description: "export → manually match → CRM"

**Verdict**: HIGH PRIORITY opportunity.

### Example 3: Free solution disqualification

**Top comments**:
```json
[
  { "body": "Ubersuggest has a free tier that covers basic keyword research", "score": 47 },
  { "body": "Just use Google Search Console + Screaming Frog free version", "score": 35 },
  { "body": "SE Ranking is way cheaper and has most features", "score": 28 }
]
```

**Analysis**:
- Comments 1-2 recommend free/open tools with high scores
- Opportunity is **CONDITIONAL** at best — requires "all-in-one convenience" positioning

---

## Quick reference

### Endpoint template

```
https://www.reddit.com/r/{subreddit}/comments/{post_id}.json?sort=top&limit=500&depth=10&raw_json=1
```

### Key JSON paths

```
Post data:       [0].data.children[0].data
Comments array:  [1].data.children
Comment body:    [1].data.children[i].data.body
Comment score:   [1].data.children[i].data.score
Nested replies:  [1].data.children[i].data.replies.data.children
More nodes:      [1].data.children[i].kind == "more"
```

### Extractor command

```bash
python3 tools/reddit_thread_best_effort.py "<url>" \
  --sort top --limit 500 --depth 10 \
  --max-morechildren-requests 120 --max-seconds 240 \
  --min-score 5 \
  --output-raw raw.json --output-analysis-md analysis.md
```

### Runner command

```bash
./comment_extraction_run.sh -i urls.txt [-o output_dir] [-m 5] [-s top] [-l 500]
```

### Default filters

```
score >= 5 (general)
score >= 3 (B2B/niche)
```

### Critical output metrics

| Metric | Interpretation |
|--------|----------------|
| `coverage_estimate` | Ratio of extracted to expected comments |
| `stop_reason` | Why extraction stopped |
| `remaining_pending_child_ids` | IDs not yet expanded |
| `missing_children_ids` | IDs that returned empty |
