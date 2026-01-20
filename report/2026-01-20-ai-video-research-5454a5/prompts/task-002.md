# Subtask: task-002 AI 视频角色/场景一致性痛点研究

## Objective

深入分析 Reddit 上用户对 AI 视频生成工具中角色一致性、场景连贯性问题的痛点，识别现有解决方案的缺陷和潜在 Micro-SaaS 机会。

## ⚠️ CONTRACT: Verifiable Execution

> **Your output will be mechanically verified. Task FAILS if any condition is not met.**

### PRE-CONDITIONS
- [x] Research objective: 角色/场景一致性问题
- [x] Target sources: r/SoraAi, r/generativeAI, r/aitubers, r/n8n, r/StableDiffusion
- [x] MCP tools available

### REQUIRED CHECKS (with evidence)

| Check | Evidence requirement |
|-------|---------------------|
| `relevance_check` | Min 50 chars, cite specific consistency-related findings |
| `signal_quality_check` | Min 50 chars, explain why these are real workflow blockers |
| `source_credibility_check` | Min 50 chars, note community engagement levels |

### OUTPUT PROTOCOL

1. Write full research to: `runs/2026-01-20-ai-video-research-5454a5/child_outputs/task-002.md`
2. Return JSON per CONTRACT.md schema

## Constraints

- MCP tools only, no wget/curl
- Max 10 search rounds
- **Time filter**: `after:2025-07-25`

## 🚨 Reddit Research Requirements (MANDATORY)

### High-Value Threads to Extract

1. `https://www.reddit.com/r/generativeAI/comments/1mbwbyt/can_anybody_tell_me_how_to_create_consistent_ai/` - 50+ comments
2. `https://www.reddit.com/r/aitubers/comments/1omwufw/any_ai_tools_for_consistent_character_animation/` - 20+ comments
3. `https://www.reddit.com/r/n8n/comments/1or1gwi/i_built_an_ai_automation_that_generates_unlimited/` - 20+ comments
4. `https://www.reddit.com/r/grok/comments/1ogq0sy/keeping_character_appearance_consistent_across/` - 10+ comments
5. `https://www.reddit.com/r/generativeAI/comments/1lfzzz3/best_texttovideo_models_for_character_scene/` - 10+ comments

### Extraction Method

Use Tavily Extract or Python script per EXTRACTION.md guidelines.

## Language Requirements

- All outputs in **Simplified Chinese**

## Target Sources

- r/generativeAI (primary) - 跨工具讨论
- r/aitubers (primary) - YouTube 创作者，一致性核心需求
- r/SoraAi (secondary) - Sora 用户
- r/n8n (secondary) - 自动化方案
- r/StableDiffusion (secondary) - LoRA 等技术方案

## Search Patterns

1. `site:reddit.com AI video "consistent character" OR "character consistency" after:2025-07-25`
2. `site:reddit.com AI video "same character" "multiple clips" OR "across scenes" after:2025-07-25`
3. `site:reddit.com AI video "character sheet" OR "reference image" consistency after:2025-07-25`
4. `site:reddit.com "video LoRA" OR "train LoRA" character consistency after:2025-07-25`

## Focus Areas

1. **角色外观一致性**: 跨片段人物变化问题
2. **场景连贯性**: 背景、道具、光线等一致性
3. **现有解决方案**: LoRA 训练、参考图、特定工具
4. **技术门槛**: 用户实现一致性的难度
5. **工作流痛点**: 多工具组合的复杂性

## Critical Filters

- Echo chamber trap: Avoid builder communities
- Free solution test: Check if LoRA training or free tools fully solve the problem
- DIY workaround signals: Users building complex pipelines = opportunity

## Output Format

Must follow Child Output Contract with Opportunity Signals section.
