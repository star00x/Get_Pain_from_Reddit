# Subtask: task-003 AI 视频生成质量/可控性痛点研究

## Objective

深入分析 Reddit 上用户对 AI 视频生成工具生成质量、Prompt 遵循度、可控性问题的痛点，识别用户对更可控生成的需求和潜在机会。

## ⚠️ CONTRACT: Verifiable Execution

### PRE-CONDITIONS
- [x] Research objective: 生成质量/可控性问题
- [x] Target sources: r/SoraAi, r/runwayml, r/KlingAI_Videos, r/generativeAI
- [x] MCP tools available

### REQUIRED CHECKS

| Check | Evidence requirement |
|-------|---------------------|
| `relevance_check` | Min 50 chars, cite quality/control related findings |
| `signal_quality_check` | Min 50 chars, explain why these block real workflows |
| `source_credibility_check` | Min 50 chars, note high engagement threads |

### OUTPUT PROTOCOL

1. Write full research to: `runs/2026-01-20-ai-video-research-5454a5/child_outputs/task-003.md`
2. Return JSON per CONTRACT.md schema

## Constraints

- MCP tools only
- Max 10 search rounds
- **Time filter**: `after:2025-07-25`

## 🚨 Reddit Research Requirements (MANDATORY)

### High-Value Threads to Extract

1. `https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/` - 90+ comments
2. `https://www.reddit.com/r/SoraAi/comments/1l8pdf1/sora_ai_keeps_ignoring_specific_visual/` - 20+ comments
3. `https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/` - 40+ comments
4. `https://www.reddit.com/r/KlingAI_Videos/comments/1gwvw5h/major_issues_with_kling_ai_unusable_results/` - 20+ comments

## Language Requirements

- All outputs in **Simplified Chinese**

## Target Sources

- r/SoraAi (primary) - Sora 具体问题
- r/runwayml (primary) - Runway Gen-4 问题
- r/KlingAI_Videos (primary) - Kling 问题
- r/generativeAI (secondary) - 跨工具讨论

## Search Patterns

1. `site:reddit.com Sora "ignores" OR "doesn't follow" prompt instructions after:2025-07-25`
2. `site:reddit.com AI video "physics" OR "unrealistic" OR "unnatural" movement after:2025-07-25`
3. `site:reddit.com AI video "hands" OR "face" OR "fingers" deformed OR weird after:2025-07-25`
4. `site:reddit.com AI video "control" OR "controllable" OR "precise" generation after:2025-07-25`
5. `site:reddit.com AI video "success rate" OR "usable" OR "unusable" results after:2025-07-25`

## Focus Areas

1. **Prompt 遵循度**: 指令被忽略的具体情况
2. **物理真实感**: 运动、重力、交互的不自然
3. **人体变形**: 手、脸、手指等问题
4. **成功率**: 可用输出的比例
5. **可控性需求**: 用户想要的控制粒度

## Critical Filters

- Focus on specific, actionable complaints (not vague "AI isn't ready")
- Prioritize threads with detailed technical descriptions
- Look for "I would pay for X level of control" signals

## Output Format

Must follow Child Output Contract with Opportunity Signals section.
