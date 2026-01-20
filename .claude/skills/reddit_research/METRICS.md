# Quantitative Metrics for Reddit Research

This document provides quantitative frameworks for scoring and prioritizing opportunities discovered through Reddit research.

## Contents

- [Willingness to Pay Index (WPI)](#willingness-to-pay-index-wpi)
- [Pain Level Score (PLS)](#pain-level-score-pls)
- [Momentum Analysis](#momentum-analysis)
- [Anti-Cloud Trend Index](#anti-cloud-trend-index)

---

## Willingness to Pay Index (WPI)

Quantify payment likelihood by scanning comments for payment-related keywords and calculating weighted density.

### Keyword categories and weights

| Category | Keywords | Weight | Rationale |
|----------|----------|--------|-----------|
| **Explicit intent** | "I'd pay", "worth paying", "take my money", "shut up and take my money" | 5x | Direct purchase intent |
| **Current spending** | "paying for", "subscription costs", "$X/month", "already paying" | 4x | Proven budget allocation |
| **Price inquiry** | "pricing", "cost", "how much", "enterprise tier" | 3x | Active purchase consideration |
| **Professional context** | "for clients", "for my business", "for my agency" | 2x | B2B = higher budgets |
| **Time cost** | "saves hours", "worth the time", "saves me X hours" | 1x | Implicit value recognition |

### WPI Calculation

```
WPI = Σ (keyword_count × weight) / total_posts_analyzed
```

**Example**: Analyzing 50 posts about "invoice automation":
- Found 3 "I'd pay for" (3 × 5 = 15)
- Found 5 "paying $X/month" (5 × 4 = 20)
- Found 8 "pricing" mentions (8 × 3 = 24)
- Found 12 "for clients" (12 × 2 = 24)
- Found 10 "saves hours" (10 × 1 = 10)

WPI = (15 + 20 + 24 + 24 + 10) / 50 = **1.86**

### Benchmark thresholds by category

| Category | Low WPI | Medium WPI | High WPI | Notes |
|----------|---------|------------|----------|-------|
| **Finance** | <5 | 5-15 | >15 | Highest baseline willingness |
| **E-commerce** | <3 | 3-10 | >10 | Tool cost = business expense |
| **Productivity** | <2 | 2-8 | >8 | High noise, filter carefully |
| **Developer tools** | <1 | 1-4 | >4 | Developer paradox applies |
| **Consumer** | <0.5 | 0.5-2 | >2 | Very low conversion rates |

### Category reference data (from 9300+ sample)

Based on analysis of 9,363 "I wish there was an app" posts:

| Category | Pay signals | WPI estimate | Research priority |
|----------|------------|--------------|-------------------|
| Finance | 193 signals | ~15+ | ★★★★★ |
| Online Commerce | 76 signals | ~8 | ★★★★☆ |
| Travel | 42 signals | ~5 | ★★★☆☆ |
| Productivity | Low density | ~2 | ★★☆☆☆ (high volume, low conversion) |

**Key insight**: Productivity has highest request volume but NOT highest payment signals. Finance and E-commerce beat "General Productivity" for revenue potential.

---

## Pain Level Score (PLS)

Measure frustration intensity based on post characteristics. **Long, detailed posts are blueprints for feature lists.**

### Scoring dimensions

| Dimension | Score 1 | Score 2 | Score 3 |
|-----------|---------|---------|---------|
| **Post length** | <100 words | 100-300 words | >300 words |
| **Emotional intensity** | "wish", "would be nice" | "frustrated", "annoying" | "hate", "nightmare", "fed up" |
| **Detail level** | Vague description | Some specifics | Detailed workflow with steps |
| **Failed attempts** | None mentioned | 1-2 alternatives tried | 3+ alternatives tried |

### PLS Calculation

```
PLS = (length_score + emotion_score + detail_score + attempt_score) / 4
```

**Score interpretation**:
- **PLS ≥ 2.5**: Strong pain — Prioritize this opportunity
- **PLS 1.5-2.5**: Moderate pain — Worth investigating
- **PLS < 1.5**: Weak pain — Deprioritize unless other signals strong

### Category benchmarks (from 9300+ sample)

| Category | Avg post length | PLS estimate | Interpretation |
|----------|-----------------|--------------|----------------|
| **Developer platforms** | 229 words | High (~2.8) | ⚠️ High detail BUT check WPI (developer paradox) |
| **Cooking/Recipes** | 223 words | High (~2.7) | Users angry about ad bloat, passion-driven |
| **Parenting** | 221 words | High (~2.6) | Emotional, high-retention niche |
| **Smart Home/IoT** | Medium | Medium (~2.0) | Growing trend, visualization needs |
| **Productivity** | 145 words | Medium (~1.8) | Broad audience, less specific |

**Key insight**: Don't just count posts — **look for long posts**. A 300-word complaint is a feature specification document.

### Combined PLS + WPI decision matrix

| PLS | WPI | Verdict |
|-----|-----|---------|
| High | High | ✅ **Strong opportunity** — Pursue immediately |
| High | Low | ⚠️ **Passion project** — Check developer paradox |
| Low | High | ⚠️ **Quick win possible** — Low complexity feature |
| Low | Low | ❌ **Skip** — Neither pain nor payment signal |

---

## Momentum Analysis

Track opportunity trending signals over rolling 60-day windows.

### Momentum indicators

| Indicator | Bullish 📈 | Neutral ➡️ | Bearish 📉 |
|-----------|-----------|-----------|-----------|
| **Post frequency** | Increasing month-over-month | Stable | Declining |
| **Comment engagement** | Rising avg comments | Stable | Declining |
| **New competitors** | None mentioned | 1-2 new entrants | 3+ new entrants discussed |
| **"Alternative to" posts** | Increasing | Stable | Dominant alternative emerged |
| **"Solved by X" comments** | Rare | Occasional | Frequent |

### 60-day comparison method

1. **Count posts T-60 to T-0** (current period)
2. **Count posts T-120 to T-60** (prior period)
3. **Calculate growth rate**: `(current - prior) / prior × 100%`

**Interpretation**:
- **>20% growth**: Hot trend — First mover advantage possible
- **0-20% growth**: Stable opportunity — Validate carefully
- **<0% growth**: Cooling trend — Check if problem solved or market saturated

### Timing heuristics

**Weekly patterns** (from 9300+ sample):
- **Peak frustration**: Monday-Tuesday (people hit workflow friction at week start)
- **Solution research**: Wednesday-Thursday (mid-week research time)
- **Decision making**: Friday (wrap-up before weekend)

**Seasonality markers**:

| Category | Peak seasons | Rationale |
|----------|-------------|-----------|
| Tax/Finance | Jan-Apr, Sep-Oct | Tax deadlines |
| E-commerce | Oct-Dec | Holiday prep |
| Education | Aug-Sep, Jan | School year start |
| Health/Fitness | Jan, Sep | New Year + back-to-work |
| Productivity | Jan, Sep | Resolution + fresh start mindset |

**Trend example** (from 9300+ sample):
- Health & Wellness + Gaming spiked in Dec-Jan 2026
- Follows "New Year, New Me" trend
- Gym trackers, habit-builders, gamified life tools are heating up

---

## Anti-Cloud Trend Index

Track subscription fatigue and privacy-first sentiment. Growing opportunity for offline-first and one-time-purchase models.

### Market data (from 9300+ sample)

- **7% of all requests** (640+ posts) specifically asked for offline-first or privacy-focused tools
- Primary drivers: subscription fatigue, data ownership concerns
- Strongest in: productivity tools, developer tools, note-taking

### Detection queries

```
site:reddit.com "subscription fatigue" OR "tired of subscriptions" [category]
site:reddit.com "one-time purchase" OR "lifetime license" [category]
site:reddit.com "self-hosted" OR "on-prem" OR "offline" [category]
site:reddit.com "no cloud" OR "local only" OR "runs locally" [category]
site:reddit.com "own my data" OR "data ownership" [category]
```

### Anti-Cloud Score calculation

For a given opportunity, count mentions in these categories:

| Category | Weight | Example phrases |
|----------|--------|-----------------|
| **Subscription rejection** | 3x | "no subscription", "one-time purchase", "lifetime" |
| **Privacy concern** | 2x | "privacy", "own my data", "doesn't upload" |
| **Self-hosting desire** | 2x | "self-hosted", "run locally", "on my machine" |
| **Cloud distrust** | 1x | "no cloud", "offline capable", "works without internet" |

```
Anti-Cloud Score = Σ (mention_count × weight) / total_posts
```

**Interpretation**:
- **Score > 1.0**: Strong anti-cloud sentiment — Consider offline-first or hybrid model
- **Score 0.3-1.0**: Moderate sentiment — Offer offline option as differentiator
- **Score < 0.3**: Low sentiment — Cloud-first acceptable

### Positioning implications

| Anti-Cloud Score | Pricing model | Architecture |
|------------------|---------------|--------------|
| High (>1.0) | One-time + optional cloud sync | Local-first, sync optional |
| Medium (0.3-1.0) | Freemium with local tier | Cloud primary, offline mode |
| Low (<0.3) | SaaS subscription | Cloud-native |

---

## Quick Reference Card

### Opportunity Scoring Checklist

For each candidate opportunity, calculate:

| Metric | Score | Threshold | Pass? |
|--------|-------|-----------|-------|
| WPI | _____ | Category benchmark | ☐ |
| PLS | _____ | ≥ 2.0 preferred | ☐ |
| Momentum | _____ | ≥ 0% growth | ☐ |
| Anti-Cloud | _____ | Note for positioning | ☐ |

### Red flags (deprioritize if present)

- WPI < category minimum AND PLS < 1.5
- Momentum < -20% (problem being solved elsewhere)
- Developer category with WPI < 1 (developer paradox)
- "Perfect free solution" in top comments

### Green flags (prioritize if present)

- WPI > category "High" threshold
- PLS ≥ 2.5 with specific workflow descriptions
- Momentum > 20% with no dominant solution
- Multiple "I'd pay for this" comments with upvotes
