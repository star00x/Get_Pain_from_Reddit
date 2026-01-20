# Wide Research Execution Flow

Detailed 8-phase execution flow for multi-agent research orchestration.

## Phase 0: Reconnaissance (主代理执行，不委派)

**This phase MUST be executed by the main agent, NOT delegated to subagents.**

### Checklist

1. **Clarify user intent**: Research objective, expected output, evaluation criteria
2. **Identify core dimensions**: Topic clusters, stakeholders, regions, time periods
3. **Collect real samples**: At least ONE actual sample required (no pure speculation)
4. **Check MCP tools**: Trigger `search_router/` skill
   - If Tavily AND SerpApi unavailable → **STOP and report**, do not continue
5. **🚨 Reddit Detection Gate (MANDATORY)**:
   - Check if search results contain `reddit.com` URLs
   - If YES → **MUST trigger `reddit_research/` skill** before proceeding
   - This is a **BLOCKING REQUIREMENT**, not optional
   - See [Reddit Detection Gate](#reddit-detection-gate) below
6. **Route to other domain skills**:
   - Micro-SaaS evaluation → Mark for `microsaas_eval/` in Phase 6-7
7. **Generate reconnaissance report**: Dimensions, samples, gaps, estimated scope
8. **Report and continue**: Auto mode continues; Interactive mode waits for confirmation

### Reddit Detection Gate

**⚠️ CRITICAL: This gate MUST be checked before Phase 1.**

**🏆 Best Practice #1: 永远不要跳过此门控**

```
Detection logic:
  IF any of the following are true:
    - Search results contain reddit.com URLs
    - User mentions Reddit, subreddit, or r/
    - Research topic involves user feedback/complaints/pain points
  THEN:
    1. MUST trigger: Skill: skill = "reddit_research", args = "[topic]"
    2. MUST load reddit_research/EXTRACTION.md for comment extraction methods
    3. MUST include JSON API extraction in subagent prompts (Phase 3)

  IF gate is skipped:
    - Research quality will be DEGRADED (search snippets only, no comment analysis)
    - Report MUST include warning: "⚠️ 数据质量警告：未执行 Reddit 评论深度抓取"
```

**Why this matters**:
- SerpApi/Tavily only return search snippets, NOT full comment threads
- Reddit's real value is in the **comments**, not post titles
- Without `reddit_research`, citations may be incomplete or misleading

**🚨 NO-SKIP PRINCIPLE**:

| Situation | Agent thinking | Correct action |
|-----------|---------------|----------------|
| "User didn't mention Reddit" | "Maybe I can skip?" | **NO** — if URLs present, trigger |
| "Only 2 Reddit URLs in results" | "Probably not important?" | **NO** — any Reddit URL = trigger |
| "Research is about general topic" | "Reddit not primary source?" | **NO** — pain points almost always involve Reddit |
| "Unsure if Reddit is relevant" | "Should I ask user?" | **NO** — trigger anyway (false positive is cheap) |

**Violation consequences**:
1. Entire research output marked as **DEGRADED**
2. Final report MUST include quality warning
3. User trust in research accuracy is compromised

### 🔧 Reddit Tool Readiness Check (MANDATORY if Reddit Detection Gate passed)

**⚠️ CRITICAL: This check MUST be executed BEFORE any Reddit comment extraction.**

```
Pre-flight checklist:

□ COOKIE_FILE_CHECK:
  - Execute: ls -la cookie.txt
  - If EXISTS → Record path for --cookie-file parameter
  - If MISSING → STOP, create cookie.txt first (see EXTRACTION.md §Rate limiting)

□ COOKIE_FRESHNESS_CHECK:
  - Execute: find cookie.txt -mtime -7
  - If FRESH (< 7 days) → Proceed
  - If STALE (> 7 days) → WARN, cookie may need refresh

□ TOOL_VALIDATION:
  - Execute test extraction:
    python3 tools/reddit_thread_best_effort.py "https://www.reddit.com/r/test/comments/abc123/" \
      --cookie-file cookie.txt \
      --limit 10 --max-seconds 10
  - Check output: grep "stop_reason" output.json
  - If "completed" → Tool ready
  - If "blocked_requires_login_or_oauth" → Cookie invalid, STOP and refresh
  - If "rate_limited" → Wait and retry with increased delay
```

**Extraction Command Template (MANDATORY)**:

All Reddit extractions MUST use this template:

```bash
python3 tools/reddit_thread_best_effort.py "<URL>" \
  --cookie-file cookie.txt \
  --sort top --limit 500 --depth 10 \
  --max-morechildren-requests 120 --max-seconds 240 \
  --min-score 5 \
  --output-raw <output>.json \
  --output-analysis-md <output>.md
```

**Failure Recovery**:

| Error | Cause | Fix |
|-------|-------|-----|
| `blocked_requires_login_or_oauth` | Missing/expired cookie | Refresh cookie.txt from browser |
| `rate_limited` | Too many requests | Increase `--base-delay` to 2.0+ |
| `coverage_estimate < 0.8` | Partial extraction | Increase `--max-seconds` |

### 🏆 Best Practice #4: 阻塞失败需要人工介入

**CRITICAL**: When extraction encounters blocking errors, DO NOT attempt workarounds. STOP and request human intervention.

**Human intervention trigger conditions**:

| Condition | Severity | Agent action |
|-----------|----------|--------------|
| `blocked_requires_login_or_oauth` | 🔴 Critical | **STOP immediately**, request cookie refresh |
| `rate_limited` 3+ consecutive times | 🔴 Critical | **STOP**, suggest wait 10+ minutes |
| `coverage_estimate < 50%` on critical thread | 🟡 Warning | **ASK user**: proceed degraded or retry? |
| cookie.txt missing | 🔴 Critical | **STOP**, request cookie creation |
| cookie.txt stale (> 7 days) | 🟡 Warning | **WARN**, suggest refresh before proceeding |

**Human intervention request protocol**:

```markdown
⚠️ **Reddit 抓取被阻止，需要人工介入**

**错误类型**: [stop_reason from extraction output]
**受影响线程**: [thread URL]
**影响范围**: 无法获取该线程的完整评论数据

**所需操作** (选择一项):

**选项 A - 修复 Cookie (推荐)**:
1. 在浏览器中登录 Reddit
2. 打开 DevTools → Network → 复制完整 Cookie 头
3. 保存到项目根目录的 cookie.txt (单行)
4. 回复 "已修复" 继续研究

**选项 B - 降级继续**:
- 回复 "降级继续" 接受数据质量降低
- 报告将标注: ⚠️ 数据质量降级

**选项 C - 跳过此线程**:
- 回复 "跳过" 继续处理其他线程
- 此线程数据将不包含在分析中
```

**Why human intervention, not workarounds?**
1. Cookie issues require browser access (agent cannot obtain)
2. Rate limits require waiting (research timeline decision belongs to user)
3. Partial data quality tradeoff requires user consent
4. Attempting workarounds may waste time on futile retries

### Tool usage

```
Main agent executes directly (no Task tool):

1. Search for samples (priority order):
   # Preferred: SerpApi MCP (Google engine)
   serpapi.search:
     mode = "compact"
     params.engine = "google"
     params.q = "site:reddit.com [topic] pain points"
     params.num = 10

   # Preferred: Tavily MCP
   tavily_search:
     query = "[topic] complaints"
     max_results = 6
     search_depth = "advanced"

   # Fallback: Built-in tool (only if MCP unavailable)
   WebSearch: query = "site:reddit.com [topic] pain points 2025"

2. 🚨 Reddit Detection Gate (MANDATORY):
   # Check search results for reddit.com URLs
   IF results contain reddit.com:
     # MUST trigger reddit_research skill
     Skill: skill = "reddit_research", args = "[topic]"

     # MUST read extraction methods
     Read: file_path = ".claude/skills/reddit_research/EXTRACTION.md"

     # Record in reconnaissance report:
     "Reddit Detection Gate: PASSED - reddit_research skill loaded"
   ELSE:
     # Record in reconnaissance report:
     "Reddit Detection Gate: SKIPPED - no Reddit URLs detected"
```

## Phase 1: Initialize

Create run directory structure:

```bash
mkdir -p "runs/$(date +%Y-%m-%d)-<summary>-$(openssl rand -hex 3)"/{prompts,child_outputs,logs,raw,tmp}
```

Directory structure:
```
runs/<YYYY-MM-DD>-<summary>-<random>/
├── prompts/           # Subtask prompt files
├── child_outputs/     # Subagent outputs
├── logs/              # Execution logs
├── raw/               # MCP cached raw data
├── tmp/               # Intermediate files
├── aggregated_raw.md  # Concatenated raw outputs
└── polished_report.md # Final deliverable
```

## Phase 2: Decompose

Break research objective into parallelizable subtasks.

**Example decomposition**:

| ID | Subtask | Target source | Expected output |
|----|---------|---------------|-----------------|
| `task-001` | Invoice pains - SMB | r/smallbusiness, r/Accounting | Pain list + citations |
| `task-002` | Invoice pains - Freelancers | r/freelance | Pain list + citations |
| `task-003` | Invoice pains - Agencies | r/agencies, r/marketing | Pain list + citations |
| `task-004` | Competitive analysis | Public review sites | Weakness mapping |

## Phase 3: Generate prompts

Write detailed prompt for each subtask to `prompts/task-00X.md`.

Use templates from `templates/researcher.md` or `templates/synthesizer.md`.

**Prompt requirements**:
- Written in English (template), output in Chinese
- Include MCP tool constraints
- Include output format requirements per CONTRACT.md
- Include iteration limits (max 10 search rounds)

### 🚨 Phase 3 Validation Gate (MANDATORY)

**Before proceeding to Phase 4, MUST verify all prompts pass these checks:**

```
For EACH prompt file in prompts/task-00X.md:

□ TIME_FILTER_CHECK:
  - Grep for "after:\d{4}" in all search queries
  - If Reddit research: ALL queries must have time filter
  - FAIL if any query missing time filter

□ REDDIT_EXTRACTION_CHECK (if targets include Reddit):
  - Grep for "JSON API" OR "reddit_thread_best_effort" OR ".json"
  - MUST find at least one reference to JSON API extraction method
  - FAIL if only Tavily/SerpApi mentioned for comment extraction

□ DATA_QUALITY_WARNING_CHECK (if Reddit research):
  - Verify prompt includes fallback annotation requirement:
    "⚠️ 数据质量警告：未执行 Reddit 评论深度抓取"
```

**Validation execution**:

```bash
# Check time filter in all prompts
grep -r "after:[0-9]" prompts/ || echo "❌ FAIL: Missing time filter"

# Check JSON API extraction method
grep -rE "JSON API|reddit_thread_best_effort|\.json\?" prompts/ || echo "❌ FAIL: Missing JSON API extraction"
```

**If validation fails**:
1. DO NOT proceed to Phase 4
2. Edit prompt files to fix missing requirements
3. Re-run validation
4. Only proceed when all checks pass

## Phase 4: Parallel execution (Token-Optimized)

**CRITICAL: Send multiple Task calls in a SINGLE message.**

**⚠️ TOKEN OPTIMIZATION: Subagents write directly to files, return only status summaries.**

```
Task call 1:
  description: "Research SMB invoice pains"
  prompt: |
    [task-001 full prompt content]

    ⚠️ OUTPUT PROTOCOL:
    1. Write full output to: runs/[RUN_DIR]/child_outputs/task-001.md
    2. Return ONLY status summary (< 200 tokens):
       - Task ID, Status, Output file path, Key stats
  subagent_type: "general-purpose"
  model: "opus"
  run_in_background: true

Task call 2:
  description: "Research freelancer invoice pains"
  prompt: [task-002 with same OUTPUT PROTOCOL]
  subagent_type: "general-purpose"
  model: "opus"
  run_in_background: true

Task call 3:
  description: "Competitive analysis invoicing"
  prompt: [task-004 with same OUTPUT PROTOCOL]
  subagent_type: "general-purpose"
  model: "opus"
  run_in_background: true
```

Each Task returns an `agentId` for result collection.

### Collect and verify results

```
1. Collect JSON output:
   TaskOutput: task_id = "agent-id-1", block = true, timeout = 300000
   Returns: JSON object (see CONTRACT_SCHEMA.md)

2. Verify POST-conditions (mechanical check):
   - All required fields present?
   - All evidence fields >= 50 chars?
   - findings.length >= 3?
   - All checks.executed == true?

3. If verification fails:
   - retry_count < 2 → Retry with stronger prompt
   - retry_count >= 2 → Log failure, continue with partial data
```

**Main agent receives (JSON)**:
```json
{
  "task_id": "task-001",
  "status": "completed",
  "output_file": "runs/.../child_outputs/task-001.md",
  "checks_performed": {
    "relevance_check": {
      "executed": true,
      "evidence": "5篇文章中4篇直接讨论invoice追款问题...",
      "verdict": "pass"
    },
    "signal_quality_check": {
      "executed": true,
      "evidence": "来自r/smallbusiness的3个高赞帖(↑42,↑38,↑29)...",
      "verdict": "pass"
    }
  },
  "findings": [...],
  "summary": {
    "top_3_discoveries": [
      "追款/催款是最频繁提及的痛点，占投诉的40%+",
      "Wave用户普遍抱怨'免费但难用'",
      "自由职业者特别关注移动端和离线功能"
    ],
    "unexpected_insight": "多人提到希望AI自动分类发票",
    "suggested_direction": "深入调研'AI分类'需求的具体场景"
  }
}
```

**Verification pseudocode**:
```python
def verify_researcher_output(output: dict) -> tuple[bool, list[str]]:
    errors = []

    # Required fields
    for field in ["task_id", "status", "output_file", "checks_performed", "findings"]:
        if field not in output:
            errors.append(f"Missing: {field}")

    # Evidence length
    for check_name, check in output.get("checks_performed", {}).items():
        if len(check.get("evidence", "")) < 50:
            errors.append(f"Evidence too short: {check_name}")
        if not check.get("executed"):
            errors.append(f"Check not executed: {check_name}")

    # Minimum findings
    if len(output.get("findings", [])) < 3:
        errors.append("Insufficient findings (need >= 3)")

    return (len(errors) == 0, errors)
```

## Phase 5: Aggregate (Delegated to Subagent)

**⚠️ TOKEN OPTIMIZATION: Main agent does NOT read child outputs. Aggregation is delegated.**

```
Task call:
  description: "Aggregate, validate, and quality-check outputs"
  prompt: |
    # Aggregator Task

    ## Input
    - Run directory: runs/[RUN_DIR]
    - Child outputs: runs/[RUN_DIR]/child_outputs/task-*.md
    - Research objective: "[OBJECTIVE]"

    ## Tasks
    1. Read all child output files
    2. Validate format (sections, citations, placeholders, language)
    3. Validate content quality (relevance, substance, signal quality)
    4. Identify cross-task conflicts and coverage gaps
    5. Synthesize top 3 collective findings
    6. Concatenate to runs/[RUN_DIR]/aggregated_raw.md

    ⚠️ OUTPUT PROTOCOL:
    Return layered summary (< 500 tokens):
    - Layer 1: Status (subtasks, validated, file path, citations, failures)
    - Layer 2: Quality assessment (consistency, gaps, top findings, insights, recommended actions)
  subagent_type: "general-purpose"
  model: "opus"    # Requires judgment for content quality assessment
  run_in_background: false  # Wait for completion before Phase 6
```

**Main agent receives (JSON)**:
```json
{
  "task_id": "aggregator",
  "status": "completed",
  "output_file": "runs/.../aggregated_raw.md",
  "checks_performed": {
    "format_validation": {
      "executed": true,
      "evidence": "4个子任务中3个通过格式验证，task-003缺少Evidence部分",
      "verdict": "partial",
      "details": {"total": 4, "passed": 3, "failed": 1}
    },
    "content_quality": {
      "executed": true,
      "evidence": "task-001和task-002提供了具体用户原话和高赞数据，task-004的竞品分析较为全面",
      "verdict": "pass"
    },
    "cross_task_consistency": {
      "executed": true,
      "evidence": "task-001和task-002都将追款列为#1痛点，仅在次要痛点排序上有差异，无重大矛盾",
      "verdict": "pass"
    }
  },
  "quality_assessment": {
    "overall_quality": "high",
    "collective_findings": [
      "追款是跨所有细分市场的最高频痛点",
      "现有工具被认为'够用但不好用'",
      "自由职业者更关注移动端体验"
    ],
    "unexpected_insights": "AI自动分类作为新兴需求出现",
    "recommended_action": "proceed"
  },
  "stats": {"total_subtasks": 4, "validated": 3, "failed": 1, "total_citations": 18}
}
```

**Verification**: Same pattern as researcher (see CONTRACT_SCHEMA.md)

## Phase 6-7: Digest + Polish (Combined, Delegated)

**⚠️ TOKEN OPTIMIZATION: Main agent does NOT read aggregated_raw.md. Synthesis is delegated.**

**If Micro-SaaS research**: Include `microsaas_eval/` framework in synthesizer prompt.

```
Task call:
  description: "Digest and polish research report"
  prompt: |
    # Synthesizer Task

    ## Input
    Read: runs/[RUN_DIR]/aggregated_raw.md

    ## Steps
    1. Digest: Identify coverage, duplicates, gaps, top signals
    2. Outline: Design client-ready report structure
    3. Polish: Write each section with proper formatting
    4. Write output: runs/[RUN_DIR]/polished_report.md

    ## Micro-SaaS Framework (if applicable)
    Apply five-dimension scoring: Demand, Focus, Tech, API, SEO

    ⚠️ CONTRACT: Return JSON with checks_performed and evidence (see CONTRACT_SCHEMA.md)
  subagent_type: "general-purpose"
  model: "opus"    # Requires semantic understanding
  run_in_background: false  # Wait for completion before Phase 8
```

**Main agent receives (JSON)**:
```json
{
  "task_id": "synthesizer",
  "status": "completed",
  "output_file": "runs/.../polished_report.md",
  "checks_performed": {
    "completeness_check": {
      "executed": true,
      "evidence": "报告涵盖了aggregated_raw中的全部5个核心痛点和3个竞品，每个痛点有2-3个用户原话支撑",
      "verdict": "pass"
    },
    "coherence_check": {
      "executed": true,
      "evidence": "报告从问题→现状→机会→建议逻辑递进，各部分无矛盾",
      "verdict": "pass"
    },
    "actionability_check": {
      "executed": true,
      "evidence": "建议具体到'验证QuickBooks用户迁移意愿'而非泛泛而谈",
      "verdict": "pass"
    }
  },
  "executive_summary": {
    "key_findings": [
      "追款是最大痛点，占79%的投诉",
      "自由职业者更关注易用性，小企业更关注集成",
      "Wave被频繁提及为'够用但不好用'的选择"
    ],
    "opportunities_identified": 3,
    "recommended_next_steps": ["验证QuickBooks用户迁移意愿", "深入AI分类需求调研"]
  },
  "report_structure": {
    "sections": ["执行摘要", "核心痛点(5)", "竞品分析", "机会评估", "后续建议"],
    "word_count": 2500,
    "citation_count": 15
  }
}
```

**Verification**: Same pattern as researcher (see CONTRACT_SCHEMA.md)

## Phase 8: Deliver

1. Ensure report meets client-ready standards
2. Summarize main findings and actionable recommendations
3. Provide report file path
4. Mention follow-up items only if necessary

**Delivery format**:
```
研究完成。报告已保存至：runs/2024-12-28-invoice-research-abc123/polished_report.md

**主要发现**：
1. 追款是最大痛点，79% 的投诉涉及此问题
2. 自由职业者更关注易用性，小企业更关注集成
3. Wave 被频繁提及为"够用但不好用"的选择

**后续建议**：
- 验证 QuickBooks 用户的迁移意愿
- 深入分析定价敏感度
```

## Error handling

### Subagent failure

```
1. Check result:
   result = TaskOutput: task_id = "agent-id", block = true

2. If failed:
   if result.status == "failed":
     # Log failure
     Write:
       file_path = "runs/.../logs/task-001-error.log"
       content = "Failed at [timestamp]\n[error details]"

     # Decide retry:
     # - Transient error: retry
     # - Prompt issue: adjust and retry
     # - System limitation: log and skip
```

### Timeout strategy

| Subtask complexity | Initial timeout | Max timeout |
|--------------------|-----------------|-------------|
| Light | 3 min | 5 min |
| Medium | 5 min | 10 min |
| Heavy | 10 min | 15 min |

Max timeout reached = prompt/workflow needs debugging.

## Checklist

### Pre-execution

- [ ] Execution mode confirmed (Auto or Interactive)
- [ ] Phase 0 reconnaissance completed with ≥1 real sample
- [ ] MCP tools available (Tavily or SerpApi)
- [ ] **🚨 Reddit Detection Gate passed** (if Reddit URLs in results → `reddit_research` skill triggered)
- [ ] **🔧 Reddit Tool Readiness Check passed** (if Reddit research):
  - [ ] cookie.txt exists and path recorded
  - [ ] Cookie freshness verified (< 7 days)
  - [ ] Test extraction completed with `stop_reason: completed`
  - [ ] `--cookie-file` parameter included in all extraction commands
- [ ] Subtasks decomposed with unique IDs
- [ ] Prompts written to files (auditable)
- [ ] **Prompts include JSON API extraction instructions** (if Reddit research)
- [ ] **🚨 Phase 3 Validation Gate passed** (all prompts verified):
  - [ ] Time filter check: ALL search queries have `after:YYYY` filter
  - [ ] Reddit extraction check: Prompts include JSON API method references
  - [ ] Data quality warning: Fallback annotation requirement included
- [ ] All subagent tasks use `opus` model
- [ ] Parallel execution uses single-message multi-Task calls
- [ ] All network access via MCP tools (no curl/wget)
- [ ] **⚠️ TOKEN OPTIMIZATION: All prompts include OUTPUT PROTOCOL section**

### Post-execution

- [ ] All subagent outputs saved to child_outputs/
- [ ] All outputs validated per CONTRACT.md
- [ ] aggregated_raw.md created (audit copy)
- [ ] polished_report.md created by synthesizer subagent
- [ ] Citations use inline Markdown link format
- [ ] Deliverable language is Simplified Chinese (or user-specified)
- [ ] Final deliverable is file path, not chat paste
- [ ] **⚠️ TOKEN OPTIMIZATION: Main agent context contains only status summaries**

### Token optimization verification

- [ ] Phase 4: Researcher subagents returned < 350 tokens each (Layer 1 + Layer 2)
- [ ] Phase 5: Aggregator subagent returned < 500 tokens (Status + Quality Assessment)
- [ ] Phase 6-7: Synthesizer subagent returned < 500 tokens
- [ ] Main agent never called Read on child_outputs/* or aggregated_raw.md
- [ ] Total main agent context growth: < 3000 tokens for entire workflow
- [ ] Main agent has enough context to make strategic decisions (key findings, quality assessment)
