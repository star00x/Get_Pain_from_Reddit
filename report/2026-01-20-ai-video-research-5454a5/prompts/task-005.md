# Subtask: task-005 AI 视频生成竞品分析与市场格局研究

## Objective

分析 Reddit 上用户对主流 AI 视频生成工具（Sora, Runway, Kling, Pika, HeyGen, VEO3 等）的对比评价，识别各工具的优劣势、市场空白和潜在机会。

## ⚠️ CONTRACT: Verifiable Execution

### PRE-CONDITIONS
- [x] Research objective: 竞品分析与市场格局
- [x] Target sources: r/singularity, r/artificial, r/generativeAI, r/premiere
- [x] MCP tools available

### REQUIRED CHECKS

| Check | Evidence requirement |
|-------|---------------------|
| `relevance_check` | Min 50 chars, cite tool comparison findings |
| `signal_quality_check` | Min 50 chars, explain user experience basis |
| `source_credibility_check` | Min 50 chars, note active user communities |

### OUTPUT PROTOCOL

1. Write full research to: `runs/2026-01-20-ai-video-research-5454a5/child_outputs/task-005.md`
2. Return JSON per CONTRACT.md schema

## Constraints

- MCP tools only
- Max 10 search rounds
- **Time filter**: `after:2025-07-25`

## 🚨 Reddit Research Requirements (MANDATORY)

### High-Value Threads to Extract

1. `https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/` - 90+ comments
2. `https://www.reddit.com/r/artificial/comments/1mi9y9m/whats_the_current_frontier_in_aigenerated/` - 70+ comments
3. `https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/` - 320+ comments

## Language Requirements

- All outputs in **Simplified Chinese**

## Target Sources

- r/singularity (primary) - AI 前沿讨论
- r/artificial (primary) - 通用 AI 讨论
- r/generativeAI (primary) - 生成式 AI 讨论
- r/premiere (secondary) - 专业用户视角

## Search Patterns

1. `site:reddit.com "Sora vs" OR "Runway vs" OR "Kling vs" comparison after:2025-07-25`
2. `site:reddit.com "best AI video generator" 2025 after:2025-07-25`
3. `site:reddit.com AI video "switched from" OR "moved to" tool after:2025-07-25`
4. `site:reddit.com AI video "pros and cons" OR "honest review" after:2025-07-25`
5. `site:reddit.com Sora Runway Kling Pika VEO3 comparison after:2025-07-25`

## Focus Areas

1. **工具对比**: 各工具的优缺点
2. **用户迁移**: 从 A 工具到 B 工具的原因
3. **市场空白**: 没有工具解决的问题
4. **定位差异**: 各工具的目标用户和场景
5. **未来趋势**: 用户期待的功能和方向

## Competitive Intelligence Framework

For each major tool, capture:
- **Strengths mentioned**: What users praise
- **Weaknesses mentioned**: What users complain about
- **Ideal use case**: When users recommend it
- **Churn reasons**: Why users leave
- **Pricing perception**: Too expensive / fair / good value

### Tools to cover
- OpenAI Sora
- Runway Gen-4
- Kling AI
- Pika Labs
- Google VEO3
- HeyGen (avatar-focused)
- Hailuo AI
- Stable Diffusion video models

## Critical Filters

- Prioritize actual user experiences over speculation
- Weight recent reviews (last 6 months) higher
- Look for switching patterns and reasons

## Output Format

Must follow Child Output Contract with:
- Competitive landscape matrix
- Gap analysis for Micro-SaaS opportunities
- Opportunity Signals section
