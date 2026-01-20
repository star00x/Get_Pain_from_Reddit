# Seven-Dimension Evaluation Framework

Complete scoring criteria for Micro-SaaS opportunity evaluation.

**Framework version**: 2.0 (expanded from 5 to 7 dimensions)

**Key change**: Demand + Competition + Market form the **gate dimensions**. Any gate dimension scoring 🔴 Low results in automatic disqualification.

## Dimension definitions

### 1. Demand Rigidity

**Question**: Will users actually pay? Is the problem urgent enough?

| Score | Criteria | Example signals |
|-------|----------|-----------------|
| 🟢 **High** | Explicit willingness to pay OR blocking/urgent pain; no acceptable alternative | "Would pay for this," "need this yesterday," quantified costs ($X/month, Y hours/week) |
| 🟡 **Medium** | Users complain but tolerate workarounds; "nice to have" unless very cheap | "Annoying but I manage," occasional mentions without urgency |
| 🔴 **Low** | Casual mentions, hypothetical wishes, OR problem already solved by free tools | "Would be cool if," "just use [free tool]" in top comments |

**Key signals**:
- Current spending: "I pay $X/month for..." ★★★★★
- Custom development: "Hired someone on Upwork to..." ★★★★★
- Quantified time cost: "Spend 4 hours every week on..." ★★★★
- Compliance pressure: "Auditors require..." ★★★★★
- Failed DIY attempts: "My Excel sheet keeps breaking..." ★★★★

### 2. Feature Focus

**Question**: Can the core value be described in one sentence?

| Score | Criteria | Example signals |
|-------|----------|-----------------|
| 🟢 **High** | Single workflow, single persona; value prop fits in one sentence | "Convert PDF invoices to QuickBooks entries" |
| 🟡 **Medium** | 2-3 tightly related features; clear primary use case + secondary add-ons | Main feature + "also nice to have..." |
| 🔴 **Low** | Scattered feature requests, unclear boundaries, "platform" ambitions | "It should do X and Y and Z and also integrate with everything" |

**Warning signs**:
- Multiple unrelated user personas
- Feature requests pulling in opposite directions
- "Everything app" requests
- No clear "job to be done"

### 3. Technical Feasibility

**Question**: Can a solo developer ship an MVP in 2-4 weeks?

| Score | Criteria | Example signals |
|-------|----------|-----------------|
| 🟢 **High** | Standard web stack, mature libraries, no new algorithms; <4 weeks MVP | CRUD app, simple integrations, well-documented APIs |
| 🟡 **Medium** | Requires learning new tech OR coordinating 2-3 external services; 4-8 weeks | Multiple API integrations, moderate data transformation |
| 🔴 **Low** | Requires team, R&D, or depends on unstable/proprietary tech | ML model training, real-time video processing, hardware integration |

**Complexity factors**:
- Real-time requirements: WebSocket, live collaboration
- Data processing: ETL pipelines, large file handling
- Compliance: HIPAA, SOC2, PCI (adds audit overhead)
- Mobile native: iOS/Android native (vs web/PWA)

### 4. API Availability

**Question**: Can core functionality be built by composing existing APIs?

| Score | Criteria | Example signals |
|-------|----------|-----------------|
| 🟢 **High** | Core features achievable with 1-2 well-documented APIs | OpenAI + Stripe, Twilio + SendGrid |
| 🟡 **Medium** | Requires 3+ API integrations OR significant data transformation layer | Multiple services to orchestrate, custom glue code |
| 🔴 **Low** | No suitable API; must build core capability from scratch | OCR for niche documents, domain-specific NLP, proprietary algorithms |

**Common APIs by category**:
- AI/ML: OpenAI, Anthropic, Replicate, Hugging Face
- Payments: Stripe, Paddle, LemonSqueezy
- Communication: Twilio, SendGrid, Postmark
- Data: Plaid, Clearbit, Hunter.io
- Storage: AWS S3, Cloudflare R2
- Auth: Clerk, Auth0, Supabase Auth

### 5. SEO Potential

**Question**: Can the product acquire users through organic search?

| Score | Criteria | Example signals |
|-------|----------|-----------------|
| 🟢 **High** | Clear long-tail keywords with search intent; low competition; content moat opportunity | "How to [task]," "best [tool] for [niche]," educational content potential |
| 🟡 **Medium** | Keywords exist but competitive; requires differentiated content strategy | Established players ranking, but angle possible |
| 🔴 **Low** | No natural search intent; depends on paid ads, virality, or outbound sales | Enterprise sales, referral-only markets, social-first products |

**SEO indicators**:
- Problem keywords users actually search
- Competitor density in SERPs
- Content moat potential (tutorials, templates, guides)
- Long-tail vs head term ratio

### 6. Competition Landscape ⚠️ GATE DIMENSION

**Question**: Is there space to compete? Are incumbents beatable?

| Score | Criteria | Example signals |
|-------|----------|-----------------|
| 🟢 **High** | No clear market leader OR leader has systematic weaknesses | No dominant player, fragmented market, users complaining about all options |
| 🟡 **Medium** | 2-3 competitors exist but differentiation angle is clear | Established players but clear gap (pricing, niche, simplicity) |
| 🔴 **Low** | Market dominated by well-funded players with no obvious gaps | Category leaders (Notion, Airtable, etc.) with no systematic complaints |

**Assessment questions**:
1. Who are the top 3 competitors? (List names + funding/team size if known)
2. What do users complain about most in existing solutions?
3. Is there a clear differentiation angle? (Simpler? Cheaper? Specific niche?)
4. Are competitors small enough to compete with?

**Evidence requirements**:
- Competitor list with brief assessment
- User complaint summary from Reddit/reviews
- Clear differentiation statement

**Why this is a gate dimension**: Even strong demand is worthless if you can't compete. Building in a dominated market = high risk of failure regardless of product quality.

### 7. Market Scale ⚠️ GATE DIMENSION

**Question**: Is the market big enough to sustain a viable business?

| Score | Criteria | Example signals |
|-------|----------|-----------------|
| 🟢 **High** | Target community 10K+ members OR similar tools have proven success | Active subreddit, public revenue reports, multiple successful competitors |
| 🟡 **Medium** | Target community 3-10K members OR small-scale success cases exist | Smaller but active community, indie success stories |
| 🔴 **Low** | Target community <3K members AND no validation cases | Tiny niche, no comparable success stories, unclear if anyone will pay |

**Assessment methods**:
1. **Community size**: Subreddit subscriber count, forum membership
2. **Post frequency**: Activity level in target communities
3. **Comparable success**: Similar tools with public revenue (Indie Hackers, Twitter, etc.)
4. **TAM estimation**: Rough calculation from industry data

**Market math example**:
```
Subreddit: 5,000 members
Reddit ≈ 5% of total market → 100,000 potential users
3% awareness × 5% conversion = 0.15% of total market
150 customers × $20/month = $3,000 MRR potential

Assessment: 🟡 Medium (viable for solo founder, but limited ceiling)
```

**Evidence requirements**:
- Community size metrics
- Comparable product success data (if available)
- Rough market size estimation with reasoning

**Why this is a gate dimension**: A perfect product in a too-small market = failed business. Must validate sufficient market size before investing.

## Gate dimension summary

| Dimension | Role | Why it gates |
|-----------|------|--------------|
| **Demand Rigidity** | Validates "will they pay?" | No demand = no revenue |
| **Competition Landscape** | Validates "can we win?" | Unwinnable competition = wasted effort |
| **Market Scale** | Validates "is it big enough?" | Too small = unsustainable business |

**Gate logic**: If ANY gate dimension = 🔴 Low → Automatic ❌ Pass

**Non-gate dimensions** (Focus, Tech, API, SEO) affect opportunity strength but don't automatically disqualify.

## Signal-to-dimension mapping

Route collected signals to appropriate dimensions:

| Signal type | Primary dimension | Secondary | Notes |
|-------------|-------------------|-----------|-------|
| `pain-expression` | Demand | — | Core demand signal; urgency matters |
| `switching` | Demand | Competition | Active buying intent; also reveals competitor weaknesses |
| `churn` | Demand | Competition | Market dissatisfaction; reveals competitor failures |
| `price-sensitivity` | Demand | Market | Willingness indicator; also reveals market price ceiling |
| `tool-seeking` | Demand | — | Active shopping behavior |
| `feature-gap` | Focus | Competition | Scope definition; also reveals competitor gaps |
| `ux-friction` | Focus | Competition | UX issues reveal differentiation opportunity |
| `automation-desire` | Focus | — | Workflow scope; usually focused |
| `integration-need` | API | Tech | External dependency signal |
| `ai-fatigue` | Focus | — | Anti-feature signal; non-AI opportunity |
| `competitor-mention` | Competition | — | Direct competitive landscape signal |
| `market-size-indicator` | Market | — | Community size, industry scope signals |

## Composite judgment logic

Apply these rules to derive final recommendation.

**Key change in v2.0**: Gate dimensions (Demand, Competition, Market) are checked first. Any 🔴 Low in gate dimensions = automatic disqualification.

```python
def judge_opportunity_v2(scores: dict) -> str:
    """
    Seven-dimension evaluation with gate logic.

    Gate dimensions (any Low = auto-fail):
    - demand: Demand Rigidity
    - competition: Competition Landscape
    - market: Market Scale

    Non-gate dimensions (affect strength, don't auto-fail):
    - focus: Feature Focus
    - tech: Technical Feasibility
    - api: API Availability
    - seo: SEO Potential
    """
    # Gate dimensions (any Low = immediate Pass)
    demand = scores['demand']
    competition = scores['competition']
    market = scores['market']

    # Non-gate dimensions
    focus = scores['focus']
    tech = scores['tech']
    api = scores['api']
    seo = scores['seo']

    # === GATE CHECK (highest priority) ===
    gate_dimensions = [demand, competition, market]
    if any(g == 'low' for g in gate_dimensions):
        failed_gates = [name for name, val in
                       [('Demand', demand), ('Competition', competition), ('Market', market)]
                       if val == 'low']
        return f"❌ Pass (Gate failed: {', '.join(failed_gates)})"

    # Technical feasibility is also a hard blocker (can't build = can't ship)
    if tech == 'low':
        return "❌ Pass (Technical barrier)"

    # === STRENGTH ASSESSMENT ===
    non_gate_dimensions = [focus, api, seo]
    red_count = sum(1 for s in non_gate_dimensions if s == 'low')

    # Too many non-gate reds = Pass
    if red_count >= 2:
        return "❌ Pass (Multiple dimension risks)"

    # All dimensions at least Medium = Strong opportunity
    all_scores = [demand, competition, market, focus, tech, api, seo]
    if all(s in ['high', 'medium'] for s in all_scores):
        # Bonus: At least one High in gates + one High elsewhere
        gate_highs = sum(1 for g in gate_dimensions if g == 'high')
        other_highs = sum(1 for s in [focus, tech, api, seo] if s == 'high')
        if gate_highs >= 1 and other_highs >= 1:
            return "✅ Strong"
        elif red_count == 0:
            return "✅ Strong"

    # One red in non-gate = Conditional
    if red_count == 1:
        return "⚠️ Conditional (mitigate: " +
               [name for name, val in [('Focus', focus), ('API', api), ('SEO', seo)]
                if val == 'low'][0] + ")"

    return "⚠️ Conditional"
```

### Verdict reference table

| Gate dimensions (Demand + Competition + Market) | Tech | Non-gate reds | Verdict |
|------------------------------------------------|------|---------------|---------|
| Any 🔴 Low | — | — | ❌ Pass |
| All ≥ 🟡 Medium | 🔴 Low | — | ❌ Pass |
| All ≥ 🟡 Medium | ≥ 🟡 Medium | 0 | ✅ Strong |
| All ≥ 🟡 Medium | ≥ 🟡 Medium | 1 | ⚠️ Conditional |
| All ≥ 🟡 Medium | ≥ 🟡 Medium | 2+ | ❌ Pass |

### Gate dimension failure reasons

When a gate dimension fails, document the specific reason:

| Failed gate | Common reasons | Research action |
|-------------|----------------|-----------------|
| **Demand** | No payment signals, only "nice to have" | Pivot to different pain point |
| **Competition** | Market dominated by well-funded players | Find smaller niche or pivot |
| **Market** | Community too small, no comparable success | Expand scope or pivot |

## Evidence requirements

Each dimension score MUST have at least one supporting citation:

| Dimension | Required evidence | Gate? |
|-----------|-------------------|-------|
| **Demand** | Link to Reddit post/comment with pain statement | ⚠️ Yes |
| **Competition** | Competitor list + user complaint summary | ⚠️ Yes |
| **Market** | Community size metrics + comparable success data | ⚠️ Yes |
| **Focus** | Summary of the single workflow being solved | No |
| **Tech** | List of required integrations + complexity estimate | No |
| **API** | API names + documentation links | No |
| **SEO** | Keyword research screenshot/link OR SERP competition note (mark as "estimated" if no tools) | No |

**Gate dimension evidence is mandatory**. If gate dimension evidence cannot be found, the opportunity cannot be evaluated.

## Output template

```markdown
### [Opportunity Name]

**One-sentence description**: [Single sentence describing the product]

#### Gate Dimensions (any 🔴 = automatic Pass)

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Demand Rigidity ⚠️ | 🟢/🟡/🔴 | [Citation + brief explanation] |
| Competition Landscape ⚠️ | 🟢/🟡/🔴 | [Competitors + weaknesses] |
| Market Scale ⚠️ | 🟢/🟡/🔴 | [Community size + comparable success] |

#### Execution Dimensions

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Feature Focus | 🟢/🟡/🔴 | [Citation + brief explanation] |
| Technical Feasibility | 🟢/🟡/🔴 | [Citation + brief explanation] |
| API Availability | 🟢/🟡/🔴 | [API names + doc links] |
| SEO Potential | 🟢/🟡/🔴 | [Keywords + competition notes] |

**Verdict**: ✅ Strong / ⚠️ Conditional / ❌ Pass

**Rationale**: [2-3 sentences explaining the verdict and any yellow/red flag mitigations]

**Next steps** (if ✅ or ⚠️): [Specific actionable items: create landing page, build MVP prototype, validate with 5 users, etc.]
```

### Quick evaluation template (for initial screening)

For rapid filtering, evaluate gate dimensions first:

```markdown
### [Opportunity Name] — Quick Screen

| Gate | Score | 30-second assessment |
|------|-------|---------------------|
| Demand | 🟢/🟡/🔴 | [Payment signals found? Y/N] |
| Competition | 🟢/🟡/🔴 | [Beatable incumbents? Y/N] |
| Market | 🟢/🟡/🔴 | [Sufficient size? Y/N] |

**Gate check**: PASS / FAIL

If PASS → Proceed to full 7-dimension evaluation
If FAIL → Document reason and skip
```

## Coverage assessment

After initial evaluation, assess seven-dimension coverage:

1. **Count citations per dimension**: Identify dimensions with <2 supporting quotes
2. **Flag conflicting signals**: Same opportunity has contradictory assessments
3. **Follow-up queries**: Generate targeted queries for under-explored dimensions

### Follow-up conditions

**If coverage gaps exist**:
- Generate targeted follow-up queries
- Launch 1-2 focused subagents (not full re-run)
- Append new findings and re-evaluate

**If conflicting signals exist** (high-priority opportunities):
- Generate validation queries to resolve ambiguity
- Document conflict in notes for Phase 8 resolution

### Iteration limit

**Maximum 1 follow-up iteration per run** to prevent infinite loops. If gaps persist after follow-up, document in `## Errors & Follow-ups` and proceed.

## Ordering and presentation

In final report:

1. **Sort by verdict**: ✅ Strong first, then ⚠️ Conditional, then ❌ Pass
2. **Within verdict**: Sort by Demand Rigidity strength
3. **Pass opportunities**: Move to appendix with brief disqualification reason
4. **Ensure actionability**: Every "Next steps" item should be specific and executable
