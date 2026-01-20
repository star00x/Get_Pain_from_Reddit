---
name: microsaas-opportunity-evaluation
description: Seven-dimension opportunity assessment framework for Micro-SaaS product ideas. Transforms raw demand signals into actionable build/no-build recommendations. Use when evaluating product opportunities, scoring ideas, or filtering research findings for viability.
---

# Micro-SaaS Opportunity Evaluation

Seven-dimension framework with gate logic for systematically evaluating Micro-SaaS opportunities. Gate dimensions (Demand, Competition, Market) must pass before other dimensions are considered.

## Triggers

- Wide Research involves product opportunity discovery
- User requests "评估 Micro-SaaS 机会" or "opportunity evaluation"
- User has collected demand signals and needs scoring
- Reference to this skill directory

## Capabilities

- Seven-dimension opportunity scoring with gate logic
- Gate dimensions: Demand Rigidity, Competition Landscape, Market Scale
- Execution dimensions: Feature Focus, Technical Feasibility, API Availability, SEO Potential
- Signal-to-score mapping from Reddit/web research
- Composite go/no-go recommendations
- Red flag detection and automatic disqualification

## Dependencies

- Often triggered by `wide_research/` during Phase 6-7
- Uses signal data from `reddit_research/` findings

## Load order

1. This file (always — ~100 tokens)
2. `FRAMEWORK.md` (when evaluating — ~1.5k tokens)

## Quick reference

### Seven dimensions

| Dimension | Gate? | Question | Best signal sources |
|-----------|-------|----------|---------------------|
| **Demand Rigidity** | ⚠️ | Will users pay? | "willing to pay," budget mentions, existing spending |
| **Competition Landscape** | ⚠️ | Incumbents beatable? | User complaints about competitors, differentiation angles |
| **Market Scale** | ⚠️ | Market big enough? | Community size, comparable success evidence |
| **Feature Focus** | — | One-sentence value prop? | Single workflow vs scattered requests |
| **Technical Feasibility** | — | Solo dev MVP in 2-4 weeks? | Integration complexity, real-time needs |
| **API Availability** | — | Mature third-party APIs? | OpenAI, Stripe, Twilio mentions |
| **SEO Potential** | — | Organic acquisition possible? | Long-tail keywords, content moat |

### Scoring scale

- 🟢 **High**: Strong positive signals, low risk
- 🟡 **Medium**: Mixed signals, conditional viability
- 🔴 **Low**: Weak or negative signals, significant risk

### Composite judgment (gate-first)

| Condition | Verdict |
|-----------|---------|
| Any gate dimension (Demand/Competition/Market) = 🔴 | ❌ Pass |
| Technical Feasibility = 🔴 | ❌ Pass |
| Non-gate reds (Focus/API/SEO) ≥ 2 | ❌ Pass |
| All dimensions ≥ 🟡 Medium | ✅ Strong |
| Exactly one non-gate 🔴 | ⚠️ Conditional |

### Red flag override

**Free solution test FAIL** (perfect free alternative exists in top comments) → Demand automatically becomes 🔴.

## Detailed framework

See [FRAMEWORK.md](FRAMEWORK.md) for complete scoring criteria, signal mapping, and output templates.
