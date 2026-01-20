# 侦察报告：AI 视频生成工具痛点研究

## 执行日期
2026-01-20

## 研究目标
深度调研 Reddit 上关于 AI 生成视频的细分需求和真实痛点，挖掘相关的 Micro-SaaS 机会。

## MCP 工具可用性
- ✅ Tavily MCP: 可用
- ✅ SerpApi MCP: 可用
- ✅ cookie.txt: 存在 (2026-01-12)

## Reddit Detection Gate
**状态**: ✅ PASSED

搜索结果包含 30+ 个 reddit.com URLs，`reddit_research` skill 已触发。

## 已识别的核心研究维度

### 维度 1: 成本/定价痛点 (最高频)
**信号强度**: ★★★★★

关键发现：
- Credits 系统不透明、消耗快
- 失败生成仍消耗 credits（"burned through 4000 credits without getting a single usable result"）
- 订阅费用高 ($150-250/月)
- 学习成本高（"$1500 killed in beginner mistakes"）

高价值线程：
1. [Why are AI image and video generators so expensive](https://www.reddit.com/r/artificial/comments/1n7t4f5/) - 50+ comments
2. [A rant about the cost of AI generation](https://www.reddit.com/r/StableDiffusion/comments/1ljbuw6/) - 40+ comments
3. [The real cost of AI video generation](https://www.reddit.com/r/indiehackers/comments/1mxbr59/) - 8 comments
4. [The 12 beginner mistakes that killed my first $1500](https://www.reddit.com/r/PromptEngineering/comments/1n02v3h/) - 20+ comments
5. [The cost of AI video generation is very high - $180/hour](https://www.reddit.com/r/FluxAI/comments/1gpe316/) - 20+ comments

### 维度 2: 角色/场景一致性问题 (高频)
**信号强度**: ★★★★☆

关键发现：
- 跨片段角色外观不一致是重大痛点
- 需要专门的 workflow 保持一致性
- 训练 LoRA 等技术门槛高
- 工具如 Zeemo 尝试解决但用户体验不一

高价值线程：
1. [Keeping character appearance consistent across scenes](https://www.reddit.com/r/grok/comments/1ogq0sy/) - 10+ comments
2. [Best text-to-video models for character + scene consistency](https://www.reddit.com/r/generativeAI/comments/1lfzzz3/) - 10+ comments
3. [Same characters multiple clips](https://www.reddit.com/r/SoraAi/comments/1jodxaz/) - 5 comments
4. [Any AI tools for consistent character animation](https://www.reddit.com/r/aitubers/comments/1omwufw/) - 20+ comments
5. [Can anybody tell me how to create consistent AI character](https://www.reddit.com/r/generativeAI/comments/1mbwbyt/) - 50+ comments

### 维度 3: 生成质量/可控性问题 (高频)
**信号强度**: ★★★★☆

关键发现：
- Prompt 经常被忽略（"Sora consistently ignores basic visual instructions"）
- 物理运动不自然
- 人脸/手部变形
- 成功率低（"1 in 20 shots are useable"）

高价值线程：
1. [Why is Sora so bad despite all the hype](https://www.reddit.com/r/singularity/comments/1hqvg5h/) - 90+ comments
2. [SORA AI keeps ignoring specific visual instructions](https://www.reddit.com/r/SoraAi/comments/1l8pdf1/) - 20+ comments
3. [Gen-4 honest opinion! Disappointing but better than nothing](https://www.reddit.com/r/runwayml/comments/1jor1t4/) - 40+ comments
4. [Major Issues with Kling AI: Unusable Results](https://www.reddit.com/r/KlingAI_Videos/comments/1gwvw5h/) - 20+ comments

### 维度 4: 工作流/批量自动化需求 (中高频)
**信号强度**: ★★★★☆

关键发现：
- 批量生成需求强烈
- 多平台适配（TikTok/IG/YouTube）痛点
- 自动化流水线构建复杂
- 用户在用 n8n, Make 等工具拼凑方案

高价值线程：
1. [My complete AI video workflow that generates 20+ videos per week](https://www.reddit.com/r/PromptEngineering/comments/1mzan5d/) - 10+ comments
2. [I built a fully automated AI video factory](https://www.reddit.com/r/automation/comments/1mivv0a/) - 10+ comments
3. [How are you automating 1000+ product showcase videos](https://www.reddit.com/r/automation/comments/1q9xvhw/) - 9 comments
4. [Bulk Auto AI Video Creator](https://www.reddit.com/r/AI_Agents/comments/1kj8nbu/) - 2 comments
5. [everything I learned after 10000 AI video generations](https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/) - 100+ comments

### 维度 5: 工具稳定性/可用性 (中频)
**信号强度**: ★★★☆☆

关键发现：
- HeyGen 变得不可用（"sits on 97% for 30+ minutes"）
- 生成速度慢
- Watermark 去除需求

高价值线程：
1. [HeyGen Studio has become unusable](https://www.reddit.com/r/generativeAI/comments/1mjyfpw/) - 10+ comments
2. [I got tired of Sora's watermark](https://www.reddit.com/r/SoraAi/comments/1odhoht/) - 50+ comments

## 目标社区（客户社区）

| 社区 | 用户类型 | 研究价值 |
|------|---------|---------|
| r/runwayml | Runway 用户 | 工具具体问题 |
| r/SoraAi | Sora 用户 | 质量/可控性问题 |
| r/KlingAI_Videos | Kling 用户 | 工具问题 |
| r/generativeAI | 通用 AI 生成用户 | 跨工具痛点 |
| r/StableDiffusion | 开源社区 | 成本/技术方案 |
| r/PromptEngineering | Prompt 优化者 | 工作流/成本优化 |
| r/artificial | AI 讨论者 | 市场观察 |
| r/automation | 自动化工作流 | 批量/流水线需求 |
| r/n8n | 自动化工具用户 | 集成需求 |
| r/aitubers | AI YouTube 创作者 | 一致性/工作流 |

## 避开的 Builder Echo Chamber

- r/SaaS
- r/Entrepreneur
- r/startups
- r/microsaas
- r/indiehackers（仅用于竞品观察）

## 子任务分解

| Task ID | 研究维度 | 目标社区 | 预期输出 |
|---------|---------|---------|---------|
| task-001 | 成本/定价痛点 | r/StableDiffusion, r/FluxAI, r/PromptEngineering, r/artificial | 定价模式问题、ROI 计算、付费意愿 |
| task-002 | 角色/场景一致性 | r/SoraAi, r/generativeAI, r/aitubers, r/n8n | 一致性痛点、现有方案缺陷 |
| task-003 | 生成质量/可控性 | r/SoraAi, r/runwayml, r/KlingAI_Videos | Prompt 问题、质量缺陷 |
| task-004 | 工作流/批量自动化 | r/automation, r/n8n, r/PromptEngineering | 批量处理、多平台适配需求 |
| task-005 | 竞品分析与市场格局 | r/singularity, r/artificial, r/generativeAI | 工具对比、市场机会 |

## 时间过滤器
- 执行日期: 2026-01-20
- 过滤起始日期: 2025-07-25 (180 天前)
- 所有搜索查询必须包含: `after:2025-07-25`

## 下一步
- [x] Phase 0: 侦察完成
- [ ] Phase 1: 创建运行目录结构
- [ ] Phase 2-3: 生成子任务 prompts
- [ ] Phase 4: 并行执行 5 个研究子任务
- [ ] Phase 5-7: 聚合、消化、润色
- [ ] Phase 8: 交付最终报告
