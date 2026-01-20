# Child Output Contract

Validation rules for subagent outputs. Every `child_outputs/<id>.md` must conform to this contract.

## Required sections (in order)

1. `## Scope & Inputs` — Research scope and input parameters
2. `## Key Findings` — Primary discoveries
3. `## Evidence (with citations)` — Supporting evidence with links
4. `## Gaps & Next Steps` — Data gaps and suggested follow-ups
5. `## Errors & Follow-ups` — Only when errors occur

## Additional sections (context-dependent)

### Micro-SaaS research

When subtask involves product opportunity discovery, add:

6. `## Opportunity Signals` — Seven-dimension model signals with gate logic (see `microsaas_eval/`)

### Reddit research

When subtask involves Reddit, ensure Evidence section includes:
- `### Representative quotes (verbatim)` with metadata
- `### Free solution disqualification test` with PASS/CONDITIONAL/FAIL verdict

## Validation gates

| Check | Requirement | Failure action |
|-------|-------------|----------------|
| **Section presence** | All required sections exist | Retry once |
| **Citation count** | ≥2 Markdown links `[text](url)` | If impossible, explain in Errors |
| **No placeholders** | No `<id>`, `${...}`, `{{...}}`, `TODO`, `TBD` | Retry or manual completion |
| **Language** | Simplified Chinese (unless user specifies) | Retry |
| **Opportunity Signals** | Present and non-empty (Micro-SaaS only) | Add missing dimensions |

## Validation logic

```python
def validate_child_output(content: str, is_microsaas: bool = False) -> tuple[bool, list[str]]:
    errors = []

    # Check required sections
    required = ["## Scope & Inputs", "## Key Findings", "## Evidence"]
    for section in required:
        if section not in content:
            errors.append(f"Missing section: {section}")

    # Check citation count
    import re
    citations = re.findall(r'\[.*?\]\(https?://.*?\)', content)
    if len(citations) < 2:
        errors.append(f"Insufficient citations: {len(citations)}/2")

    # Check placeholders
    placeholders = re.findall(r'<\w+>|\$\{.*?\}|\{\{.*?\}\}|TODO|TBD', content)
    if placeholders:
        errors.append(f"Unexpanded placeholders: {placeholders}")

    # Micro-SaaS specific
    if is_microsaas and "## Opportunity Signals" not in content:
        errors.append("Missing section: ## Opportunity Signals")

    return (len(errors) == 0, errors)
```

## Retry policy

1. **First failure**: Retry with same prompt
2. **Second failure**: Preserve `## Errors & Follow-ups` section, continue aggregation
3. **Never skip**: Aggregation must not miss coverage due to single-point failures

## Quote formatting rules

1. **Preserve original**: Keep typos, grammar, formatting exactly as written
2. **Include context**: Use [brackets] for editorial notes if needed
3. **Link to source**: Always include full URL (thread or comment permalink)
4. **Required metadata**: subreddit, date, upvotes (use ↑ symbol)
5. **One signal type per quote**: Choose primary intent signal

**Quote format template**:
```markdown
> "[Preserved verbatim quote]"
> — r/[subreddit], [YYYY-MM-DD], ↑[upvotes]
> 🔗 [full URL]
> **Signal type**: [signal-type]
```

## Signal type reference

Map quotes to these categories (from `reddit_research/PATTERNS.md`):

| Signal type | Indicates | Example patterns |
|-------------|-----------|------------------|
| `pain-expression` | Active frustration | "struggling with," "frustrated," "hate when" |
| `switching` | Ready to change | "alternative to," "replacement for," "done with" |
| `churn` | Recently left | "stopped using," "cancelled," "gave up on" |
| `feature-gap` | Missing functionality | "wish X had," "doesn't have," "missing" |
| `price-sensitivity` | Cost deciding factor | "too expensive," "cheaper alternative" |
| `ux-friction` | Usability issues | "confusing," "clunky," "outdated UI" |
| `automation-desire` | Manual work pain | "tedious," "takes hours," "repetitive" |
| `tool-seeking` | Actively shopping | "best app for," "recommend a tool" |
| `integration-need` | Workflow connectivity | "sync between," "connect X to Y," "API" |
| `ai-fatigue` | AI-specific concerns | "hallucinated," "can't trust AI," "no AI" |

## Section templates

### Scope & Inputs

```markdown
## Scope & Inputs

- **Research scope**: [description]
- **Input parameters**: [community list, search patterns, etc.]
- **Time range**: [e.g., past 180 days]
- **Posts reviewed**: [number]
```

### Key Findings

```markdown
## Key Findings

### Pain Points Discovered

1. **[Pain Point Title]**
   - Frequency: [daily/weekly/occasional]
   - Intensity: [high/medium/low]
   - Representative comment: > "..."

2. **[Pain Point Title]**
   ...
```

### Evidence (with citations)

```markdown
## Evidence (with citations)

### Representative quotes (verbatim)

> "[Quote 1]"
> — r/subreddit, 2024-12-01, ↑42
> 🔗 https://reddit.com/r/xxx/...
> **Signal type**: pain-expression

> "[Quote 2]"
> — r/subreddit, 2024-11-15, ↑28
> 🔗 https://reddit.com/r/xxx/...
> **Signal type**: switching

### Free solution disqualification test

- [x] Checked top-voted comments
- Free solutions found: [list or "none"]
- **Conclusion**: [PASS / CONDITIONAL / FAIL]
```

### Opportunity Signals (Micro-SaaS)

```markdown
## Opportunity Signals

### Demand Rigidity Signals
- [Citation/paraphrase]([link]) — Urgency: blocking/annoying/nice-to-have
- Willingness to pay indicators: [price mentions, budget discussions]
- Alternative complaints: [how users currently cope]

### Feature Focus Signals
- Core problem one-sentence summary: [...]
- Observed feature requests: [list, note if focused or scattered]
- Target persona clarity: [specific role/industry or vague]

### Technical Feasibility Signals
- Required integrations: [list APIs/services mentioned]
- Real-time requirement: [yes/no, complexity notes]
- Data processing: [simple CRUD vs complex pipeline]

### API Availability Signals
- Candidate APIs: [names + doc links if found]
- "Build from scratch" risk: [any core capability without API support]

### SEO Potential Signals
- Observed problem keywords: [exact phrases users search]
- Competition notes: [existing solutions mentioned, saturation hints]
- Content moat opportunity: [can educational content drive traffic?]

### Competition Landscape Signals ⚠️ GATE
- Competitors mentioned: [names + user complaints]
- Differentiation angles: [simplicity, niche, pricing, UX]
- "Unwinnable" flags: [dominant incumbents, no clear gaps]

### Market Scale Signals ⚠️ GATE
- Community size/activity: [subscribers, posts per 6 months]
- Comparable success evidence: [indie revenue, public cases]
- Rough market math: [back-of-envelope TAM logic]

### Free Solution Check
- Free alternatives mentioned: [list with links]
- Disqualification risk: [High/Medium/Low — explain]
```

### Gaps & Next Steps

```markdown
## Gaps & Next Steps

### Data gaps
- [Areas not covered]

### Suggested follow-ups
- [Specific actionable next steps]

### Validation checklist
- [ ] Found in 3+ threads across different communities
- [ ] Users describe multiple failed solution attempts
- [ ] Evidence of existing spending (time or money)
- [ ] Recurring language present ("every time," "always")
- [ ] No perfect free solution in top comments
- [ ] Target users have budget authority (B2B) or strong motivation (B2C)
```

### Errors & Follow-ups

```markdown
## Errors & Follow-ups

- **Error description**: [if any]
- **Retry suggestion**: [if any]
- **Missing coverage**: [what this subtask failed to cover]
```
