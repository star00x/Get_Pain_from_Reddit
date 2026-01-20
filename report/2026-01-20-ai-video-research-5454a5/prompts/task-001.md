# Subtask: task-001 AI 视频生成成本/定价痛点研究

## Objective

深入分析 Reddit 上用户对 AI 视频生成工具定价模式、Credits 系统、订阅费用的痛点和不满，识别付费意愿信号和潜在 Micro-SaaS 机会。

## ⚠️ CONTRACT: Verifiable Execution

> **Your output will be mechanically verified. Task FAILS if any condition is not met.**

### PRE-CONDITIONS (verify before starting)
- [x] Research objective is clear: 成本/定价痛点
- [x] Target sources are specified: r/StableDiffusion, r/FluxAI, r/PromptEngineering, r/artificial
- [x] MCP tools are available: Tavily, SerpApi

### REQUIRED CHECKS (with evidence)

| Check | What to verify | Evidence requirement |
|-------|---------------|---------------------|
| `relevance_check` | Do findings address pricing pain points? | Min 50 chars, cite specific findings |
| `signal_quality_check` | Are pain signals genuine (with payment willingness)? | Min 50 chars, explain why signals are real |
| `source_credibility_check` | Are sources trustworthy customer communities? | Min 50 chars, note community size/engagement |

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
   Write: file_path = "runs/2026-01-20-ai-video-research-5454a5/child_outputs/task-001.md"
   ```

2. **Return JSON (strict schema)** - see CONTRACT.md for full schema

## Constraints

- Use MCP tools only (prefer Tavily: `tavily_search` / `tavily_extract`; SerpApi for Google site search)
- No native network commands (wget/curl)
- Search/extract iteration limit: max 10 rounds
- **Time filter**: All search queries MUST include `after:2025-07-25`

## 🚨 Reddit Research Requirements (MANDATORY)

### High-Value Threads to Extract

1. `https://www.reddit.com/r/artificial/comments/1n7t4f5/why_are_ai_image_and_video_generators_so/` - 50+ comments
2. `https://www.reddit.com/r/StableDiffusion/comments/1ljbuw6/a_rant_about_the_cost_of_ai_generation_and_how/` - 40+ comments
3. `https://www.reddit.com/r/PromptEngineering/comments/1n02v3h/the_12_beginner_mistakes_that_killed_my_first/` - 20+ comments
4. `https://www.reddit.com/r/PromptEngineering/comments/1mxb375/how_i_cut_my_ai_video_costs_by_80_and_actualy_got/` - 20+ comments
5. `https://www.reddit.com/r/FluxAI/comments/1gpe316/the_cost_of_ai_video_generation_is_very_high_its/` - 20+ comments

### Extraction Method

Use Tavily Extract with JSON endpoint:
```
tavily_extract:
  urls: ["<reddit_url>.json?sort=top&limit=100"]
  format: "markdown"
```

Or if available, use Python script:
```bash
python3 tools/reddit_thread_best_effort.py "<url>" \
  --sort top --limit 500 --min-score 5 \
  --output-analysis-md analysis.md
```

### Data Quality Annotation

If JSON API extraction not executed, output MUST include:
```
⚠️ 数据质量警告：未执行 Reddit 评论深度抓取
```

## Language Requirements

- All outputs must be in **Simplified Chinese**

## Target Sources

- r/StableDiffusion (primary) - 开源社区，成本敏感用户
- r/FluxAI (primary) - 成本讨论活跃
- r/PromptEngineering (secondary) - 优化成本的用户
- r/artificial (secondary) - 通用讨论

## Search Patterns

High-intent queries (ALL include time filter):
1. `site:reddit.com AI video generation "expensive" OR "cost" OR "pricing" after:2025-07-25`
2. `site:reddit.com AI video "credits" OR "subscription" "too expensive" after:2025-07-25`
3. `site:reddit.com "burned through" OR "wasted" credits AI video after:2025-07-25`
4. `site:reddit.com AI video generation ROI "worth it" OR "not worth" after:2025-07-25`

## Focus Areas

1. **Credits 系统痛点**: 透明度、消耗速度、失败生成是否退款
2. **订阅定价**: 月费是否合理、与价值是否匹配
3. **学习成本**: 新手浪费的金钱
4. **付费意愿信号**: 用户愿意为什么付费、价格敏感度
5. **成本优化方案**: 用户采用的省钱策略

## Critical Filters

- Echo chamber trap: Avoid r/SaaS, r/Entrepreneur (use only for competitive intel)
- Free solution test: Check if top comments recommend free alternatives
- Payment signal priority: "I'd pay for", "worth paying", "already paying"

## Output Format

Must follow Child Output Contract with:
- `## Scope & Inputs`
- `## Key Findings` (Pain Points with frequency/intensity)
- `## Evidence (with citations)` (≥2 links, verbatim quotes)
- `## Opportunity Signals` (Micro-SaaS specific)
- `## Gaps & Next Steps`
