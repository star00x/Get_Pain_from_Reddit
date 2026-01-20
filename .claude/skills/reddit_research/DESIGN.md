# Reddit Product Research Skill - Design Document

This document explains the design decisions behind the `researching-reddit-opportunities` Agent Skill, following Anthropic's official best practices.

## Skill structure overview

```
reddit-product-research/
├── SKILL.md                    # Main instructions (loaded when triggered)
├── PATTERNS.md                 # 200+ search pattern library (loaded as needed)
├── SYNTAX.md                   # Reddit/Google syntax reference (loaded as needed)
├── COMMUNITIES.md              # Community selection guide (loaded as needed)
└── EXTRACTION.md               # Comment extraction technical reference (loaded as needed)
```

## Design decisions aligned with best practices

### 1. Conciseness (context window is a public good)

The SKILL.md body is kept under 500 lines. Claude already knows what Reddit is, how search engines work, and general product research concepts. The Skill adds only what Claude does not already know: the specific pattern library, the echo chamber trap, the free solution test, and the structured methodology.

**What we assume Claude knows**:
- How to construct search queries
- General business and product concepts
- Reddit's purpose and structure

**What we explicitly provide**:
- Domain-specific search patterns (200+)
- Critical filters (echo chamber, free solution)
- Scoring frameworks and convergence tables
- Platform-specific syntax quirks

### 2. Progressive disclosure (tiered content loading)

Following the "one level deep" principle, SKILL.md provides an overview and points to reference files. Claude loads detailed content only when the task requires it.

**Tier 1 (always loaded)**: Core methodology in SKILL.md
- Echo chamber filter
- Workflow modes
- Free solution test
- Scoring dimensions

**Tier 2 (loaded as needed)**: Reference files
- PATTERNS.md: Complete pattern library by category
- SYNTAX.md: Search operator syntax
- COMMUNITIES.md: Subreddit mapping
- EXTRACTION.md: JSON structure, signal patterns, rate limiting workarounds

This prevents token waste when the user only needs a subset of capabilities.

### 3. Appropriate degrees of freedom

The Skill uses **medium-to-high freedom** because:
- Multiple valid approaches exist for any research objective
- Decisions depend heavily on context (target market, product type, user goals)
- The methodology provides heuristics, not rigid procedures

However, certain elements require **low freedom** (specific instructions):
- Search syntax (case-sensitive operators, no spaces after colons)
- The echo chamber filter (always warn if targeting builder communities)
- The free solution test (always check top comments before recommending)

### 4. Naming convention (gerund form)

The name `researching-reddit-opportunities` follows the recommended gerund pattern, clearly describing the activity the Skill provides.

### 5. Description for discovery

The description includes:
- What the Skill does (discovers opportunities, generates queries, scores opportunities)
- When to use it (product research, market validation, competitor analysis, query generation)
- Key terms for discovery (Reddit, Micro-SaaS, pain points, validation)

Written in third person as required: "Discovers..." not "I can help you discover..."

### 6. Workflow patterns

The Skill defines four workflow modes based on user intent:
1. **Discovery mode**: Exploration with broad patterns
2. **Validation mode**: Hypothesis testing with counter-queries
3. **Competitive intelligence mode**: Competitor weakness mapping
4. **Query generation mode**: Direct query output

This follows the "conditional workflow pattern" from best practices.

### 7. Feedback loops

The free solution disqualification test implements a validation loop:
1. Find threads about target pain
2. Check top comments for free solutions
3. If perfect free solution exists → disqualify
4. If partial solutions → conditional opportunity

This prevents Claude from recommending opportunities that will face "but you can just use [free thing]" objections.

### 8. Template pattern

The output format section provides a structured template:
```
## Research: [Objective]
### Target communities
### Query set
### Validation checklist
```

This ensures consistent, actionable outputs.

### 9. Examples pattern

The reference files include concrete input/output examples for search patterns, showing both the pattern and expected insight type.

### 10. Avoiding time-sensitive information

The Skill avoids hardcoded dates or version numbers. The only time-sensitive element is the AI fatigue section, which is framed as a "2025 market dynamic" rather than absolute truth, acknowledging it may evolve.

Tool recommendations (GummySearch closure) are handled by omission rather than explicit dating.

## Scenarios considered

### Scenario 1: Novice user with vague input

User says: "I want to find SaaS ideas"

The Skill will:
- Ask clarifying questions about target user type
- Default to Discovery mode
- Warn about builder echo chamber trap
- Provide educational context about verb-over-noun principle

### Scenario 2: Experienced researcher with specific hypothesis

User says: "I believe accountants struggle with client document collection"

The Skill will:
- Activate Validation mode
- Generate confirming queries targeting r/Accounting, r/taxpros
- Generate disconfirming queries (free solution test)
- Apply the "every time / always / constantly" test

### Scenario 3: User targeting AI markets

The Skill includes AI fatigue patterns (accuracy concerns, privacy concerns, "no AI" preferences) to surface counter-positioning opportunities.

### Scenario 4: User needs executable queries

The Skill generates copy-paste-ready queries with:
- Correct case for boolean operators (AND/OR/NOT)
- Proper field filter syntax (no spaces)
- `self:true/false` (not `self:yes/no`)

### Scenario 5: User asking about wrong communities

If user mentions r/SaaS or r/Entrepreneur as research targets, the Skill explicitly warns and redirects to customer communities.

## What this Skill does NOT include

Following the "Claude is already smart" principle, we omit:
- Explanation of what Reddit is
- General product research methodology
- Basic marketing concepts
- Explanation of what SaaS or Micro-SaaS means

## Testing recommendations

Before deployment, test with:

1. **Haiku**: Does the Skill provide enough guidance for simpler models?
2. **Sonnet**: Is the Skill clear and efficient?
3. **Opus**: Does the Skill avoid over-explaining?

Example evaluation:
```json
{
  "skills": ["researching-reddit-opportunities"],
  "query": "Find opportunities in the PDF tools market",
  "expected_behavior": [
    "Recommends customer communities (r/college, r/LawFirm, r/GradSchool)",
    "Warns against r/SaaS, r/Entrepreneur",
    "Generates queries using high-intent patterns",
    "Includes free solution test queries"
  ]
}
```

## Iteration approach

Following the "Claude A / Claude B" development pattern:
1. Use the Skill with Claude B on real research tasks
2. Observe where it struggles or succeeds
3. Return to Claude A with observations
4. Refine and test again

Common refinements to watch for:
- Does Claude consistently apply the echo chamber filter?
- Are generated queries syntactically correct?
- Does Claude remember to check top comments for free solutions?
- Is the scoring framework applied consistently?
