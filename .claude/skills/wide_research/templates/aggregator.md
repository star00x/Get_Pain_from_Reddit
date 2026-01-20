# Aggregator Subagent Template

Template for collecting, validating, and quality-checking child outputs. Uses `opus` model (requires judgment).

> **Token Optimization**: This subagent reads files and writes output directly. Main agent never sees full content.

---

## Template

```markdown
# Subtask: aggregator Collect, Validate, and Quality-Check Outputs

## Objective

Read all child output files, validate format AND content quality, identify cross-task issues, concatenate into aggregated_raw.md.

## ⚠️ CONTRACT: Verifiable Execution

> **Your output will be mechanically verified. Task FAILS if any condition is not met.**

### PRE-CONDITIONS (verify before starting)
- [ ] Run directory exists
- [ ] Child output files exist in `child_outputs/`
- [ ] Research objective is provided

### REQUIRED CHECKS (with evidence)

You MUST perform these checks and record **specific evidence**:

| Check | What to verify | Evidence requirement |
|-------|---------------|---------------------|
| `format_validation` | All child outputs have required sections | Min 50 chars, list which passed/failed |
| `content_quality` | Findings are substantive, not vague platitudes | Min 100 chars, cite specific quality issues |
| `cross_task_consistency` | Findings across tasks don't contradict | Min 100 chars, note any conflicts |
| `coverage_assessment` | Research objective dimensions are covered | Min 50 chars, list gaps if any |

### POST-CONDITIONS (mechanically verified)

Your JSON output will be validated. **Task FAILS if**:
- Any required field is missing
- Any `evidence` field is < 50 characters (100 for quality/consistency)
- `collective_findings` array has < 3 items
- Any `check.executed` != true

### OUTPUT PROTOCOL

1. **Write aggregated output to file**:
   ```
   Write: file_path = "[RUN_DIR]/aggregated_raw.md"
   ```

2. **Return JSON (strict schema)**:

```json
{
  "task_id": "aggregator",
  "status": "completed | partial | failed",
  "output_file": "[RUN_DIR]/aggregated_raw.md",
  "checks_performed": {
    "format_validation": {
      "executed": true,
      "evidence": "[具体证据：哪些子任务通过/失败格式验证，原因]",
      "verdict": "pass | fail | partial",
      "details": {
        "total": 4,
        "passed": 3,
        "failed": 1,
        "failed_tasks": ["task-003"]
      }
    },
    "content_quality": {
      "executed": true,
      "evidence": "[具体证据：内容质量评估，是否有空洞断言，至少100字]",
      "verdict": "pass | fail | partial"
    },
    "cross_task_consistency": {
      "executed": true,
      "evidence": "[具体证据：跨任务一致性分析，是否有矛盾，至少100字]",
      "verdict": "pass | fail | partial",
      "conflicts": ["task-001 says X, task-002 says Y"]
    },
    "coverage_assessment": {
      "executed": true,
      "evidence": "[具体证据：覆盖度评估，哪些维度已覆盖/缺失]",
      "verdict": "pass | fail | partial",
      "gaps": ["enterprise segment not covered"]
    }
  },
  "quality_assessment": {
    "overall_quality": "high | medium | low",
    "collective_findings": [
      "[跨任务发现1 - 多个子任务共同支持]",
      "[跨任务发现2]",
      "[跨任务发现3]"
    ],
    "unexpected_insights": "[意外发现，或 'none']",
    "recommended_action": "proceed | retry:task-X | adjust_scope | escalate"
  },
  "stats": {
    "total_subtasks": 4,
    "validated": 3,
    "failed": 1,
    "total_citations": 18
  }
}
```

**Evidence Examples**:

❌ Bad: `"evidence": "质量良好"` (too short, no specifics)

✅ Good: `"evidence": "4个子任务中3个提供了具体用户原话和高赞数据(↑20+)，task-003仅有模糊描述'用户不满意'缺乏具体证据，标记为partial"`

## Input

- Run directory: `[RUN_DIR]`
- Child output files: `[RUN_DIR]/child_outputs/task-*.md`
- Research objective: `[OBJECTIVE]` (for relevance checking)

## Validation Rules

### Layer 1: Format Validation (from CONTRACT.md)

| Check | Requirement | Action on failure |
|-------|-------------|-------------------|
| Section presence | `## Scope & Inputs`, `## Key Findings`, `## Evidence` | Mark failed |
| Citation count | ≥2 Markdown links | Mark failed |
| No placeholders | No `<id>`, `${...}`, `TODO`, `TBD` | Mark failed |
| Language | Simplified Chinese | Mark failed |

### Layer 2: Content Quality Validation (requires judgment)

| Check | What to assess | Action on issue |
|-------|----------------|-----------------|
| **Relevance** | Does content address the research objective? | Flag as "off-topic" |
| **Substance** | Are findings specific or vague platitudes? | Flag as "low-value" |
| **Consistency** | Do findings across subtasks contradict? | Note in conflicts list |
| **Completeness** | Are there obvious gaps in coverage? | Note in gaps list |
| **Signal quality** | Are pain points genuine or echo-chamber noise? | Flag questionable signals |

## Execution Steps

1. **Read research objective** from prompt (for relevance checking)

2. **List and read all child outputs**:
   ```
   Glob: pattern = "[RUN_DIR]/child_outputs/task-*.md"
   ```

3. **For each file, validate format AND content**:
   - Format checks (section, citation, placeholder, language)
   - Content checks (relevance, substance, signal quality)
   - Record both validation results

4. **Cross-task analysis**:
   - Identify contradictions between subtasks
   - Identify overlapping/duplicate findings
   - Identify coverage gaps
   - Synthesize top collective findings

5. **Concatenate valid outputs** (include warnings for flagged content):
   ```markdown
   # Wide Research: [Topic]

   ---

   ## Subtask 001: [Title]

   [content from task-001.md]

   ---

   ## Subtask 002: [Title]
   > ⚠️ Aggregator note: Some findings flagged as low-relevance

   [content from task-002.md]

   ---
   ...
   ```

6. **Write aggregated file**:
   ```
   Write: file_path = "[RUN_DIR]/aggregated_raw.md", content = aggregated
   ```

7. **Return layered summary** (Layer 1 + Layer 2)

## Error Handling

- Format failure → include task-id in `Failed validations`
- Content quality issues → include in `Quality Assessment` with specific flags
- Cross-task conflicts → document in summary, let main agent decide
- Do NOT retry — main agent will decide strategy based on assessment

## Language Requirements

- Aggregated output language: **Simplified Chinese**
- Return summary: English (for main agent parsing)
```

---

## Instantiation example

```markdown
# Subtask: aggregator Collect, Validate, and Quality-Check Outputs

## Objective

Read all child output files from runs/2024-12-28-invoice-abc123/, validate format and content quality, concatenate.

## Input

- Run directory: `runs/2024-12-28-invoice-abc123`
- Child output files: `runs/2024-12-28-invoice-abc123/child_outputs/task-*.md`
- Research objective: "Identify invoice management pain points for SMBs to validate Micro-SaaS opportunity"

## Execution

[Follow template steps]

## Return Format

## Aggregation Status
- **Total subtasks**: 4
- **Validated**: 3 passed, 1 failed
- **Output file**: runs/2024-12-28-invoice-abc123/aggregated_raw.md
- **Total citations**: 18
- **Failed validations**: task-003 (missing citations)

## Quality Assessment
- **Cross-task consistency**: minor conflicts (task-001 says "追款" is #1 pain, task-002 says "格式" is #1)
- **Coverage gaps**: No data on enterprise segment
- **Top 3 collective findings**:
  1. 追款/催款是跨所有细分市场的最高频痛点
  2. 现有工具（Wave, QuickBooks）被认为"够用但不好用"
  3. 自由职业者更关注移动端体验
- **Unexpected insights**: Multiple mentions of "AI 自动分类" as emerging need
- **Recommended actions**: proceed (conflicts are minor, can resolve in synthesis)
```

---

## Model selection

| Task | Model | Rationale |
|------|-------|-----------|
| Aggregation + validation + quality check | `opus` | Requires judgment: relevance, consistency, signal quality |

**Why not haiku?**
- haiku can only do format validation (section exists, citation count)
- haiku cannot judge: Is the content relevant? Is it valuable? Are findings consistent?
- Using haiku = "rubber stamp" validation, garbage in → garbage out
