# Synthesizer Subagent Template

Template for analysis, synthesis, and final polish. Requires `opus` model for semantic understanding.

---

## Template

```markdown
# Subtask: synthesizer [Synthesis Task Title]

## Objective

[Clear description of synthesis/analysis objective]

## ⚠️ CONTRACT: Verifiable Execution

> **Your output will be mechanically verified. Task FAILS if any condition is not met.**

### PRE-CONDITIONS (verify before starting)
- [ ] Aggregated file exists at specified path
- [ ] Research objective is clear
- [ ] Target audience is defined

### REQUIRED CHECKS (with evidence)

You MUST perform these checks and record **specific evidence**:

| Check | What to verify | Evidence requirement |
|-------|---------------|---------------------|
| `completeness_check` | All major findings from aggregated input are represented | Min 100 chars, list what's included/excluded |
| `coherence_check` | Report flows logically, no contradictions | Min 100 chars, explain narrative structure |
| `actionability_check` | Recommendations are specific and actionable | Min 50 chars, cite specific recommendations |
| `citation_integrity` | All claims have sources, no broken links | Min 50 chars, note citation count |

### POST-CONDITIONS (mechanically verified)

Your JSON output will be validated. **Task FAILS if**:
- Any required field is missing
- Any `evidence` field is < 50 characters (100 for completeness/coherence)
- `key_findings` array has < 3 items
- `report_sections` array is empty
- Any `check.executed` != true

### OUTPUT PROTOCOL

1. **Write polished report to file**:
   ```
   Write: file_path = "[RUN_DIR]/polished_report.md"
   ```

2. **Return JSON (strict schema)**:

```json
{
  "task_id": "synthesizer",
  "status": "completed | partial | failed",
  "output_file": "[RUN_DIR]/polished_report.md",
  "checks_performed": {
    "completeness_check": {
      "executed": true,
      "evidence": "[具体证据：哪些发现被纳入，是否有遗漏，至少100字]",
      "verdict": "pass | fail | partial"
    },
    "coherence_check": {
      "executed": true,
      "evidence": "[具体证据：报告结构逻辑，叙事连贯性，至少100字]",
      "verdict": "pass | fail | partial"
    },
    "actionability_check": {
      "executed": true,
      "evidence": "[具体证据：建议的具体性和可执行性]",
      "verdict": "pass | fail | partial"
    },
    "citation_integrity": {
      "executed": true,
      "evidence": "[具体证据：引用数量和完整性]",
      "verdict": "pass | fail | partial",
      "citation_count": 15
    }
  },
  "executive_summary": {
    "key_findings": [
      "[核心发现1 - 一句话]",
      "[核心发现2]",
      "[核心发现3]"
    ],
    "opportunities_identified": 3,
    "recommended_next_steps": [
      "[具体建议1]",
      "[具体建议2]"
    ]
  },
  "report_structure": {
    "sections": ["执行摘要", "核心痛点", "竞品分析", "机会评估", "后续建议"],
    "word_count": 2500,
    "citation_count": 15
  }
}
```

**Evidence Examples**:

❌ Bad: `"evidence": "报告完整"` (too short, no specifics)

✅ Good: `"evidence": "报告涵盖了aggregated_raw中的全部5个核心痛点和3个竞品分析，每个痛点都有2-3个用户原话支撑，仅排除了2个低置信度发现（来源不明确）"`

## Input Context

[Description of inputs this subtask will receive or access]

## Constraints

- Use MCP tools for any web access (prefer Tavily/SerpApi)
- Analysis depth: [deep/moderate/surface]
- Return immediately upon completion

## Language Requirements

- All outputs must be in **Simplified Chinese** unless user specifies otherwise

## Analysis Framework

[Specify the analytical lens to apply]

1. [Framework dimension 1]
2. [Framework dimension 2]
3. [Framework dimension 3]

## Expected Deliverables

1. **[Deliverable 1]**: [description]
2. **[Deliverable 2]**: [description]
3. **[Deliverable 3]**: [description]

## Output Format (written to file, NOT returned)

### 执行摘要
[2-3 paragraph executive summary]

### 主要发现
#### [Category 1]
- Finding 1
- Finding 2

#### [Category 2]
- Finding 1
- Finding 2

### 证据支撑
- [Source 1](https://...) — supports [finding]
- [Source 2](https://...) — supports [finding]

### 机会评估 (if Micro-SaaS research)
[Five-dimension scoring table]

### 数据缺口与后续建议
- Analysis limitations: [what couldn't be determined]
- Recommended follow-ups: [specific next steps]
```

---

## Instantiation example: Competitive analysis

```markdown
# Subtask: task-004 Competitive Weakness Analysis - Invoicing Tools

## Objective

Map systematic weaknesses of top invoicing tools (FreshBooks, QuickBooks, Wave) based on user complaints.

## Input Context

- Search public review sites and Reddit discussions
- Focus on recurring complaint patterns, not isolated incidents

## Constraints

- Use MCP tools for all web access
- Analysis depth: deep
- Return immediately upon completion

## Language Requirements

- All outputs in **Simplified Chinese**

## Analysis Framework

1. **Feature gaps**: What users say is missing
2. **UX friction**: Interface and workflow complaints
3. **Pricing pain**: Cost-related objections
4. **Integration failures**: What doesn't connect well
5. **Support quality**: Customer service complaints

## Expected Deliverables

1. **Weakness matrix**: Tool × weakness category grid
2. **Opportunity gaps**: Underserved needs across all tools
3. **Positioning recommendations**: How a new entrant could differentiate

## Output Format

[As specified in Child Output Contract]
```

---

## Instantiation example: Micro-SaaS opportunity synthesis

```markdown
# Subtask: task-005 Opportunity Synthesis - [Domain]

## Objective

Synthesize findings from research subtasks into scored opportunity candidates using the five-dimension model.

## Input Context

- Aggregated findings from task-001 through task-004
- Pain points, competitor weaknesses, user quotes

## Constraints

- No additional web research (synthesis only)
- Apply microsaas_eval framework strictly
- Return immediately upon completion

## Language Requirements

- All outputs in **Simplified Chinese**

## Analysis Framework (Five Dimensions)

1. **Demand Rigidity**: Will users pay? Evidence of urgency?
2. **Feature Focus**: Can value be described in one sentence?
3. **Technical Feasibility**: Can solo dev ship MVP in 2-4 weeks?
4. **API Availability**: Are required APIs mature and documented?
5. **SEO Potential**: Can content drive organic acquisition?

## Expected Deliverables

1. **Opportunity candidates**: 3-5 ranked opportunities
2. **Per-opportunity scoring**: 🟢/🟡/🔴 for each dimension
3. **Go/No-go recommendation**: ✅ Strong / ⚠️ Conditional / ❌ Pass
4. **Next steps**: Specific validation actions for top candidates

## Output Format

### Scope & Inputs
- Synthesis scope: [domains covered]
- Source subtasks: [task-001, task-002, ...]

### Key Findings
#### Opportunity 1: [Name]
| Dimension | Score | Evidence |
|-----------|-------|----------|
| Demand | 🟢/🟡/🔴 | [citation] |
| Focus | 🟢/🟡/🔴 | [description] |
| Tech | 🟢/🟡/🔴 | [complexity notes] |
| API | 🟢/🟡/🔴 | [API names] |
| SEO | 🟢/🟡/🔴 | [keyword notes] |

**Verdict**: ✅/⚠️/❌
**Rationale**: [2-3 sentences]
**Next steps**: [specific actions]

### Evidence (with citations)
[Links to source findings]

### Gaps & Next Steps
[What needs further validation]
```

---

## Instantiation example: Full digest + polish (Phase 6-7)

This is the primary use case for token optimization.

```markdown
# Subtask: synthesizer Digest and Polish Research Report

## Objective

Read aggregated_raw.md, identify patterns and gaps, produce client-ready polished_report.md.

## ⚠️ CRITICAL: Output Protocol

1. **Read input**: `[RUN_DIR]/aggregated_raw.md`
2. **Write output**: `[RUN_DIR]/polished_report.md`
3. **Return ONLY**: Executive summary (< 500 tokens)

## Input Context

- Aggregated file: `runs/2024-12-28-invoice-abc123/aggregated_raw.md`
- Contains raw outputs from 4 research subtasks
- Topic: Invoice management pain points for SMBs

## Execution Steps

### Step 1: Digest (identify patterns)

Read aggregated_raw.md and identify:
- **Coverage**: Which dimensions are well-covered?
- **Duplicates**: Overlapping findings across subtasks
- **Gaps**: Missing perspectives or data
- **Top signals**: Highest-confidence pain points

### Step 2: Design outline

```markdown
# [Topic] 研究报告

## 执行摘要
[Synthesize top 3-5 findings]

## 核心痛点
### 痛点 1: [Name]
### 痛点 2: [Name]
...

## 竞品分析
[If applicable]

## 机会评估
[Five-dimension scoring if Micro-SaaS]

## 数据局限与后续建议
```

### Step 3: Polish section by section

For each section:
1. Extract relevant content from aggregated_raw.md
2. Deduplicate and synthesize
3. Ensure consistent citation format
4. Write to polished_report.md

### Step 4: Return summary only

```
## Synthesis Complete
- **Output file**: runs/2024-12-28-invoice-abc123/polished_report.md
- **Report sections**: 执行摘要, 核心痛点(5), 竞品分析, 机会评估, 后续建议
- **Key findings** (top 3):
  1. 追款是最大痛点，占 79% 的投诉
  2. 自由职业者更关注易用性，小企业更关注集成
  3. Wave 被频繁提及为"够用但不好用"的选择
- **Opportunities identified**: 3
- **Recommended next steps**: 验证 QuickBooks 用户迁移意愿
```

## Language Requirements

- Polished report: **Simplified Chinese**
- Return summary: English (for main agent parsing)
```

---

## Model selection

**All synthesizer subtasks → `opus`**

Synthesis tasks inherently require judgment:
- Identifying what's important vs noise
- Resolving conflicting findings
- Structuring narrative for target audience
- Ensuring coherent, non-redundant output

Even "simple aggregation" in research context requires deciding **what to keep** and **what to merge**.
