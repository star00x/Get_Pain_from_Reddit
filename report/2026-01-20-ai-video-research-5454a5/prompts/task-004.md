# Subtask: task-004 AI 视频工作流/批量自动化需求研究

## Objective

深入分析 Reddit 上用户对 AI 视频批量生成、自动化工作流、多平台适配的需求，识别工作流工具化的机会。

## ⚠️ CONTRACT: Verifiable Execution

### PRE-CONDITIONS
- [x] Research objective: 工作流/批量自动化需求
- [x] Target sources: r/automation, r/n8n, r/PromptEngineering, r/premiere
- [x] MCP tools available

### REQUIRED CHECKS

| Check | Evidence requirement |
|-------|---------------------|
| `relevance_check` | Min 50 chars, cite workflow/automation findings |
| `signal_quality_check` | Min 50 chars, explain business context and scale |
| `source_credibility_check` | Min 50 chars, note professional user signals |

### OUTPUT PROTOCOL

1. Write full research to: `runs/2026-01-20-ai-video-research-5454a5/child_outputs/task-004.md`
2. Return JSON per CONTRACT.md schema

## Constraints

- MCP tools only
- Max 10 search rounds
- **Time filter**: `after:2025-07-25`

## 🚨 Reddit Research Requirements (MANDATORY)

### High-Value Threads to Extract

1. `https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/` - 100+ comments
2. `https://www.reddit.com/r/PromptEngineering/comments/1mzan5d/my_complete_ai_video_workflow_that_generates_20/` - 10+ comments
3. `https://www.reddit.com/r/automation/comments/1mivv0a/i_built_a_fully_automated_ai_video_factory_heres/` - 10+ comments
4. `https://www.reddit.com/r/automation/comments/1q9xvhw/how_are_you_automating_1000_product_showcase/` - 9 comments
5. `https://www.reddit.com/r/automation/comments/1pdkrwj/what_i_learned_from_burning_500_on_ai_video/` - 10+ comments

## Language Requirements

- All outputs in **Simplified Chinese**

## Target Sources

- r/automation (primary) - 自动化工作流用户
- r/n8n (primary) - n8n 用户，技术解决方案
- r/PromptEngineering (primary) - 高产出用户
- r/premiere (secondary) - 专业视频编辑需求

## Search Patterns

1. `site:reddit.com AI video "batch" OR "bulk" generation automation after:2025-07-25`
2. `site:reddit.com AI video workflow "20+" OR "100+" videos weekly after:2025-07-25`
3. `site:reddit.com AI video "TikTok" OR "Instagram" OR "YouTube" multiple platforms after:2025-07-25`
4. `site:reddit.com AI video n8n OR Make OR Zapier automation after:2025-07-25`
5. `site:reddit.com AI video "product showcase" OR "e-commerce" bulk after:2025-07-25`

## Focus Areas

1. **批量生成需求**: 用户需要多少量级的视频
2. **多平台适配**: 不同平台尺寸/格式需求
3. **自动化流水线**: 用户构建的 DIY 方案
4. **工具集成**: 与现有工具的连接需求
5. **内容规模化**: 商业/营销用途的规模需求

## Critical Filters

- Prioritize B2B signals: "for my clients", "for my business", "agency"
- Look for quantified scale: "20+ videos/week", "1000+ products"
- DIY workaround signals: Users building complex n8n/Make workflows = opportunity

## Output Format

Must follow Child Output Contract with Opportunity Signals section.
