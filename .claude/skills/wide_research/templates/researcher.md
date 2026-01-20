# Researcher Subagent Template

Template for information-gathering subtasks. Instantiate by replacing `[placeholders]`.

---

## Template

```markdown
# Subtask: [task-id] [Task Title]

## Objective

[Clear description of research objective]

## ⚠️ CONTRACT: Verifiable Execution

> **Your output will be mechanically verified. Task FAILS if any condition is not met.**

### PRE-CONDITIONS (verify before starting)
- [ ] Research objective is clear
- [ ] Target sources are specified
- [ ] MCP tools are available

### REQUIRED CHECKS (with evidence)

You MUST perform these checks and record **specific evidence** (not just "pass"):

| Check | What to verify | Evidence requirement |
|-------|---------------|---------------------|
| `relevance_check` | Do findings address the research objective? | Min 50 chars, cite specific findings |
| `signal_quality_check` | Are pain signals genuine (not echo chamber)? | Min 50 chars, explain why signals are real |
| `source_credibility_check` | Are sources trustworthy? | Min 50 chars, note community size/engagement |

### POST-CONDITIONS (mechanically verified)

Your JSON output will be validated. **Task FAILS if**:
- Any required field is missing
- Any `evidence` field is < 50 characters
- `findings` array has < 3 items
- Any finding is missing `source_url`
- Any `check.executed` != true

### OUTPUT PROTOCOL

1. **Write full research to file**:
   ```
   Write: file_path = "[RUN_DIR]/child_outputs/[task-id].md"
   ```

2. **Return JSON (strict schema)**:

```json
{
  "task_id": "[task-id]",
  "status": "completed | partial | failed",
  "output_file": "[RUN_DIR]/child_outputs/[task-id].md",
  "checks_performed": {
    "relevance_check": {
      "executed": true,
      "evidence": "[具体证据：哪些发现与目标相关，为什么，至少50字]",
      "verdict": "pass | fail | partial"
    },
    "signal_quality_check": {
      "executed": true,
      "evidence": "[具体证据：为什么这些是真实痛点而非噪音，至少50字]",
      "verdict": "pass | fail | partial"
    },
    "source_credibility_check": {
      "executed": true,
      "evidence": "[具体证据：来源的可信度依据，至少50字]",
      "verdict": "pass | fail | partial"
    }
  },
  "findings": [
    {
      "content": "[发现内容]",
      "source_url": "[来源URL - 必填]",
      "signal_type": "pain-expression | switching | feature-gap | ...",
      "confidence": "high | medium | low"
    }
  ],
  "summary": {
    "top_3_discoveries": [
      "[最重要发现 - 一句话]",
      "[第二发现]",
      "[第三发现]"
    ],
    "unexpected_insight": "[意外发现，或 'none']",
    "suggested_direction": "[建议的后续方向，或 'none']"
  },
  "stats": {
    "pain_points_found": 5,
    "citations_collected": 12,
    "data_quality": "full | search-snippets-only"
  }
}
```

**Evidence Examples**:

❌ Bad: `"evidence": "内容相关"` (too short, no specifics)

✅ Good: `"evidence": "5篇文章中4篇直接讨论invoice追款问题，包括r/smallbusiness的3个高赞帖(↑42,↑38,↑29)，用户明确表达付费意愿"`

## Constraints

- Use MCP tools only (prefer Tavily: `tavily_search` / `tavily_extract`; if unavailable, use SerpApi MCP)
- No native network commands (wget/curl)
- Search/extract iteration limit: max 10 rounds
- Return immediately upon completion, do not wait for human approval
- **Time filter**: All search queries MUST include `after:YYYY-MM-DD` (180 days ago from today)

## 🚨 Reddit Research Requirements (MANDATORY if target sources include Reddit)

> **If ANY target source is a subreddit (r/...), this section is MANDATORY.**

### Comment Extraction Method

**DO NOT use Tavily for Reddit comment extraction.** Tavily only returns search snippets, not full comment threads.

**MUST use JSON API extraction**:

1. For each high-value thread (10+ comments), convert URL to JSON endpoint:
   ```
   https://www.reddit.com/r/{sub}/comments/{post_id}.json?sort=top&limit=500&depth=10
   ```

2. If `tools/reddit_thread_best_effort.py` is available, use it:
   ```bash
   python3 tools/reddit_thread_best_effort.py "<url>" \
     --sort top --limit 500 --depth 10 \
     --max-morechildren-requests 120 --max-seconds 240 \
     --min-score 5 \
     --output-raw raw.json --output-analysis-md analysis.md
   ```

3. If Python script unavailable, fetch JSON via Tavily Extract with `.json` URL suffix.

### Time Filter Requirement

All Reddit search queries MUST include time filter:
- Calculate: `today - 180 days = YYYY-MM-DD`
- Append to every query: `after:YYYY-MM-DD`

### Data Quality Annotation

If JSON API extraction is not executed, output MUST include:
```
⚠️ 数据质量警告：未执行 Reddit 评论深度抓取，引用可能来自搜索摘要而非原始评论
```

## Language Requirements

- All outputs must be in **Simplified Chinese** unless user specifies otherwise
- This prompt template is in English; the deliverable must be in Chinese

## Target Sources

[List specific sources: subreddits, sites, communities]

- [Source 1] (primary)
- [Source 2] (secondary)
- [Source 3] (supplementary)

## Search Patterns

High-intent queries first:
1. [Query 1]
2. [Query 2]
3. [Query 3]

## Critical Filters

- Echo chamber trap: Avoid [list builder communities to avoid]
- Free solution test: Check if top-voted comments provide perfect free solution

## Output Format (Must follow Child Output Contract)

### Scope & Inputs
- Research scope: [description]
- Input parameters: [sources, patterns, etc.]

### Key Findings
#### Pain Points Discovered
1. **Pain Point Title**
   - Frequency: [daily/weekly/occasional]
   - Intensity: [high/medium/low]
   - Representative comment: > "..."

#### Free Solution Check
- [x] Checked top-voted comments
- Free solutions found: [list or "none"]
- Conclusion: [PASS / CONDITIONAL / FAIL]

### Evidence (with citations)
- [Source 1](https://...)
- [Source 2](https://...)
- (At least 2 citations required)

### Gaps & Next Steps
- Data gaps: [areas not covered]
- Suggested follow-ups: [optional deeper directions]

### Errors & Follow-ups
(Only fill when errors occur)
- Error description: [if any]
- Retry suggestion: [if any]
```

---

## Instantiation example

**Subtask**: Research invoice pain points for small businesses

```markdown
# Subtask: task-001 Invoice Pain Points - Small Business

## Objective

Analyze real pain points of small business owners regarding invoice management on Reddit.

## Constraints

- Use MCP tools only (prefer Tavily for search; JSON API for Reddit comments)
- No native network commands (wget/curl)
- Search/extract iteration limit: max 10 rounds
- Return immediately upon completion
- **Time filter**: All queries must include `after:2025-07-08` (adjust to 180 days from execution date)

## 🚨 Reddit Research Requirements

**This task targets Reddit subreddits → JSON API extraction is MANDATORY.**

### High-Value Threads to Extract via JSON API

1. `https://www.reddit.com/r/smallbusiness/comments/abc123/...` → append `.json`
2. `https://www.reddit.com/r/Accounting/comments/def456/...` → append `.json`

### Extraction Command (if Python available)

```bash
python3 tools/reddit_thread_best_effort.py "<url>" \
  --sort top --limit 500 --min-score 5 \
  --output-analysis-md analysis.md
```

### If JSON API not executed

Must annotate output with:
```
⚠️ 数据质量警告：未执行 Reddit 评论深度抓取
```

## Language Requirements

- All outputs must be in **Simplified Chinese**

## Target Sources

- r/smallbusiness (primary)
- r/Accounting (secondary)
- r/Bookkeeping (supplementary)

## Search Patterns

High-intent queries first (ALL include time filter):
1. site:reddit.com/r/smallbusiness "invoice" ("hate" OR "frustrating") after:2025-07-08
2. site:reddit.com/r/smallbusiness "billing" "every time" tedious after:2025-07-08
3. site:reddit.com/r/smallbusiness "switched from" invoicing after:2025-07-08

## Critical Filters

- Echo chamber trap: Avoid r/SaaS, r/Entrepreneur, r/startups
- Free solution test: Check if top comments recommend Wave, Google Sheets, etc.

## Output Format

[As specified in Child Output Contract]
```

---

## Model selection

**All researcher subtasks → `opus`**

Research tasks inherently require judgment:
- Understanding search intent
- Evaluating source credibility
- Classifying pain signals
- Distinguishing genuine complaints from noise

Even "data fetching" in research context requires deciding **what to fetch** and **what's relevant**.
