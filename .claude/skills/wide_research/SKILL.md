---
name: wide-research
description: Multi-agent research orchestration framework for deep market/topic analysis. Coordinates parallel subagents, synthesizes findings across sources, and produces structured deliverables. Use when user requests "Wide Research", "宽泛研究", or comprehensive multi-source analysis requiring parallel execution.
---

# Wide Research Orchestration

Multi-agent research framework that decomposes complex research objectives into parallel subtasks, coordinates execution via Claude Code's Task tool, and synthesizes results into polished deliverables.

## Triggers

- User mentions "Wide Research" or "宽泛研究"
- User requests comprehensive multi-source analysis
- User references this skill directory
- Research scope requires parallel subagent coordination

## Capabilities

- Parallel subagent coordination via Task tool
- Research synthesis across multiple sources/communities
- Structured deliverable generation with incremental editing
- Integration with domain-specific skills (reddit_research, microsaas_eval)

## Execution modes

| Mode | Trigger | Behavior |
|------|---------|----------|
| **Auto** (default) | No explicit request | Phase 0 完成后自动继续执行 |
| **Interactive** | User says "Interactive" or "等待确认" | 每阶段停止等待用户确认 |

## Dependencies

- `search_router/` — MCP tool availability check and routing (always required)
- `reddit_research/` — **🚨 MANDATORY when search results contain reddit.com URLs**
  - Provides: JSON API extraction, comment analysis, signal scoring
  - Without it: Only search snippets available, citations incomplete
  - See: FLOW.md "Reddit Detection Gate" for trigger conditions
- `microsaas_eval/` — Micro-SaaS opportunity evaluation (when applicable)

## Default configuration

- **Language**: Simplified Chinese (unless user specifies otherwise)
- **Deliverable format**: File path + summary (never paste full document in chat)
- **Editing mode**: Incremental (Edit tool, not Write)

## Load order

1. This file (always — ~150 tokens)
2. `FLOW.md` (when executing — ~2k tokens)
3. `CONTRACT.md` (when validating subagent outputs — ~1k tokens)
4. `CONTRACT_SCHEMA.md` (verification rules for all subagents — ~2k tokens)
5. `templates/*.md` (when spawning subagents)

## Quick reference

### Phase overview (Token-Optimized)

| Phase | Name | Actor | Model | Key action | Token budget |
|-------|------|-------|-------|------------|--------------|
| 0 | Reconnaissance | Main agent | - | Collect samples, check MCP, route to domain skills | ~500 |
| 1 | Initialize | Main agent | - | Create run directory structure | ~100 |
| 2 | Decompose | Main agent | - | Break objective into subtasks with unique IDs | ~300 |
| 3 | Generate prompts | Main agent | - | Write prompts to `prompts/task-00X.md` | ~500 |
| 4 | Execute | Subagents | opus | **Write to files, return layered summary** | ~350/task |
| 5 | Aggregate | Subagent | opus | **Quality-check, validate, return assessment** | ~500 |
| 6-7 | Digest+Polish | Subagent | opus | **Synthesize, polish, return executive summary** | ~500 |
| 8 | Deliver | Main agent | - | File path + summary from synthesizer | ~200 |

**Total main agent context: ~3000 tokens** (vs ~15000+ without optimization)

### Critical patterns

**Token-optimized execution** (correct):
```
Single message containing:
  Task #1: run_in_background=true, model="opus"
    prompt includes: "Write output to [file], return ONLY status summary"
  Task #2: run_in_background=true, model="opus"
    prompt includes: "Write output to [file], return ONLY status summary"
  Task #3: run_in_background=true, model="opus"
    prompt includes: "Write output to [file], return ONLY status summary"
```

**Model selection**:
- `opus`: **All subagent tasks** — research, aggregation, synthesis all require judgment
- `haiku`: Not used in Wide Research (no pure mechanical subtasks exist)

**Deliverable format**:
```
研究完成。报告已保存至：runs/YYYY-MM-DD-topic-abc123/polished_report.md

**主要发现**：
1. [Finding 1]
2. [Finding 2]
...
```

### Anti-patterns (avoid)

| Wrong | Correct |
|-------|---------|
| Sequential Task messages | Single message with multiple Task calls |
| Use haiku for "simple" subtasks | All subtasks use opus (judgment required) |
| Paste full report in chat | Provide file path |
| **🚨 Main agent reads child outputs** | **Subagents write files, return summaries only** |
| **🚨 Main agent reads aggregated_raw.md** | **Synthesizer subagent handles digest+polish** |
| Delegate Phase 0 to subagent | Main agent executes reconnaissance |
| Use curl/wget | Use MCP tools (Tavily/SerpApi) |
| **🚨 Skip `reddit_research` when Reddit URLs present** | **Trigger skill + load EXTRACTION.md** |
| Use only SerpApi snippets for Reddit | Use JSON API for comment extraction |
| Cite search snippets as "user said" | Extract actual comment text via `.json` endpoint |

---

## 🏆 Best practices (链式门控)

**This section codifies the critical operational guidelines for Reddit Detection Gate → Extraction Gate chain.**

### Practice 1: 永远不要跳过 Gate 1

| Condition | Action | Rationale |
|-----------|--------|-----------|
| Search results contain `reddit.com` URLs | **MUST trigger** `reddit_research/` | Even if user didn't mention Reddit explicitly |
| User mentions pain points/feedback/complaints | **MUST trigger** `reddit_research/` | These topics almost always involve Reddit data |
| Unsure if Reddit is relevant | **Trigger anyway** | False positive is cheap; false negative degrades quality |

**⚠️ VIOLATION CONSEQUENCE**: If Gate 1 is skipped when Reddit URLs are present, the entire research output is considered **DEGRADED**. Final report MUST include: `⚠️ 数据质量警告：未执行 Reddit 评论深度抓取`

### Practice 2: Gate 2 降级路径是可接受的

Extraction Gate may produce three outcomes:

| Outcome | Condition | Action | Report annotation |
|---------|-----------|--------|-------------------|
| ✅ **Full pass** | `stop_reason: completed` + `coverage > 80%` | Use complete data | `✅ 评论完整抓取 (coverage: X%)` |
| ⚠️ **Degraded pass** | Tool unavailable OR partial extraction | Use available data | `⚠️ 数据质量降级：[specific reason]` |
| ❌ **Blocked** | `blocked_requires_login_or_oauth` | **STOP, request human intervention** | See Practice 4 |

**Key insight**: Degraded pass is acceptable—research can proceed with reduced confidence. The critical requirement is **transparent annotation**.

### Practice 3: cookie.txt 是关键依赖

| Check | Frequency | Action if failed |
|-------|-----------|------------------|
| **Existence** | Every Reddit research | STOP, request user to create cookie file |
| **Freshness** (< 7 days) | Every Reddit research | WARN, suggest refresh if stale |
| **Validity** | Before first extraction | Test with small extraction, check `stop_reason` |

**Maintenance protocol**:
```
1. Log in to Reddit in browser
2. Open DevTools → Network → copy full Cookie header
3. Save to project root as cookie.txt (single line)
4. Verify: file mtime should be < 7 days
```

**Why 7 days?** Reddit session cookies typically expire after ~7 days. Stale cookies trigger `blocked_requires_login_or_oauth`.

### Practice 4: 阻塞失败需要人工介入

**CRITICAL**: When extraction is blocked, DO NOT attempt workarounds. STOP and request human intervention.

| Error | Human action required | Agent behavior |
|-------|----------------------|----------------|
| `blocked_requires_login_or_oauth` | Refresh cookie.txt from browser | **STOP**, report to user, wait for fix |
| Repeated `rate_limited` (3+ times) | Wait 10+ minutes OR refresh cookie | **STOP**, report to user, suggest wait |
| `coverage_estimate < 50%` on critical thread | Increase `--max-seconds` OR accept degraded | **ASK** user: proceed degraded or retry? |

**Human intervention request template**:
```
⚠️ **Reddit 抓取被阻止，需要人工介入**

**错误**: [stop_reason]
**影响**: 无法获取完整评论数据
**所需操作**:
1. 从浏览器重新导出 cookie.txt
2. 确认文件位于项目根目录
3. 回复 "已修复" 继续研究

**或者**: 回复 "降级继续" 接受数据质量降低
```

---

## Detailed execution

See [FLOW.md](FLOW.md) for complete 8-phase execution flow.

See [CONTRACT.md](CONTRACT.md) for subagent output validation rules.
