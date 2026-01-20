---
name: researching-reddit-opportunities
description: Discovers Micro-SaaS opportunities and validates product ideas by analyzing Reddit discussions. Generates targeted search queries using 200+ validated patterns, identifies genuine pain points in customer communities (not builder echo chambers), scores opportunities using multi-dimensional frameworks, and applies the "free solution disqualification test." Use when researching product ideas, finding market gaps, validating demand, analyzing competitors, or generating Reddit/Google search queries for product research.
---

# Reddit Product Research

Systematic methodology for discovering Micro-SaaS opportunities through Reddit signal analysis.

## Skill ecosystem integration

This skill is part of a modular research framework:

| Skill | Role | When this skill triggers it |
|-------|------|----------------------------|
| `wide_research/` | Orchestration layer | Wide Research triggers this skill for Reddit-specific research |
| `microsaas_eval/` | Opportunity evaluation | Findings feed into five-dimension scoring |
| `search_router/` | MCP tool routing | Called before executing searches |

### As a standalone skill

Use directly when:
- User explicitly requests Reddit research
- Focus is specifically on Reddit communities
- Generating search queries for manual execution

### As part of Wide Research

When triggered by `wide_research/`:
- Follow Child Output Contract for output format
- Include `## Opportunity Signals` section for Micro-SaaS research
- Ensure citations meet minimum requirements (≥2 links)
- Apply free solution disqualification test

### Output adaptation

| Context | Output format |
|---------|---------------|
| Standalone | Full Research Strategy or Feedback Collection Report |
| Wide Research subtask | Child Output Contract format (see `wide_research/CONTRACT.md`) |

## 🚨 Mandatory gates

This skill has ONE mandatory gate that MUST be executed:

| Gate | Location | Trigger condition |
|------|----------|-------------------|
| **Extraction Gate** | [Comment extraction section](#-extraction-gate-mandatory) | When high-value threads (10+ comments) are identified |

**Gate ensures**: Comments are extracted via JSON API + Python script, not just search snippets.

**If skipped**: Report quality is DEGRADED. Must annotate: `⚠️ 数据质量警告：未执行 Reddit 评论深度抓取`

## Core principle

**Search for verbs, not nouns.** Don't search "CRM" or "email tool"—search for what people are trying to DO ("track leads," "follow up," "schedule meetings"). Action-oriented searches surface authentic problems rather than generic product discussions.

### Verb clustering reference table

Beyond individual verb searches, **cluster by verbs across domains** to find "boring but durable SaaS" opportunities. The same action-verb applied to different domains often reveals similar tool needs.

| Verb cluster | Cross-domain opportunity | Example niches | Query pattern |
|-------------|-------------------------|----------------|---------------|
| **track** | Universal tracking tools | Leads, habits, inventory, time, expenses | `"I track" [domain] "spreadsheet"` |
| **remind** | Reminder/notification systems | Appointments, renewals, deadlines, follow-ups | `"remind me" OR "reminder for" [task]` |
| **visualize** | Dashboards/reporting | Analytics, progress, comparisons, trends | `"visualize" OR "dashboard for" [data type]` |
| **sync** | Integration/glue tools | Multi-platform data, calendars, contacts | `"sync between" [tool1] [tool2]` |
| **convert** | Format transformation | PDF→Excel, video→audio, data migration | `"convert" [format1] "to" [format2]` |
| **batch** | Bulk operation tools | Mass edits, bulk exports, automation | `"batch" OR "bulk" [action]` |
| **export** | Data liberation | Locked platforms, backup, migration | `"export from" [platform]` |
| **automate** | Workflow automation | Repetitive tasks, scheduling, triggers | `"automate" [task] "without code"` |

**Why clustering works**: Users search "how to track leads without forgetting follow-ups," not "CRM alternatives." The verb reveals the job-to-be-done; the noun is just context.

**Discovery workflow**:
1. Pick a verb cluster (e.g., "sync")
2. Search across 3-5 different domains
3. Look for patterns in frustration language
4. The domain with highest pain + payment signals is your target

## Critical filter: Builder echo chamber trap

**Never conduct primary demand research in builder communities.**

Subreddits like r/SaaS, r/Entrepreneur, r/startups, r/microsaas are populated by builders discussing how to sell products, not customers expressing real needs.

| Target market | Research here (customers) | Avoid (builder echo chambers) |
|---------------|---------------------------|-------------------------------|
| PDF tools | r/college, r/LawFirm, r/GradSchool | r/SaaS, r/Entrepreneur |
| Marketing tools | r/marketing, r/SEO, r/PPC | r/startups, r/microsaas |
| Developer tools | r/webdev, r/devops, r/selfhosted | r/SideProject, r/indiehackers |
| Design tools | r/graphic_design, r/UI_Design | r/Entrepreneur |
| E-commerce | r/ecommerce, r/FulfillmentByAmazon | r/startups |

**Exception**: Builder communities ARE valuable for competitive intelligence (what others are building, saturated markets, launch post-mortems). Just don't use them to validate demand.

## Market tier framework

Different market types require different validation standards. **Do not apply mass-consumer thresholds to B2B niches.**

| Market tier | Community size | Post density | Engagement metric | Example communities |
|-------------|---------------|--------------|-------------------|---------------------|
| **Mass consumer** | 50K+ | 15-20+ / 6mo | 50+ upvotes avg | r/productivity, r/apps |
| **Vertical consumer** | 10-50K | 8-15 / 6mo | 20+ upvotes avg | r/GetStudying, r/digitalnomad |
| **B2B professional** | 3-30K | 4-10 / 6mo | 10+ comments avg | r/sysadmin, r/accounting, r/LawFirm |
| **Hyper-niche** | 1-10K | 2-5 / 6mo | 5+ comments avg | r/MSP, r/taxpros, r/restaurateur |

**Critical insight**: For B2B and hyper-niche markets, use **comment count** instead of upvotes as engagement metric. Comments indicate deeper involvement than passive upvoting.

### Why B2B thresholds are lower

B2B professionals:
- Have smaller total populations (5,000 cigar shops vs 50M productivity app users)
- Value time in monetary terms ($50/hr saved = measurable ROI)
- Make purchasing decisions individually or with small teams
- Embed tools into workflows (lower churn)

**Math example**: A subreddit with 3,000 members targeting "independent dental practices":
- 3,000 Reddit users × 20 (Reddit = ~5% of market) = 60,000 potential practices
- 1% conversion = 600 customers × $50/month = $30K MRR potential

**Do not dismiss small communities with high engagement.**

## Opportunity type classification

### Greenfield vs Fix Framework

Before deep research, classify the opportunity type. **This distinction fundamentally changes your validation strategy.**

| Type | Signal patterns | Market implication | Validation focus |
|------|-----------------|-------------------|------------------|
| **Greenfield** | "I wish there was...", "Why is there no...", "Is there anything that..." | New market creation, higher risk/reward | Validate market existence first |
| **Fix** | "I wish [X] had...", "[Product] should...", "[Product] doesn't..." | Existing market validation, proven demand | Must differentiate from incumbent roadmap |

**Classification queries**:
```
# Greenfield detection
site:reddit.com "I wish there was" [category] after:[dynamic-date]
site:reddit.com "why is there no" [category] after:[dynamic-date]

# Fix detection
site:reddit.com "wish [product] had" OR "[product] should" after:[dynamic-date]
site:reddit.com "[product] doesn't" OR "missing in [product]" after:[dynamic-date]
```

**Strategic implications**:

| Type | Primary risk | Mitigation |
|------|-------------|------------|
| Greenfield | Market may not exist | Require 3+ independent complaint sources before proceeding |
| Fix | Incumbent may ship feature | Check product roadmap, target gaps they're unlikely to fill |

**Mixed signals**: Some opportunities are both ("I wish [Product] had X, but honestly I wish there was a simpler tool entirely"). Classify by the **dominant sentiment** in comments.

---

## Workflow modes

Select the appropriate mode based on user's objective:

### Discovery mode
User has vague direction, needs opportunity exploration.

1. Identify target user type and industry vertical
2. Select 3-8 customer communities (see [COMMUNITIES.md](COMMUNITIES.md))
3. Generate queries using high-intent patterns from [PATTERNS.md](PATTERNS.md)
4. Prioritize: churn signals → alternative-seeking → tool recommendations → pain expressions

### Validation mode
User has specific hypothesis, needs confirmation.

1. Generate queries targeting the hypothesized pain point
2. Include "free solution test" queries (check top comments for perfect free solutions)
3. Generate counter-hypothesis queries to challenge assumptions
4. Apply the recurring filter: look for "every time," "always," "constantly"

### Competitive intelligence mode
User wants to understand competitor weaknesses.

1. Generate churn signal queries: "stopped using [product]," "gave up on [product]"
2. Generate switching queries: "alternative to [product]," "replacement for [product]"
3. Generate feature gap queries: "wish [product] had," "[product] doesn't have"
4. Map systematic weaknesses across multiple threads

### Query generation mode
User needs executable search strings.

1. Confirm target platform: Reddit native or Google site search
2. Generate properly formatted queries using correct syntax
3. See [SYNTAX.md](SYNTAX.md) for Reddit/Google search operators

## Search syntax quick reference

**Reddit native** (case-sensitive operators):
```
subreddit:accounting ("alternative to" OR "replacement for") QuickBooks
title:"credits expire" AND (batch OR bulk)
self:true AND selftext:"every time"
```
Time filter: Add `&t=year` to search URL for past year results.

**Google site search**:
```
site:reddit.com "alternative to [product]"
site:reddit.com ([task]) ("every time" OR constantly) tedious
```

For complete syntax guide, see [SYNTAX.md](SYNTAX.md).

## Execution note (MCP tools)

When executing searches via MCP web search providers (Tavily/SerpApi), treat queries as Google site searches:
- Use `site:`/`inurl:`/`intitle:` and encode subreddit constraints in the URL path (e.g., `site:reddit.com inurl:/r/<sub>/comments/ ...`).
- Do not assume Reddit native field filters (`subreddit:`/`author:`/`title:`/`selftext:`/...) are parsed by the provider unless you have explicitly black-box verified it.

## Comment extraction (JSON endpoint)

Use this after identifying promising threads. Preferred path is best-effort full-thread expansion (no OAuth) via `/api/morechildren`, with auditable coverage metrics. Fallback is initial JSON listing only (sample).

For deep technical details (JSON structure, signal patterns, rate limiting), see [EXTRACTION.md](EXTRACTION.md).

### 🚨 Extraction Gate (MANDATORY)

**This gate MUST be executed when high-value Reddit threads are identified.**

#### Gate check sequence

```bash
# 1. Verify extractor exists
EXTRACTOR="tools/reddit_thread_best_effort.py"
if [[ ! -f "$EXTRACTOR" ]]; then
  echo "❌ BLOCKER: Extractor not found at $EXTRACTOR"
  echo "Fallback to Tavily will result in DEGRADED data quality"
fi

# 2. Check cookie file for rate limit bypass
COOKIE_FILE="cookie.txt"
if [[ -f "$COOKIE_FILE" ]]; then
  export REDDIT_COOKIE_FILE="$COOKIE_FILE"
  echo "✅ Cookie file found, rate limits will be bypassed"
else
  echo "⚠️ No cookie file, may hit rate limits on large threads"
fi

# 3. Ready for extraction
echo "Gate passed: Ready to extract comments"
```

#### Execution pattern (MUST follow)

For each identified high-value thread (10+ comments, matches pain hypothesis):

```bash
# Single thread extraction
python3 tools/reddit_thread_best_effort.py "$THREAD_URL" \
  --sort top \
  --limit 500 \
  --depth 10 \
  --max-morechildren-requests 120 \
  --max-seconds 240 \
  --min-score 5 \
  --output-raw "raw_$ID.json" \
  --output-analysis-md "analysis_$ID.md"

# OR batch extraction (preferred for multiple threads)
echo "$THREAD_URL_1" > urls.txt
echo "$THREAD_URL_2" >> urls.txt
./comment_extraction_run.sh -i urls.txt -o runs/current-research
```

#### Gate failure handling

| Scenario | Action | Report annotation |
|----------|--------|-------------------|
| Extractor not found | Use Tavily fallback | `⚠️ 数据质量降级：未使用 JSON API 抓取` |
| Cookie missing + rate limited | Retry with delays | `⚠️ 部分评论未抓取：触发速率限制` |
| Thread blocked (403/451) | Skip thread, log | `❌ 线程被阻止：需要登录` |
| Extraction successful | Continue | `✅ 评论完整抓取 (coverage: X%)` |

**Critical**: If gate is bypassed entirely (no Bash execution attempted), the final report MUST include:
```
⚠️ 数据质量警告：未执行 Reddit 评论深度抓取，引用可能来自搜索摘要而非原始评论
```

#### 🏆 Best Practice Integration

**Practice #2: 降级路径是可接受的**

Extraction Gate produces three outcomes—research can proceed with any of them as long as transparent annotation is included:

| Outcome | Proceed? | Annotation required |
|---------|----------|---------------------|
| ✅ Full pass (`completed` + coverage >80%) | Yes | `✅ 评论完整抓取 (coverage: X%)` |
| ⚠️ Degraded pass (partial extraction) | Yes | `⚠️ 数据质量降级：[specific reason]` |
| ❌ Blocked (`blocked_requires_login_or_oauth`) | **STOP** | Request human intervention (see Practice #4 in `wide_research/FLOW.md`) |

**Practice #3: cookie.txt 是关键依赖**

Before any extraction attempt:

| Check | Frequency | Action if failed |
|-------|-----------|------------------|
| File exists | Every extraction | STOP, request user to create cookie file |
| Freshness (< 7 days) | Every extraction | WARN, suggest refresh if stale |
| Validity | First extraction | Test with small extraction, check `stop_reason` |

See `EXTRACTION.md` → "Cookie Maintenance" for refresh procedure.

### Trigger criteria

- Matches the pain hypothesis
- 10+ comments in the thread
- Title suggests discussion (not only a link share)

### Endpoint conversion

Append `.json` to the post path before any query parameters.

Minimum:
`https://www.reddit.com/r/{sub}/comments/{post_id}.json`

Recommended (best-effort):
`https://www.reddit.com/r/{sub}/comments/{post_id}.json?sort=top&limit=500`

### Extraction steps

**⚠️ MUST execute [Extraction Gate](#-extraction-gate-mandatory) first before proceeding.**

#### Preferred path (best-effort full thread)

1. Execute Gate check sequence (verify extractor + cookie)
2. Run extraction command from [Execution pattern](#execution-pattern-must-follow)
3. Check output metrics:
   - `stop_reason`: Should be `completed`
   - `coverage_estimate`: Should be >80%
   - `remaining_pending_child_ids`: Should be 0 or low
4. If `stop_reason: blocked_requires_login_or_oauth`, ensure `REDDIT_COOKIE_FILE` is set and retry

#### Fallback path (ONLY if preferred path fails)

Use ONLY when Bash execution is impossible (sandbox restrictions, missing Python):

1. Convert the post URL to JSON endpoint (append `.json`)
2. Fetch JSON via Tavily Extract
3. Navigate to `[1].data.children`
4. Collect returned comment nodes as-is
5. **MUST annotate report**: `⚠️ 数据质量降级：未使用 JSON API 抓取`

**Note**: `kind: "more"` nodes are NOT resolved in fallback. Coverage will be incomplete.

### Analysis steps

1. Filter by `score >= 5` (B2B/hyper-niche use `score >= 3`)
2. Scan top comments for free solution indicators
3. Extract workflow descriptions and quantified costs
4. Record comment permalinks and scores

## Automation runner (Codex exec)

Use `comment_extraction_run.sh` to automate per-thread extraction.

Command:
`./comment_extraction_run.sh -i <input_file> [-o <output_dir>] [-m <min_score>] [-s <sort>] [-l <limit>]`

Input file: one Reddit post URL per line. Blank lines and lines starting with `#` are ignored.

Outputs: `runs/<run-id>/prompts/`, `runs/<run-id>/raw/`, `runs/<run-id>/analysis_inputs/`, `runs/<run-id>/child_outputs/`, `runs/<run-id>/logs/`, `runs/<run-id>/aggregated_raw.md`.

## Intent signal hierarchy

**VERY HIGH** (ready to buy):
- Specific product names + action verbs ("switching from," "replacing")
- Urgency language ("need," "help me choose")
- Strong frustration ("fed up," "done with," "can't stand")

**HIGH** (actively researching):
- Feature-focused inquiries with requirements
- Comparison questions with context
- Workaround-seeking behavior

**MEDIUM** (information gathering):
- General comparison questions
- Exploratory without urgency

## Payment intent signal hierarchy

Explicit "I'd pay for X" statements are rare on Reddit. **Hunt for layered signals instead.**

This four-tier hierarchy organizes signals by predictive strength. **Tier 1-2 signals are strong buying indicators; Tier 3-4 provide supporting evidence.**

### Tier 1: Direct payment signals (strongest)

Direct evidence of spending willingness or current expenditure.

| Signal type | Example phrases | Strength | Why valuable |
|-------------|-----------------|----------|--------------|
| **Explicit willingness** | "I'd pay for", "shut up and take my money", "worth paying for" | ★★★★★ | Direct intent (but verify with behavior) |
| **Current spending disclosure** | "I'm paying $X/month for", "subscription costs me", "already paying for Y but hate it" | ★★★★★ | Proven willingness—budget already allocated |
| **Price inquiry** | "pricing?", "cost for team?", "enterprise tier?", "how much does X cost?" | ★★★★★ | Active purchase consideration |
| **Custom development** | "Paid a dev $500 to script this", "hired someone on Upwork for this" | ★★★★★ | Budget exists, no product found |
| **Compliance pressure** | "Auditors require", "HIPAA mandates", "SOC2 compliance needed" | ★★★★★ | Must-solve, not nice-to-have |

**Search patterns**:
```
"I'd pay" OR "worth paying" OR "take my money" [category]
"already paying" OR "currently paying" OR "subscription" [category]
"pricing" OR "cost" OR "how much" [product/category]
"hired developer" OR "paid someone" OR "Upwork" [task]
"compliance" OR "audit" OR "required by" [domain]
```

### Tier 2: Business context signals (strong)

Signals indicating commercial use where ROI justifies purchase.

| Signal type | Example phrases | Strength | Why valuable |
|-------------|-----------------|----------|--------------|
| **Client/business context** | "for my clients", "for my business", "for my agency" | ★★★★ | B2B = higher budgets, faster decisions |
| **ROI quantified** | "saves me X hours", "reduced from Y to Z", "worth the cost because" | ★★★★ | Can calculate value proposition |
| **Scale problem** | "works fine for 10 but breaks at 100", "need to handle 1000+ per month" | ★★★★ | Outgrown free tools, needs paid solution |
| **Team collaboration** | "need to share with team", "multiple users", "team permissions" | ★★★★ | Enterprise features = paid plans |
| **Tool comparison with pricing** | "enterprise version too expensive for us", "X costs $Y but..." | ★★★★ | Price-sensitive but willing buyer |

**Search patterns**:
```
"for my clients" OR "for my business" OR "for my agency" [task]
"saves me" OR "saves hours" OR "saves time" [process]
"at scale" OR "bulk" OR "1000+" OR "enterprise" [task]
"team" AND ("share" OR "collaborate" OR "permissions") [tool category]
"too expensive" AND ("but" OR "still" OR "need") [product]
```

### Tier 3: Professional identity signals (moderate)

Role/identity markers that correlate with purchasing authority and willingness.

| Signal type | Typical roles | Strength | Why valuable |
|-------------|--------------|----------|--------------|
| **High-autonomy roles** | freelancer, consultant, agency owner, content creator (>1k followers) | ★★★ | Self-fund tools, fast decision |
| **B2B decision makers** | marketing manager, product manager, dev lead, ops manager | ★★★ | Budget authority or influence |
| **Decision authority markers** | "I manage", "I'm responsible for", "my team", "I decide what we use" | ★★★ | Can approve purchases |
| **Revenue-tied roles** | sales rep, recruiter, real estate agent, account executive | ★★★ | Tools directly impact income |

**Search patterns**:
```
"as a freelancer" OR "freelancer here" OR "agency owner" [task]
"I manage" OR "my team uses" OR "responsible for" [process]
"in my role as" OR "as a [role]" [pain point]
site:reddit.com/r/freelance OR site:reddit.com/r/agencies [pain keyword]
```

### Tier 4: Pain intensity signals (supporting evidence)

Emotional and behavioral signals that validate problem severity. **Use to corroborate Tier 1-3, not as standalone.**

| Sub-dimension | Strong signals | Weak signals |
|---------------|---------------|--------------|
| **Emotional intensity** | "frustrating", "hate", "drives me crazy", "fed up", "nightmare" | "annoying", "wish", "would be nice" |
| **Time cost quantified** | "spent 3 hours", "wasted my whole weekend", "takes forever every week" | "takes a while", "bit slow" |
| **Frequency indicators** | "every time", "constantly", "always", "daily", "weekly" | "sometimes", "occasionally", "once in a while" |
| **Failed attempts count** | 3+ tools/methods tried and failed | 1 alternative mentioned |

**Scoring guide**:
| Factor | Score 3 | Score 2 | Score 1 |
|--------|---------|---------|---------|
| Emotional | "hate", "nightmare", "fed up" | "frustrating", "annoying" | "wish", "would be nice" |
| Time | ">2 hours" or "every week" | "~1 hour" or "monthly" | "occasionally" |
| Frequency | "every time", "always" | "often", "usually" | "sometimes" |
| Failed attempts | 3+ solutions tried | 2 solutions tried | 1 or none mentioned |

**Aggregate**: ≥9 points → Strong pain; 6-8 → Moderate; <6 → Weak (deprioritize)

**Search patterns**:
```
"frustrating" OR "hate" OR "drives me crazy" [task]
"spend hours" OR "takes forever" OR "wastes time" [task]
"every time" OR "constantly" OR "always" [pain]
"tried X" AND "tried Y" AND ("doesn't work" OR "still") [problem]
```

### Signal tier summary

| Tier | Purpose | Standalone value | Best use |
|------|---------|-----------------|----------|
| **1: Direct payment** | Confirm purchase intent | ✅ High | Validate opportunity viability |
| **2: Business context** | Identify B2B opportunities | ✅ High | Target high-ARPU segments |
| **3: Professional identity** | Filter for decision makers | ⚠️ Medium | Refine target persona |
| **4: Pain intensity** | Corroborate problem severity | ❌ Low alone | Support Tier 1-3 findings |

**Key principle**: Tier 1-2 signals alone can justify pursuing an opportunity. Tier 3-4 signals strengthen the case but are insufficient alone.

### DIY workaround signals (high-value filter)

**When users are "grinding it out" with manual solutions, they're pre-validated buyers.**

| Signal | What it proves | Example phrases |
|--------|---------------|-----------------|
| **Excel/Spreadsheet grinding** | No tool exists or tools are too expensive | "I track it in Excel", "massive spreadsheet", "formula hell" |
| **Script/Code workarounds** | Technical users couldn't find a product | "wrote a Python script", "bash script that", "my hacky solution" |
| **Copy-paste workflows** | Manual process ripe for automation | "copy-paste between", "manually enter", "retype everything" |
| **Multi-tool juggling** | Integration opportunity | "export from X, import to Y", "switch between 3 apps" |
| **Calendar/reminder hacks** | Scheduling/notification gap | "set reminders to", "calendar block for", "sticky note system" |

**Why DIY signals are top-tier:**
1. They've **invested effort** → proves the problem is real
2. Current solution is **painful** → they'll switch
3. They **know the workflow** → can give you requirements
4. No good product exists → **market gap confirmed**

**Search patterns for DIY signals**:
```
"I use Excel" OR "spreadsheet" [task] (tedious OR manual OR "every week")
"wrote a script" OR "Python script" OR "bash script" [task]
"copy paste" OR "copy-paste" OR "manually enter" [workflow]
"export from" AND "import to" [tools]
"hacky" OR "workaround" OR "ugly fix" OR "duct tape" [process]
```

**When you find DIY signals: prioritize this opportunity.** Users grinding through manual workarounds are the easiest to convert.

## The free solution disqualification test

**Before recommending any opportunity, check top comments for perfect free solutions.**

1. Find complaint threads about target pain point
2. Read highest-upvoted comments via JSON extraction
3. Check if any comment provides free, complete solution
4. Check if replies confirm "Thanks, this solved it!"

**If perfect free solution exists and is well-known → DISQUALIFY**

Users will tell prospects about the free solution. You'll face constant "but you can just use [free thing]" objections.

**If free solutions are partial/complex/unreliable → CONDITIONAL OPPORTUNITY**

Value proposition becomes: convenience, reliability, support, ongoing maintenance.

## Opportunity scoring

### Pain intensity classification (filter first)

Classify pain before investing research time. **Only pursue Tier 1.**

| Tier | Name | Signals | Action |
|------|------|---------|--------|
| **1** | **Shark bite** | Already spending money/time; compliance/legal pressure; quantified costs ("$X/month", "Y hours/week") | ✅ Pursue |
| 2 | Mosquito bite | Annoying but "good enough" workarounds exist; complaints without urgency | ⚠️ Higher risk |
| 3 | Paper cut | Easy DIY fix; infrequent occurrence; brief mentions | ❌ Skip |

### Quality over quantity principle

**3 posts with 80+ substantive comments >>> 15 posts with 3 comments each**

Engagement depth indicators:
- Long comments describing specific workflows
- Back-and-forth discussion threads (problem-solving attempts)
- Users mentioning money or time already spent
- Multiple failed solution attempts listed

**Low quantity can be compensated by high quality.** A hyper-niche with 3 detailed complaint threads is more valuable than a mass-market topic with 20 shallow mentions.

### Scoring factors (1-10 each)

| Factor | High score signal |
|--------|-------------------|
| Frequency | Daily/weekly, not one-time |
| Intensity | Strong emotional language, detailed complaints |
| Market size | Multiple subreddits, consistent volume |
| Willingness to pay | Already paying for imperfect solutions (see [Implicit payment signals](#implicit-payment-signals)) |
| Competitive gap | Complaints about all current options |

**Free solution barrier** (bonus factor):
- 10: No free solutions exist
- 7: Free solutions are technical/complex
- 4: Free solutions are unreliable/limited
- 1: Perfect free solution is widely known

## Pain point convergence table

For each candidate opportunity, complete this table:

| Dimension | Question to answer |
|-----------|-------------------|
| User persona | Role/industry/skill level |
| Trigger scenario | When does this happen? (frequency) |
| Task goal | What are they trying to accomplish? |
| Current approach | How do they do it now? |
| Friction point | Where does it break down? |
| Failed attempts | What have they tried? (more = more valuable) |
| Cost | Time/money/risk/compliance pressure |
| Success criteria | How do they know it's solved? |
| Free solution threat | Is there a well-known free fix? |
| Payment motivation | Save time? Reduce errors? Compliance? |

## Vocal minority filter

Online feedback represents extreme opinions. **Only ~3% of dissatisfied users actually voice complaints.**

### Noise vs signal indicators

| Vocal minority (LOW value) | Real demand (HIGH value) |
|---------------------------|-------------------------|
| Same few users complaining repeatedly | Multiple independent sources |
| Vague complaints, quick comments | Detailed workflow descriptions |
| Requests for "free" solutions only | Already paying for partial solutions |
| One-off posts without follow-up | Recurring discussions over 6+ months |
| "That would be cool" responses | "How do I buy this?" questions |

### Behavioral validation principle

> "Anytime we ask 'Would you do X?', that response is garbage." — Teresa Torres

**Past behavior predicts future behavior.** Look for:
- What have they already tried?
- How much time/money are they currently spending?
- What workarounds have they built?

**Do not count**: "Yes I would use that", "Sounds useful", "Great idea"

## Decision framework

### Signal verification checklist (need 4+ of 6)

- [ ] Found in 3+ threads across different communities
- [ ] Users describe multiple failed solutions
- [ ] Evidence of existing spending (time or money)
- [ ] Recurring language present ("every time," "always," "constantly")
- [ ] No perfect free solution in top comments
- [ ] Target users have budget authority (B2B) or strong motivation (B2C)

### Go / No-go thresholds

**After research phase**, evaluate:

| Signal | Go | Pivot |
|--------|-----|-------|
| Landing page signups | 50+ emails | <20 after 2 weeks |
| Pre-pay commitment | 3+ people | 0 |
| Pre-revenue | Any amount | — |
| Pain classification | Tier 1 (Shark bite) | Tier 3 (Paper cut) |

### Exemption clauses

Low-quantity signals are acceptable when:
- Posts have 50+ substantive comments each
- Users quantify costs ("$X/month", "Y hours/week")
- "Hiring developer" posts exist (proves budget)
- Seasonal/cyclical problem (extend time window to 12 months)

## Pattern categories

The complete pattern library is organized by intent type:

- **Pain point patterns**: See [PATTERNS.md#pain-points](PATTERNS.md#pain-points)
- **Tool recommendation patterns**: See [PATTERNS.md#tool-recommendations](PATTERNS.md#tool-recommendations)
- **Switching patterns**: See [PATTERNS.md#switching](PATTERNS.md#switching)
- **Price sensitivity patterns**: See [PATTERNS.md#price-sensitivity](PATTERNS.md#price-sensitivity)
- **Feature gap patterns**: See [PATTERNS.md#feature-gaps](PATTERNS.md#feature-gaps)
- **UI/UX friction patterns**: See [PATTERNS.md#ui-ux-friction](PATTERNS.md#ui-ux-friction)
- **Integration patterns**: See [PATTERNS.md#integrations](PATTERNS.md#integrations)
- **Automation patterns**: See [PATTERNS.md#automation](PATTERNS.md#automation)
- **Churn patterns**: See [PATTERNS.md#churn](PATTERNS.md#churn)
- **AI fatigue patterns**: See [PATTERNS.md#ai-fatigue](PATTERNS.md#ai-fatigue)

## Constraint amplifiers

Add these terms to any pattern to surface higher-value opportunities (harder constraints = stronger payment motivation):

**Scale constraints**: "bulk," "batch," "at scale," "10,000 files," "enterprise"
**Compliance constraints**: "GDPR," "HIPAA," "SOC2," "audit trail"
**Privacy constraints**: "offline," "self-hosted," "on-prem," "no upload"
**Quality constraints**: "accurate," "no hallucinations," "deterministic"
**Integration constraints**: "webhook," "two-way sync," "API," "SLA"

## Keyword combination formula

Transform generic patterns into domain-specific queries using this formula:

```
[Object noun] + [Task verb] + [Constraint] + [Pain outcome]
```

### Building blocks

Extract these from Reddit discussions in your target community:

**Object nouns** (what they work with):
`invoice, lead, listing, patient form, timesheet, contract, report, order, ticket, subscription, campaign, asset, document, booking, inventory...`

**Task verbs** (what they're trying to do):
`export, reconcile, batch, schedule, approve, transcribe, sync, migrate, merge, validate, automate, generate, track, archive, deduplicate...`

**Constraints** (what makes it hard):
`multi-account, HIPAA, rate limit, team permissions, audit log, offline, bulk, real-time, cross-platform, legacy system, API-only, enterprise...`

**Pain outcomes** (what goes wrong):
`errors, manual work, hours wasted, rejected, lost data, compliance fail, duplicates, out of sync, timeout, broken, inconsistent...`

### Combination examples

| Domain | Object + Verb + Constraint + Pain | Resulting query |
|--------|-----------------------------------|-----------------|
| Accounting | invoice + reconcile + multi-currency + errors | `"invoice reconcile" "multi currency" (errors OR manual)` |
| Sales | lead + export + API limit + manual | `"export leads" "API" (limit OR manual OR "rate limit")` |
| HR | timesheet + approve + audit trail + compliance | `"timesheet approval" "audit" (compliance OR "audit trail")` |
| E-commerce | inventory + sync + multi-channel + out of sync | `"inventory sync" (multichannel OR "multiple platforms") "out of sync"` |
| Healthcare | patient form + digitize + HIPAA + manual | `"patient forms" (digitize OR scan) "HIPAA" manual` |

### Why this formula works

1. **Object + Verb** = The actual task (what they're trying to DO)
2. **Constraint** = Why generic solutions don't work (your differentiation)
3. **Pain outcome** = Proof they're struggling (validation signal)

**This formula helps you create queries for ANY niche, not just use pre-built patterns.**

### Quick extraction method

When reading a pain thread, extract:
1. **Nouns**: What things are they mentioning? (invoices, leads, tickets...)
2. **Verbs**: What are they trying to do? (export, sync, approve...)
3. **Blockers**: What's stopping them? (permissions, limits, compliance...)
4. **Consequences**: What bad thing happens? (errors, hours wasted, fines...)

Then combine into search queries for that specific niche.

## Output formats

The skill produces two primary outputs depending on the workflow stage, plus optional per-thread comment analysis blocks.

### Output A: Research Strategy (pre-execution)

When generating search queries before execution:

```markdown
## Research Strategy: [Objective]

### Target communities
[List 3-8 customer communities with rationale]

### Query set
**High-intent (execute first)**
1. `[query]` — Expected insight: [type]

**Pain discovery (execute second)**
1. `[query]` — Expected insight: [type]

### Validation checklist
- [ ] Found in 3+ threads across different communities
- [ ] Users describe multiple failed solutions
- [ ] Evidence of existing spending on the problem
- [ ] Recurring language present ("every time," "always")
- [ ] No perfect free solution in top comments
```

---

### Output B: Feedback Collection Report (post-execution)

After executing searches and collecting user feedback, compile findings into this structure:

```markdown
## Feedback Collection Report: [Research Objective]

### Collection metadata
| Parameter | Value |
|-----------|-------|
| Research objective | [objective] |
| Date collected | [YYYY-MM-DD] |
| Time range | [e.g., past 180 days] |
| Communities searched | [comma-separated list] |
| Total threads analyzed | [number] |
| Total quotes collected | [number] |

---

### Executive summary

[2-3 paragraphs synthesizing key findings]

**Top pain points identified** (ranked by frequency × intensity):
1. [Pain point 1] — [frequency] mentions, [intensity] emotional language
2. [Pain point 2] — ...
3. [Pain point 3] — ...

**Free solution risk assessment**: [PASS / CONDITIONAL / FAIL with brief reason]

**Overall opportunity score**: [X/50] (see scoring dimensions below)

---

### Pain point themes

#### Theme 1: [Pain Point Name]

**Signal strength**
| Dimension | Score | Evidence |
|-----------|-------|----------|
| Frequency | [1-10] | Found in X threads across Y communities |
| Intensity | [1-10] | [emotional language examples] |
| Willingness to pay | [1-10] | [existing spending evidence] |
| Competitive gap | [1-10] | [complaints about current options] |
| Free solution barrier | [1-10] | [PASS/CONDITIONAL/FAIL] |
| **Total** | [X/50] | |

**Representative quotes**

> "[Exact quote preserving original language and typos]"
> — r/[subreddit], [YYYY-MM-DD], ↑[upvotes]
> 🔗 [full URL to thread or comment]
> **Signal type**: [pain-expression | switching | churn | feature-gap | price-sensitivity | ux-friction | automation-desire | tool-seeking | integration-need | ai-fatigue]

> "[Another quote]"
> — r/[subreddit], [YYYY-MM-DD], ↑[upvotes]
> 🔗 [URL]
> **Signal type**: [type]

**Context analysis**: [1-2 sentences on why this pain matters, user persona, trigger scenario]

---

#### Theme 2: [Pain Point Name]
[Same structure as Theme 1]

---

### Disqualified opportunities

[Pain points that failed the free solution test]

| Pain point | Reason for disqualification | Free solution mentioned |
|------------|----------------------------|------------------------|
| [name] | [reason] | [e.g., "Top comment: just use Excel macro"] |

---

### Validation checklist (completed)

- [x] Found in 3+ threads across different communities
- [x] Users describe multiple failed solutions
- [ ] Evidence of existing spending on the problem ← [note if not found]
- [x] Recurring language present ("every time," "always")
- [x] No perfect free solution in top comments

---

### Raw evidence index

[Optional: Complete list of all analyzed threads for audit trail]

| # | Thread title | Community | Date | Upvotes | URL |
|---|--------------|-----------|------|---------|-----|
| 1 | [title] | r/[sub] | [date] | ↑[n] | [url] |
| 2 | ... | ... | ... | ... | ... |
```

#### Signal type reference

Map collected quotes to these signal categories (derived from [PATTERNS.md](PATTERNS.md)):

| Signal type | Indicates | Example patterns |
|-------------|-----------|------------------|
| `pain-expression` | Active frustration | "struggling with," "frustrated," "hate when" |
| `switching` | Ready to change products | "alternative to," "replacement for," "done with" |
| `churn` | Recently left a product | "stopped using," "cancelled," "gave up on" |
| `feature-gap` | Missing functionality | "wish X had," "doesn't have," "missing feature" |
| `price-sensitivity` | Cost is deciding factor | "too expensive," "cheaper alternative," "free option" |
| `ux-friction` | Interface/usability issues | "confusing," "clunky," "outdated UI" |
| `automation-desire` | Manual work pain | "tedious," "takes hours," "repetitive" |
| `tool-seeking` | Actively shopping | "best app for," "recommend a tool," "looking for" |
| `integration-need` | Workflow connectivity | "sync between," "connect X to Y," "API" |
| `ai-fatigue` | AI-specific concerns | "hallucinated," "can't trust AI," "no AI" |

#### Quote formatting rules

1. **Preserve original text**: Keep typos, grammar, and formatting exactly as written
2. **Include context**: If the quote needs context, add [brackets] for editorial notes
3. **Link to source**: Always include full URL (thread or specific comment permalink)
4. **Metadata required**: subreddit, date, upvotes (↑ symbol for visual scanning)
5. **One signal type per quote**: Choose the primary intent signal

---

### Output C: Comment Analysis (per thread, optional)

Use this block when a thread meets the comment extraction trigger criteria.

```markdown
### Comment Analysis: [Post Title]

**Post URL**: [link]
**Returned comments**: [N in initial listing]
**Analyzed**: [top N by score after filtering]

#### Free solution check
- [ ] No free solution found in top comments
- [ ] Free solution found: [describe]

#### Key pain signals
| Comment | Score | Signal | Link |
|---------|-------|--------|------|
| "[quote]" | 42 | Quantified cost | [comment link] |
| "[quote]" | 28 | Failed alternatives | [comment link] |

#### Workflow descriptions
> "[verbatim quote describing current process]"
> — u/username (score: X)
> 🔗 [comment permalink]
```

## Research trap warnings

**Critical pitfalls that can invalidate your research. Review before finalizing any opportunity assessment.**

### ⚠️ Trap 1: Sample bias

**Problem**: Reddit users don't represent the entire market.

| Bias dimension | Reddit skew | Implication |
|---------------|-------------|-------------|
| Technical literacy | Higher than average | Non-technical users may not be on Reddit |
| Age distribution | 25-45 years dominant | Older/younger demographics underrepresented |
| Solution preference | "Open source first" mindset | May overstate free solution acceptance |
| Geographic | US/English-speaking heavy | International markets underrepresented |

**Mitigation strategies**:
- Cross-validate on other platforms (Twitter/X, Quora, industry forums, Facebook groups)
- Prioritize B2B/professional communities over consumer communities
- Weight explicit "willing to pay" signals higher than general complaints
- For non-US markets, verify if Reddit is even used in that region

**Self-check**: Ask "Would my target users actually use Reddit to discuss this?"

### ⚠️ Trap 2: High upvotes ≠ Payment willingness

**Problem**: Upvotes measure resonance, not purchase intent.

| Signal type | Upvotes | Payment likelihood | Example |
|------------|---------|-------------------|---------|
| "Wouldn't it be cool if..." | ↑500+ | 🔴 Low | Nice-to-have fantasy |
| "I hate how X works" | ↑200 | 🟡 Medium | Complaint but may tolerate |
| "I've tried X, Y, Z but none work for [critical task]" | ↑50 | 🟢 High | Must-have with failed attempts |
| "I'm paying $X but still have this problem" | ↑20 | 🟢🟢 Very High | Proven buyer, unmet need |

**Judgment criteria**:
1. Does the post describe a **specific work scenario** (not hypothetical)?
2. Do comments mention **already paying** or **willing to pay**?
3. Does the problem **impact revenue or critical tasks**?
4. Are there **quantified costs** (hours/money)?

**Red flag phrases** (deprioritize):
- "Wouldn't it be cool if..."
- "Someone should build..."
- "I wish there was..." (without urgency)
- "That would be nice..."

**Green flag phrases** (prioritize):
- "I've tried everything..."
- "I'm paying $X but still..."
- "This is costing me hours every week..."
- "I need to solve this because [business reason]..."

### ⚠️ Trap 3: Overestimating execution capability

**Problem**: Finding a good opportunity ≠ Being able to build and ship it.

**Pre-commitment checklist** (complete before deep investment):

| Dimension | Question | Red flag threshold |
|-----------|----------|-------------------|
| **Technical complexity** | Can I/my team build MVP in 4 weeks? | Requires ML training, real-time infra, or unfamiliar stack |
| **Operational burden** | Does it need manual operations or support? | 24/7 support, content moderation, manual review loops |
| **Content/data dependency** | Does value require large datasets or content? | Needs curated database, training data, or content library |
| **Compliance overhead** | Are there regulatory requirements? | HIPAA, SOC2, PCI, GDPR-heavy with audit requirements |
| **Network effects** | Does product need many users to be valuable? | Marketplace, social network, or collaboration tool |
| **Sales cycle** | Can users self-serve or need sales? | Enterprise-only, requires demos and contracts |

**Scoring**: Count red flags. 0-1 = Go. 2-3 = Proceed with caution. 4+ = Reconsider or find co-founder.

### ⚠️ Trap 4: Confirmation bias in research

**Problem**: Once you have a hypothesis, you'll see evidence everywhere.

**Counter-measures**:
1. **Actively search for disconfirming evidence**: Use queries like "[product idea] sucks" or "why [solution] failed"
2. **Set a kill threshold before starting**: "If I find <X signals in Y communities, I'll abandon this"
3. **Assign devil's advocate role**: Spend 20% of research time trying to disprove your hypothesis
4. **Check competitor graveyard**: Search "[category] startup failed" or Product Hunt for dead projects

**Red flag behaviors** (you're falling for this trap):
- Skipping threads that don't support your hypothesis
- Interpreting neutral comments as positive signals
- Ignoring existing solutions because "they're not good enough"
- Rationalizing away free solution mentions

### ⚠️ Trap 5: Developer Paradox

**Problem**: Developer communities produce the longest, most detailed complaint posts—but often have the lowest payment willingness.

| Community type | Post detail level | Payment willingness | Why |
|---------------|-------------------|---------------------|-----|
| **Developer** (r/webdev, r/selfhosted, r/programming) | ★★★★★ | ★☆☆☆☆ | Can build own solution, "DIY" culture, open-source preference |
| **Finance** (r/personalfinance, r/shopify) | ★★☆☆☆ | ★★★★★ | Time = money, proven buyers |
| **Business** (r/smallbusiness, r/accounting) | ★★★☆☆ | ★★★★☆ | Tool cost = business expense |
| **Prosumer** (r/freelance, r/agencies) | ★★★☆☆ | ★★★★☆ | Billable to clients |

**Why this happens**:
- Developers can (and often prefer to) build their own solutions
- Strong "open source first" and "DIY" culture
- Time cost often undervalued vs. learning opportunity
- "I could build that in a weekend" syndrome

**Mitigation strategies**:
1. For developer-focused opportunities, **require Tier 1 payment signals** (not just detailed complaints)
2. Weight "I paid someone on Upwork to script this" signals **3x higher** in dev communities
3. Cross-validate with non-developer communities using the same tool category
4. Look for enterprise/team context: "my company needs" > "I want"

**Exception**: Developer tooling that saves significant time on non-core tasks (CI/CD, monitoring, deployment) can still succeed if positioned correctly.

**Quantitative check**: Use WPI calculation from [METRICS.md](METRICS.md). Developer opportunities should have WPI > 4 to proceed (vs. WPI > 2 for general productivity).

### Quick trap checklist

Before finalizing any opportunity assessment, verify:

- [ ] **Sample bias**: Validated on at least one non-Reddit source
- [ ] **Upvote trap**: Have Tier 1-2 payment signals, not just high engagement
- [ ] **Execution reality**: Passed pre-commitment checklist (≤1 red flag)
- [ ] **Confirmation bias**: Spent time searching for disconfirming evidence

**If any check fails**: Document the gap and either address it or deprioritize the opportunity.

## Key reminders

1. **Comment sections often contain richer data than original posts**
2. **Recurring patterns matter more than viral posts**
3. **Action-oriented language predicts buying intent** ("I need" > "I wish")
4. Always verify across multiple communities before concluding
