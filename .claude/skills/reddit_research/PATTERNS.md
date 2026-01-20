# Search Pattern Library

Complete collection of Reddit search patterns organized by intent type and buying signal strength.

## Contents

- [Pain points](#pain-points)
- [Tool recommendations](#tool-recommendations)
- [Switching](#switching)
- [Price sensitivity](#price-sensitivity)
- [Feature gaps](#feature-gaps)
- [UI/UX friction](#ui-ux-friction)
- [Integrations](#integrations)
- [Automation](#automation)
- [Churn](#churn)
- [AI fatigue](#ai-fatigue)
- [Niche vocabulary](#niche-vocabulary)

---

## Search strategy guide

**Don't know which patterns to use? Start here.** This decision tree maps your research intent to the right pattern combinations.

### Scenario 1: "I want to discover what pain points exist in this domain"

**Goal**: Open exploration, no hypothesis yet

**Recommended strategy**: Pain discovery + DIY workaround signals

| Pattern category | Priority | Why |
|-----------------|----------|-----|
| [Pain points](#pain-points) | ★★★★★ | Core frustration expressions |
| [Automation](#automation) | ★★★★☆ | Manual labor = automation opportunity |
| DIY workaround patterns | ★★★★☆ | See SKILL.md §DIY workaround signals |

**Search template**:
```
site:reddit.com/r/[community] ("struggling with" OR "frustrated" OR "hate") [domain keyword]
site:reddit.com/r/[community] ("every time" OR "constantly") [task keyword]
site:reddit.com/r/[community] "I use Excel" OR "spreadsheet" [task keyword]
```

**Time filter**: Past 6 months (`after:YYYY-MM-DD`)

**Success criteria**: Found 3+ distinct pain themes with emotional language

---

## Iterative search term expansion

Systematic approach using ~20 related search terms, taking top 5 results from each, then deduplicating. This methodology was validated on 9,300+ "I wish there was an app" posts.

### Standard 20-term query set template

For any research objective, generate queries in these five categories:

| Category | # | Pattern type | Example for "invoice automation" |
|----------|---|--------------|----------------------------------|
| Tool seeking | 1-4 | "is there a tool for [X]" variations | "is there a tool for invoice tracking" |
| App request | 5-8 | "I need an app for [X]" variations | "I need an app for invoice management" |
| Frustration | 9-12 | "[X] is so frustrating" variations | "invoicing is so tedious", "hate manual invoicing" |
| Workflow | 13-16 | "how do you handle [X]" variations | "how do you handle client invoices" |
| Recommendations | 17-20 | "best [X] tool" / "recommend [X] app" | "best invoice tool for freelancers" |

### Seed term expansion method

Start with a core term, then expand systematically:

| Expansion level | Type | Example (invoice pain) |
|----------------|------|------------------------|
| **Seed** | Core term | "invoice" |
| **Synonyms** | Alternative words | "billing", "payment request", "AP/AR" |
| **Actions** | What they do | "send invoice", "chase payment", "track invoice" |
| **Pain verbs** | Frustration | "hate invoicing", "invoice nightmare" |
| **Tool search** | Active shopping | "invoice tool for", "best invoicing app" |
| **Alternative** | Switching intent | "alternative to [competitor]" |

### Deduplication protocol

After collecting results from all 20 queries:

1. **Extract** all unique thread URLs
2. **Cluster** by post ID (same thread from different searches = 1 entry)
3. **Prioritize** by: comment count → upvotes → recency
4. **Cap** at 50-100 threads for manual review

### Execution tips

- Run 4-5 queries in parallel via MCP tools
- Use 6-month time filter (`after:YYYY-MM-DD`) for freshness
- Save raw results before deduplication for audit trail
- Track which query types yield highest-quality results for future optimization

---

### Scenario 2: "I want to validate if this specific pain point is worth building for"

**Goal**: Hypothesis validation with payment signal focus

**Recommended strategy**: Payment intent + Switching signals

| Pattern category | Priority | Why |
|-----------------|----------|-----|
| [Price sensitivity](#price-sensitivity) | ★★★★★ | Direct payment willingness indicators |
| [Switching](#switching) | ★★★★★ | Already paying, ready to change |
| [Churn](#churn) | ★★★★☆ | Left a product = proven buyer |

**Search template**:
```
site:reddit.com "[product category]" ("worth paying" OR "I'd pay for" OR "pricing")
site:reddit.com "alternative to [competitor]" OR "replacement for [competitor]"
site:reddit.com "stopped using [competitor]" OR "cancelled [competitor]"
```

**Validation checkpoints**:
1. Found explicit payment willingness expressions?
2. Users quantify current spending or time cost?
3. Multiple failed alternatives mentioned?

**Success criteria**: Found Tier 1-2 payment signals (see SKILL.md Payment Intent Hierarchy)

### Scenario 3: "I want to find weaknesses of existing competitors"

**Goal**: Competitive intelligence for differentiation

**Recommended strategy**: Feature gaps + Churn + UX friction

| Pattern category | Priority | Why |
|-----------------|----------|-----|
| [Feature gaps](#feature-gaps) | ★★★★★ | Missing functionality = your opportunity |
| [Churn](#churn) | ★★★★★ | Why people leave = your positioning |
| [UI/UX friction](#ui-ux-friction) | ★★★★☆ | Usability complaints = differentiation angle |

**Search template**:
```
site:reddit.com "[competitor name] but" OR "[competitor] doesn't have"
site:reddit.com "wish [competitor] had" OR "[competitor] missing"
site:reddit.com "gave up on [competitor]" OR "stopped using [competitor]"
site:reddit.com "[competitor]" ("confusing" OR "clunky" OR "frustrating UI")
```

**Analysis framework**:
| Weakness type | Differentiation angle |
|--------------|----------------------|
| Missing feature | Build that specific feature |
| Pricing complaint | Offer simpler/cheaper tier |
| Complexity | Simplify for specific use case |
| Integration gap | Build the connector |

**Success criteria**: Identified 2-3 systematic weaknesses with multiple user reports

### Scenario 4: "I want to understand how users currently solve this problem"

**Goal**: Workflow mapping for solution design

**Recommended strategy**: Tool recommendations + DIY signals + Integration needs

| Pattern category | Priority | Why |
|-----------------|----------|-----|
| [Tool recommendations](#tool-recommendations) | ★★★★★ | What they're already using |
| DIY workaround patterns | ★★★★★ | Manual solutions = automation opportunity |
| [Integrations](#integrations) | ★★★★☆ | Multi-tool workflows = connector opportunity |

**Search template**:
```
site:reddit.com/r/[community] "what do you use for" [task]
site:reddit.com/r/[community] "how do you handle" OR "how do you manage" [task]
site:reddit.com/r/[community] "I use Excel" OR "Google Sheets" [task]
site:reddit.com/r/[community] "export from" AND "import to" [workflow]
```

**Extraction focus**:
- Current tool stack (what's already paying for?)
- Manual steps in workflow (automation targets)
- Pain points with current approach
- Wishlist features

**Success criteria**: Can draw a workflow diagram from user descriptions

### Strategy selection matrix

| Your question | Use scenario | Primary patterns |
|--------------|--------------|------------------|
| "What problems exist here?" | Scenario 1 | Pain points, Automation |
| "Is this worth building?" | Scenario 2 | Price sensitivity, Switching |
| "How can I differentiate?" | Scenario 3 | Feature gaps, Churn, UX |
| "What do users do today?" | Scenario 4 | Tool recommendations, DIY |

### Combining strategies

**Full validation flow** (for serious opportunities):

1. **Week 1**: Scenario 1 → Discover pain landscape
2. **Week 2**: Scenario 4 → Map current solutions
3. **Week 3**: Scenario 2 → Validate payment willingness
4. **Week 4**: Scenario 3 → Identify differentiation angle

**Quick validation** (for initial filtering):

1. Run Scenario 2 patterns first
2. If no Tier 1-2 payment signals → Deprioritize
3. If signals found → Expand to Scenario 1 and 3

---

## Pain points

### Core frustration expressions

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "struggling with [X]" | HIGH | Active pain point |
| "how to fix [X]" | MEDIUM-HIGH | Problem resolution (filter needed) |
| "looking for a way to [X]" | HIGH | Solution-seeking |
| "is there anything out there that [X]" | VERY HIGH | Active product search |
| "I wish there was [X]" | VERY HIGH | Unmet need |
| "why is there no [X]" | VERY HIGH | Market gap signal |
| "the problem with [X]" | HIGH | Specific criticism |
| "this should be easier" | HIGH | UX friction |
| "why is it so hard to [X]" | VERY HIGH | Process pain point |
| "terrible experience with [X]" | HIGH | Strong dissatisfaction |
| "is there a better way to [X]" | VERY HIGH | Improvement seeking |
| "I'm frustrated with [X]" | HIGH | Emotional pain |
| "my biggest frustration is [X]" | VERY HIGH | Priority pain |
| "I hate it when [X]" | HIGH | Recurring irritation |

### High-value compound patterns

Combine for stronger signals:

| Compound pattern | Why better |
|------------------|------------|
| "how to fix [X]" + "every time" | Proves recurring problem |
| "how to fix [X]" + "tedious" | Manual labor pain |
| "how to fix [X]" + "manually" | Automation opportunity |
| "how to fix [X]" + "takes hours" | Time-sink identification |
| "struggling with [X]" + "workflow" | Process-level friction |
| "[task]" + "repetitive" | Automation candidate |

### The "every time" test

If users describe doing something repeatedly, it's likely a real SaaS opportunity. One-time questions rarely justify products.

Key indicators: "every time," "always," "constantly," "repeatedly," "again and again"

---

## Tool recommendations

### Direct request patterns (highest intent)

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "best app for [X]" | VERY HIGH | Active purchasing |
| "is there a tool that [X]" | VERY HIGH | Feature-specific search |
| "anyone know of a tool for [X]" | VERY HIGH | Community recommendation |
| "looking for a tool to [X]" | VERY HIGH | Direct product search |
| "what do you use for [X]" | HIGH | Community wisdom |
| "recommendations for [X]" | VERY HIGH | Open to suggestions |
| "what [category] do you recommend" | VERY HIGH | Trust-seeking |
| "suggest a [category]" | VERY HIGH | Ready for options |
| "need a [category] that can [X]" | VERY HIGH | Specific requirement |

### Validation-seeking patterns

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "is [product] worth it" | HIGH | Pre-purchase validation |
| "has anyone tried [product]" | HIGH | Experience seeking |
| "anyone using [product] for [use case]" | HIGH | Use-case validation |
| "thoughts on [product]" | MEDIUM-HIGH | Opinion gathering |
| "[product] reviews reddit" | HIGH | Social proof seeking |

---

## Switching

### High-intent switching phrases

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "alternative to [product]" | VERY HIGH | Active solution-seeking |
| "replacement for [product]" | VERY HIGH | Ready to purchase |
| "switching from [product]" | VERY HIGH | In transition |
| "moving away from [product]" | VERY HIGH | Decision made |
| "ditching [product]" | VERY HIGH | Frustrated, ready to switch |
| "leaving [product]" | VERY HIGH | Emotional decision |
| "migrating from [product]" | HIGH | Planned technical move |
| "done with [product]" | VERY HIGH | Frustration threshold reached |
| "what should I use instead of [product]" | VERY HIGH | Open to recommendations |

### Comparison patterns

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "similar to [product]" | MEDIUM | Exploring options |
| "like [product] but [different]" | HIGH | Feature-gap identification |
| "anything like [product]" | MEDIUM | Early research |
| "equivalent to [product]" | MEDIUM | Wants feature parity |
| "competitors to [product]" | MEDIUM | Market research |
| "options besides [product]" | HIGH | Comparison shopping |

### Frustration-driven switching

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "fed up with [product]" | VERY HIGH | Strong frustration |
| "sick of [product]" | VERY HIGH | Emotional trigger |
| "can't stand [product] anymore" | VERY HIGH | Breaking point |
| "[product] is getting worse" | HIGH | Declining satisfaction |
| "finally giving up on [product]" | VERY HIGH | Decision finalized |

---

## Price sensitivity

### Free/no-cost seeking

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "free alternative to [product]" | HIGH | Budget-constrained |
| "open source alternative to [product]" | HIGH | Values ownership + free |
| "FOSS alternative" | HIGH | Technical, privacy-conscious |
| "self-hosted alternative to [product]" | HIGH | Control + cost focus |
| "any free options for [X]" | HIGH | Solution-first search |

### Cost comparison

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "cheaper than [product]" | VERY HIGH | Price is deciding factor |
| "more affordable than [product]" | HIGH | Price-sensitive |
| "budget [category]" | HIGH | Price-first search |
| "best value [category]" | HIGH | ROI-focused |
| "[product] too expensive" | HIGH | Price objection |

### Subscription aversion (growing trend)

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "one-time purchase [category]" | VERY HIGH | Subscription fatigue |
| "no subscription [category]" | VERY HIGH | Payment model critical |
| "lifetime license [category]" | VERY HIGH | Long-term ownership |
| "buy once [category]" | VERY HIGH | Anti-recurring cost |
| "perpetual license" | HIGH | Professional buyer |
| "tired of paying monthly for [product]" | VERY HIGH | Subscription fatigue |

### Billing model pain (often overlooked)

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "pay per use alternative to [product]" | VERY HIGH | Usage-based preference |
| "credits expire" | VERY HIGH | Credit system frustration |
| "unused credits" | HIGH | Waste perception |
| "metered billing for [category]" | HIGH | Consumption-based preference |
| "only pay for what I use" | VERY HIGH | Value alignment |
| "minimum spend" | HIGH | Threshold frustration |
| "forced to upgrade" | VERY HIGH | Tier friction |
| "plan limits" | HIGH | Constraint frustration |

---

## Feature gaps

### Direct feature requests

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "wish [product] had [feature]" | MEDIUM-HIGH | Identified gap |
| "does anyone know if [product] can [X]" | HIGH | Feature discovery |
| "feature request for [product]" | MEDIUM | Formal feedback |
| "missing feature in [product]" | HIGH | Gap identification |
| "[product] doesn't have [X]" | HIGH | Limitation discovery |
| "why doesn't [product] [X]" | HIGH | Frustration with gap |
| "can [product] do [X]" | HIGH | Capability question |
| "is there a way to [X] in [product]" | HIGH | Workaround seeking |

### Must-have requirements (most valuable)

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "workaround for [limitation]" | HIGH | Feature gap compensation |
| "looking for [category] that can [X]" | VERY HIGH | Active shopping |
| "feature I need is [X]" | VERY HIGH | Deal-breaker identification |
| "deal-breaker" | VERY HIGH | Critical requirement |
| "must-have [feature]" | VERY HIGH | Essential feature |
| "would pay for [feature]" | VERY HIGH | Willingness to convert |
| "basic feature" | HIGH | Expected functionality |
| "surprised [product] doesn't [X]" | HIGH | Expectation mismatch |

---

## UI/UX friction

### Visual design complaints

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "looks like Windows 95" | HIGH | Modernization opportunity |
| "outdated UI" | HIGH | Design refresh opportunity |
| "ugly interface" | HIGH | Aesthetic pain |
| "dated design" | HIGH | Modern alternative opportunity |
| "clunky interface" | HIGH | UX friction |
| "looks unprofessional" | HIGH | B2B positioning opportunity |
| "needs a redesign" | MEDIUM-HIGH | Acknowledged weakness |
| "UI hasn't changed in years" | HIGH | Stagnant competitor |

### Usability complaints

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "confusing interface" | HIGH | Simplicity opportunity |
| "hard to navigate" | HIGH | Information architecture issue |
| "too many clicks to [action]" | HIGH | Workflow friction |
| "buried in menus" | HIGH | Discoverability issue |
| "not intuitive" | HIGH | Learning curve pain |
| "steep learning curve" | HIGH | Onboarding opportunity |
| "overwhelming UI" | HIGH | Simplicity opportunity |
| "feature bloat" | HIGH | Focused alternative opportunity |

---

## Integrations

### The Glue Strategy

**Key insight from 696 Business Tools requests: Users don't want new platforms—they want glue between existing tools.**

The dominant pattern in business tool requests is middleware/integration, not new platforms. Users have already chosen their stack (Shopify, NetSuite, Google Drive) and want simple, niche integrations to make those tools talk to each other without expensive custom development.

| Glue signal | Pattern | Opportunity type | Value proposition |
|-------------|---------|-----------------|-------------------|
| **Platform bridge** | "connect [X] to [Y]", "sync [X] with [Y]" | Two-way sync tool | Eliminate manual data transfer |
| **Export frustration** | "export from [X]", "get data out of [X]" | Data liberation tool | Escape vendor lock-in |
| **Multi-tool juggling** | "I use [X] for A, [Y] for B, manually copy" | Unified workflow | Single pane of glass |
| **Zapier fatigue** | "Zapier too expensive", "Zapier keeps breaking" | Native integration | Reliability + cost savings |

**Why glue wins for Micro-SaaS**:
- **Low switching cost** — Users keep existing stack, just add connector
- **Clear value proposition** — Time saved on manual work is measurable
- **Recurring revenue justified** — Ongoing sync value supports subscription
- **Smaller scope** — 2-4 week MVP vs. months for full platform

**Glue opportunity search patterns**:
```
site:reddit.com "[platform1]" "[platform2]" ("sync" OR "connect" OR "integrate")
site:reddit.com "export from [platform]" "import to"
site:reddit.com "Zapier" ("expensive" OR "breaking" OR "alternative" OR "too many steps")
site:reddit.com "[platform]" "and" "[platform]" "workflow" ("manual" OR "tedious")
```

---

### Core integration patterns

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "integrate with [tool]" | HIGH | Active tool evaluation |
| "workflow for [process]" | HIGH | Specific process need |
| "connect [X] to [Y]" | VERY HIGH | Clear tool pairing |
| "sync between [X] and [Y]" | HIGH | Data continuity need |
| "compatible with [tool]" | HIGH | Ecosystem evaluation |
| "does [X] have an API" | HIGH | Technical integration |
| "native integration with [tool]" | HIGH | Quality preference |
| "Zapier alternative for [use case]" | VERY HIGH | Specific solution search |
| "webhook support for [tool]" | HIGH | Developer-level need |
| "two-way sync between [X] and [Y]" | VERY HIGH | Sophisticated requirement |

### Data portability pain

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "export data from [closed platform]" | VERY HIGH | Data liberation |
| "get my data out of [product]" | VERY HIGH | Portability frustration |
| "locked into [product]" | HIGH | Vendor lock-in concern |
| "can't export from [product]" | VERY HIGH | Data hostage |
| "migrate data from [X] to [Y]" | HIGH | Migration tooling |

### Zapier fatigue (high-value opportunity area)

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "sync [X] to [Y] without Zapier" | VERY HIGH | Native integration preference |
| "Zapier too expensive" | VERY HIGH | Cost-driven alternative search |
| "Zapier alternative" | VERY HIGH | Platform frustration |
| "direct integration between [X] and [Y]" | HIGH | Quality preference |
| "native sync" | HIGH | Reliability preference |
| "Zapier keeps breaking" | VERY HIGH | Reliability concern |
| "too many Zapier steps" | HIGH | Complexity frustration |

---

## Automation

### Automation desire patterns

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "automate [process]" | VERY HIGH | Clear automation need |
| "automatically [action]" | HIGH | Process optimization |
| "streamline [workflow]" | HIGH | Efficiency-focused |
| "batch process [X]" | HIGH | Volume handling |
| "scheduled [action]" | HIGH | Recurring task management |
| "trigger when [condition]" | HIGH | Conditional automation |
| "set it and forget it" | HIGH | Low-maintenance priority |
| "without manual [intervention]" | HIGH | Labor reduction |
| "workflow automation for [X]" | VERY HIGH | Sophisticated need |
| "no-code automation for [X]" | HIGH | Non-technical user |

### Time waste patterns (gold-standard signals)

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "save time on [task]" | HIGH | Direct time-value |
| "faster way to [X]" | HIGH | Speed optimization |
| "spend too much time on [X]" | VERY HIGH | Clear pain point |
| "takes too long to [X]" | VERY HIGH | Frustration indicator |
| "waste of time" | VERY HIGH | Strong dissatisfaction |
| "tedious [process]" | HIGH | Friction pain |
| "repetitive [task]" | HIGH | Automation candidate |
| "bottleneck in [workflow]" | VERY HIGH | Critical problem |
| "hours of work on [task]" | VERY HIGH | High-value opportunity |
| "busywork" | HIGH | Low-value task ID |
| "doing [X] by hand" | HIGH | Manual labor concern |
| "context switching between [tools]" | HIGH | Workflow disruption |

---

## Churn

### Active churn signals

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "stopped using [product]" | VERY HIGH | Recent churn |
| "gave up on [product]" | VERY HIGH | Frustrated ex-user |
| "cancelled [product] subscription" | VERY HIGH | Active churn |
| "moved away from [product]" | VERY HIGH | Migration opportunity |
| "tired of [product]" | VERY HIGH | Frustration indicator |
| "switched from [X] to [Y]" | VERY HIGH | Competitor insight |
| "left [product] for [alternative]" | VERY HIGH | Alternative validation |
| "ditching [product]" | VERY HIGH | Active churn |
| "fed up with [product]" | VERY HIGH | Strong frustration |
| "done with [product]" | VERY HIGH | Decisive exit |
| "looking to replace [product]" | VERY HIGH | Immediate opportunity |

### Pre-churn signals

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "thinking of leaving [product]" | VERY HIGH | Pre-churn signal |
| "considering switching from [product]" | VERY HIGH | Evaluation phase |
| "outgrew [product]" | HIGH | Scale/maturity transition |
| "[product] not worth the price" | VERY HIGH | Value perception issue |
| "frustrated with [product]" | HIGH | At-risk user |
| "regret using [product]" | VERY HIGH | Strong dissatisfaction |

---

## AI Specificity & Trust (Post-2025 Dynamics)

User sentiment has matured from simple "AI fatigue" to sophisticated demands for reliability, privacy, and control.

### AI Reliability & Verifiability

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "AI hallucinated" / "AI made up" | HIGH | Accuracy-critical use case |
| "AI confidently wrong" | HIGH | Trust breakdown, reliability concern |
| "can't trust AI for [task]" | VERY HIGH | Human-in-the-loop / verification tool opportunity |
| "fact check AI" / "verify AI output" | VERY HIGH | Demand for accuracy tools |
| "human review for AI" | VERY HIGH | Hybrid solution opportunity |
| "explainable AI" / "show your work" | HIGH | Need for transparency, not a black box |
| "source validation" | HIGH | B2B need for auditable AI results |

### Demand for Controllable / Local AI

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "privacy concerns with [AI product]" | VERY HIGH | Local/private alternative opportunity |
| "runs locally" / "offline AI" | VERY HIGH | Privacy-first buyer, technical user |
| "local LLM" / "self-hosted AI" | VERY HIGH | Control-focused user, data sovereignty |
| "doesn't upload my data" | HIGH | Strict privacy requirement |
| "bring your own key" / "BYOK" | HIGH | Enterprise/B2B security requirement |
| "editable AI output" | HIGH | Demand for control, not just generation |
| "fine-tuning" / "custom model" | HIGH | Need for domain-specific AI |

### AI Integration & Feature Bloat

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "no AI features" / "without AI" | VERY HIGH | Anti-AI, simplicity preference |
| "disable AI in [product]" | HIGH | Feature rejection, user control issue |
| "just want [basic function]" | HIGH | Feature bloat fatigue |
| "AI ruined [product]" | VERY HIGH | User experience degradation complaint |
| "before they added AI" | HIGH | Nostalgia for focused tool |
| "too much AI" / "forced AI" | HIGH | Overwhelm and autonomy concern |
| "AI integration" | MEDIUM | Need for AI in existing workflows |

---

## Media Workflow Pain

Pain points related to the explosion of video and audio content creation for marketing, education, and social media.

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| "video editing takes forever" | VERY HIGH | Efficiency tool for creators |
| "finding B-roll" / "stock video" | HIGH | Asset sourcing and management |
| "generating subtitles" / "captioning video" | VERY HIGH | Accessibility and engagement task |
| "podcast transcription" | HIGH | Content repurposing need |
| "audio cleanup" / "remove background noise" | HIGH | Quality improvement tool |
| "repurpose video for [platform]" | VERY HIGH | Multi-platform content strategy pain |
| "video chapters" / "timestamping" | HIGH | Discoverability and UX task for long videos |
| "thumbnail design" | HIGH | Marketing/optimization task |

---

## Signal Quality Filters

Use these patterns to increase the signal-to-noise ratio and filter out low-quality marketing content in favor of authentic user discussions.

| Pattern | Intent | Insight type |
|---------|--------|--------------|
| `("alternative to" OR "review") AND ("honest opinion" OR "unbiased")` | HIGH | Seeking authentic user experiences |
| `[product] NOT ("top 10" OR "best of" OR "ultimate guide")` | HIGH | Filtering out listicle-style marketing |
| `"[product] review" -sponsored -affiliate` | HIGH | Excluding paid or biased reviews |
| `"real review"` / `"my experience with"` | MEDIUM-HIGH | Finding first-hand accounts |
| `"is [product] still good"` | HIGH | Looking for long-term user feedback |

---

## Niche vocabulary

### Developers

**Communities**: r/programming, r/webdev, r/selfhosted, r/devops, r/javascript, r/python, r/ExperiencedDevs

**Patterns**: "CLI for [task]," "library for [language]," "framework for [use case]," "self-hosted [service]," "API for [integration]," "boilerplate for [stack]," "lightweight [tool]," "anyone using [tool] in production"

**Jargon**: DX, CRUD, monorepo, CI/CD, containerized, serverless, headless, hot reload, tech debt

### Designers

**Communities**: r/design, r/graphic_design, r/UI_Design, r/userexperience, r/web_design

**Patterns**: "UI kit for [platform]," "mockup tool for [use case]," "plugin for Figma/Sketch," "design system for [framework]," "font pairing for [style]," "handoff tool for developers"

**Jargon**: whitespace, kerning, design tokens, atomic design, component library, user flow, visual hierarchy

### Marketers

**Communities**: r/marketing, r/SEO, r/PPC, r/content_marketing, r/digital_marketing, r/bigseo

**Patterns**: "track competitors," "SEO tool for [need]," "email automation for [use case]," "cheaper alternative to [expensive tool]," "analytics dashboard for [platform]," "attribution tool"

**Jargon**: ROAS, CAC, LTV, MRR, attribution, funnel, conversion rate, CPM/CPC/CPA, retargeting

### Students

**Communities**: r/GetStudying, r/studytips, r/college, r/GradSchool, r/AskAcademia

**Patterns**: "note-taking app for [subject]," "flashcard app," "study schedule tool," "citation manager," "PDF annotator for [device]," "focus/concentration app," "cheap/free [academic tool]"

**Jargon**: spaced repetition, active recall, pomodoro, cramming, GPA, thesis, dissertation

### Freelancers

**Communities**: r/freelance, r/digitalnomad, r/forhire, r/freelanceWriters

**Patterns**: "invoice tool for freelancers," "client management tool," "proposal template," "contract template," "time tracking for clients," "bookkeeping tool for freelancers"

**Jargon**: retainer, scope creep, deliverable, SOW, net-30/60/90, 1099, burn rate

### Small business

**Communities**: r/smallbusiness, r/ecommerce, r/FulfillmentByAmazon, r/dropship, r/restaurateur

**Patterns**: "all-in-one tool for [business type]," "inventory management for small business," "CRM for small teams," "cheap alternative to [enterprise tool]," "POS system for [business type]"

**Jargon**: cash flow, overhead, margins, inventory turnover, foot traffic, repeat customers

---

## Supplementary Signals (Metadata)

These signals capture **market context** rather than user pain. Use when quotes mention competitive landscape or market size. They map to gate dimensions in the Seven-Dimension Model.

| Signal type | Maps to | Indicates | Example patterns |
|-------------|---------|-----------|------------------|
| `competitor-mention` | Competition ⚠️ | Competitive landscape | "we use [X]," "better than [Y]," "like [Z] but," "[product] vs [product]" |
| `market-size-indicator` | Market ⚠️ | Market scale signals | "[X] users," "growing industry," "popular in [niche]," "everyone uses" |

### Usage notes

1. **Not mutually exclusive**: A quote can have both a pain signal AND a metadata signal
2. **Secondary tagging**: If a quote primarily expresses pain but also mentions a competitor, tag the pain signal as primary, note competitor in Evidence
3. **Gate dimension evidence**: These signals directly support gate dimension scoring in Phase 8 evaluation

### Example

> "I hate how Notion is so slow (pain-expression), but everyone in my team uses it (market-size-indicator)"
> — Tag as `pain-expression` primary, extract "everyone in my team uses it" for Market Scale evidence
