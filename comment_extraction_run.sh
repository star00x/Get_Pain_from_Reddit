#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf "%s\n" "Usage: comment_extraction_run.sh -i <input_file> [-o <output_dir>] [-m <min_score>] [-s <sort>] [-l <limit>]" >&2
  printf "%s\n" "Optional: set REDDIT_COOKIE_FILE to a file containing your logged-in browser Cookie header value." >&2
}

input_file=""
output_dir=""
min_score="5"
sort="top"
limit="500"

while getopts ":i:o:m:s:l:" opt; do
  case "$opt" in
    i) input_file="$OPTARG" ;;
    o) output_dir="$OPTARG" ;;
    m) min_score="$OPTARG" ;;
    s) sort="$OPTARG" ;;
    l) limit="$OPTARG" ;;
    *) usage; exit 1 ;;
  esac
done

if [[ -z "$input_file" ]]; then
  usage
  exit 1
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
root_dir="$script_dir"
if [[ "$input_file" != /* ]]; then
  input_file="$root_dir/$input_file"
fi

if [[ ! -f "$input_file" ]]; then
  printf "%s\n" "Input file not found: $input_file" >&2
  exit 1
fi

timestamp="$(date +"%Y%m%d-%H%M%S")"
if [[ -z "$output_dir" ]]; then
  output_dir="$root_dir/runs/comment-extraction-$timestamp"
elif [[ "$output_dir" != /* ]]; then
  output_dir="$root_dir/$output_dir"
fi

if ! command -v codex >/dev/null 2>&1; then
  printf "%s\n" "codex CLI not found in PATH" >&2
  exit 1
fi

if ! command -v rg >/dev/null 2>&1; then
  printf "%s\n" "rg not found in PATH" >&2
  exit 1
fi

python_bin=""
if command -v python3 >/dev/null 2>&1; then
  python_bin="python3"
elif command -v python >/dev/null 2>&1; then
  python_bin="python"
else
  printf "%s\n" "python3/python not found in PATH" >&2
  exit 1
fi

extractor="$root_dir/tools/reddit_thread_best_effort.py"
if [[ ! -f "$extractor" ]]; then
  printf "%s\n" "Extractor not found: $extractor" >&2
  exit 1
fi

timeout_bin=""
if command -v timeout >/dev/null 2>&1; then
  timeout_bin="timeout"
elif command -v gtimeout >/dev/null 2>&1; then
  timeout_bin="gtimeout"
fi

mkdir -p "$output_dir/prompts" "$output_dir/child_outputs" "$output_dir/logs" "$output_dir/raw" "$output_dir/analysis_inputs"
aggregated="$output_dir/aggregated_raw.md"
: > "$aggregated"

index=0
while IFS= read -r line || [[ -n "$line" ]]; do
  line="${line//$'\r'/}"
  if [[ -z "$line" ]]; then
    continue
  fi
  if [[ "$line" == \#* ]]; then
    continue
  fi

  base="$line"
  query=""
  if [[ "$line" == *\?* ]]; then
    base="${line%%\?*}"
    query="${line#*\?}"
  fi
  params="$query"
  if [[ -n "$params" ]]; then
    if [[ ! "$params" =~ (^|&)sort= ]]; then
      params="${params}&sort=$sort"
    fi
    if [[ ! "$params" =~ (^|&)limit= ]]; then
      params="${params}&limit=$limit"
    fi
  else
    params="sort=$sort&limit=$limit"
  fi
  line_sort="$sort"
  if [[ "$params" =~ (^|&)sort=([^&]+) ]]; then
    line_sort="${BASH_REMATCH[2]}"
  fi
  line_limit="$limit"
  if [[ "$params" =~ (^|&)limit=([^&]+) ]]; then
    line_limit="${BASH_REMATCH[2]}"
  fi

  index=$((index + 1))
  id="$(printf "%03d" "$index")"
  prompt_file="$output_dir/prompts/$id.md"
  output_file="$output_dir/child_outputs/$id.md"
  extract_log="$output_dir/logs/$id.extract.log"
  analysis_log="$output_dir/logs/$id.analysis.log"
  raw_file="$output_dir/raw/$id.json"
  analysis_input="$output_dir/analysis_inputs/$id.md"

  if ! "$python_bin" "$extractor" "$base" \
    --sort "$line_sort" \
    --limit "$line_limit" \
    --depth 10 \
    --max-morechildren-requests 120 \
    --max-seconds 240 \
    --min-score "$min_score" \
    --output-raw "$raw_file" \
    --output-analysis-md "$analysis_input" \
    >"$extract_log" 2>&1; then
    stop_reason="$("$python_bin" - "$raw_file" <<'PY'
import json, sys
try:
  with open(sys.argv[1], "r", encoding="utf-8") as f:
    data = json.load(f)
  m = data.get("metrics") or {}
  print(m.get("stop_reason") or "unknown")
except Exception:
  print("unknown")
PY
)"
    printf "%s\n" "### Comment Analysis: [Failed]" > "$output_file"
    printf "%s\n" "" >> "$output_file"
    printf "%s\n" "**Post URL**: $line" >> "$output_file"
    printf "%s\n" "**Returned comments**: 0" >> "$output_file"
    printf "%s\n" "**Analyzed**: 0" >> "$output_file"
    printf "%s\n" "**Coverage (est.)**: N/A (stop_reason=$stop_reason)" >> "$output_file"
    printf "%s\n" "" >> "$output_file"
    printf "%s\n" "#### Free solution check" >> "$output_file"
    printf "%s\n" "- [ ] No free solution found in top comments" >> "$output_file"
    printf "%s\n" "- [ ] Free solution found: extraction failed" >> "$output_file"
    printf "%s\n" "" >> "$output_file"
    printf "%s\n" "#### Key pain signals" >> "$output_file"
    printf "%s\n" "| Comment | Score | Signal | Link |" >> "$output_file"
    printf "%s\n" "|---------|-------|--------|------|" >> "$output_file"
    printf "%s\n" "| \"Extraction failed\" | 0 | Error | N/A |" >> "$output_file"
    printf "%s\n" "" >> "$output_file"
    printf "%s\n" "#### Workflow descriptions" >> "$output_file"
    continue
  fi

  tee "$prompt_file" >/dev/null <<EOF
You are analyzing extracted Reddit comments for product research.

Constraints:
- Do not fetch the web.
- Do not use Tavily or any MCP tools.
- Use ONLY the extracted data provided below.

Input URL:
$line

BEGIN EXTRACTED DATA
EOF

  rg "" "$analysis_input" >> "$prompt_file"

  tee -a "$prompt_file" >/dev/null <<EOF
END EXTRACTED DATA

Task:
- Use the extracted Post Title for the heading.
- Use the Input URL exactly in the Post URL field.
- Returned comments: use extracted_unique_comments from metrics.
- Analyzed: number of comments you actually used (from the Selected comments list or fewer).
- If stop_reason != completed OR remaining_pending_child_ids > 0 OR coverage_estimate is low, explicitly note coverage is partial.
- Filter baseline: score >= $min_score (unless signal is strong).

Output:
Return only the following Markdown block.

### Comment Analysis: [Post Title]

**Post URL**: [link]
**Returned comments**: [N extracted]
**Analyzed**: [N analyzed]
**Coverage (est.)**: [coverage_estimate + stop_reason]

#### Free solution check
- [ ] No free solution found in top comments
- [ ] Free solution found: [describe]

#### Key pain signals
| Comment | Score | Signal | Link |
|---------|-------|--------|------|
| "[quote]" | 42 | Quantified cost | [comment link] |

#### Workflow descriptions
> "[verbatim quote describing current process]"
> - u/username (score: X)
EOF

  if [[ -n "$timeout_bin" ]]; then
    if ! "$timeout_bin" 600 codex exec --sandbox workspace-write -c model_reasoning_effort="low" --output-last-message "$output_file" - < "$prompt_file" > "$analysis_log" 2>&1; then
      printf "%s\n" "### Comment Analysis: [Failed]" > "$output_file"
      printf "%s\n" "" >> "$output_file"
      printf "%s\n" "**Post URL**: $line" >> "$output_file"
      printf "%s\n" "**Returned comments**: 0" >> "$output_file"
      printf "%s\n" "**Analyzed**: 0" >> "$output_file"
      printf "%s\n" "**Coverage (est.)**: N/A (analysis failed)" >> "$output_file"
      printf "%s\n" "" >> "$output_file"
      printf "%s\n" "#### Free solution check" >> "$output_file"
      printf "%s\n" "- [ ] No free solution found in top comments" >> "$output_file"
      printf "%s\n" "- [ ] Free solution found: extraction failed" >> "$output_file"
      printf "%s\n" "" >> "$output_file"
      printf "%s\n" "#### Key pain signals" >> "$output_file"
      printf "%s\n" "| Comment | Score | Signal | Link |" >> "$output_file"
      printf "%s\n" "|---------|-------|--------|------|" >> "$output_file"
      printf "%s\n" "| \"Extraction failed\" | 0 | Error | N/A |" >> "$output_file"
      printf "%s\n" "" >> "$output_file"
      printf "%s\n" "#### Workflow descriptions" >> "$output_file"
    fi
  else
    if ! codex exec --sandbox workspace-write -c model_reasoning_effort="low" --output-last-message "$output_file" - < "$prompt_file" > "$analysis_log" 2>&1; then
      printf "%s\n" "### Comment Analysis: [Failed]" > "$output_file"
      printf "%s\n" "" >> "$output_file"
      printf "%s\n" "**Post URL**: $line" >> "$output_file"
      printf "%s\n" "**Returned comments**: 0" >> "$output_file"
      printf "%s\n" "**Analyzed**: 0" >> "$output_file"
      printf "%s\n" "**Coverage (est.)**: N/A (analysis failed)" >> "$output_file"
      printf "%s\n" "" >> "$output_file"
      printf "%s\n" "#### Free solution check" >> "$output_file"
      printf "%s\n" "- [ ] No free solution found in top comments" >> "$output_file"
      printf "%s\n" "- [ ] Free solution found: extraction failed" >> "$output_file"
      printf "%s\n" "" >> "$output_file"
      printf "%s\n" "#### Key pain signals" >> "$output_file"
      printf "%s\n" "| Comment | Score | Signal | Link |" >> "$output_file"
      printf "%s\n" "|---------|-------|--------|------|" >> "$output_file"
      printf "%s\n" "| \"Extraction failed\" | 0 | Error | N/A |" >> "$output_file"
      printf "%s\n" "" >> "$output_file"
      printf "%s\n" "#### Workflow descriptions" >> "$output_file"
    fi
  fi

  if [[ -s "$output_file" ]]; then
    if [[ -s "$aggregated" ]]; then
      printf "\n\n" >> "$aggregated"
    fi
    tee -a "$aggregated" < "$output_file" >/dev/null
  fi
done < "$input_file"

printf "%s\n" "Run directory: $output_dir"
