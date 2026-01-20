# Reddit and Google Search Syntax

Complete syntax reference for generating executable search queries.

## Contents

- [Reddit native search](#reddit-native-search)
- [Google site search](#google-site-search)
- [Query templates](#query-templates)

---

## Reddit native search

> **WARNING: Reddit's native search is inconsistent and volatile.** As of 2026, Google Site Search is the **strongly preferred** method for reliability and depth. Use Reddit's native search only for specific tasks like sorting by "new" or searching comments, and anticipate potential failures or incomplete results. Do not build a critical dependency on its advanced features.

Reddit supports boolean operators and field filters. All operators are **case-sensitive**.

Note: This syntax applies to Reddit's own search (UI/URL/search.json). Do not assume MCP web search providers parse these operators.

### Boolean operators (must be uppercase)

| Operator | Function | Example |
|----------|----------|---------|
| `AND` | Both terms required | `Notion AND export` |
| `OR` | Either term matches | `alternative OR replacement` |
| `NOT` | Exclude term | `PDF NOT free` |
| `()` | Group operations | `(alternative OR replacement) AND Notion` |

**Important**: Use `NOT` instead of `-keyword`. The minus syntax is unreliable.

### Field filters

| Filter | Function | Example |
|--------|----------|---------|
| `title:` | Search only titles | `title:"alternative to"` |
| `selftext:` | Search post body | `selftext:"every time"` |
| `author:` | Filter by author | `author:username` |
| `subreddit:` | Limit to subreddit | `subreddit:accounting` |
| `flair:` | Filter by flair | `flair:"help"` |
| `url:` | Search link URLs | `url:github.com` |
| `site:` | Search link domains | `site:stripe.com` |
| `self:true` | Text posts only | `self:true` |
| `self:false` | Link posts only | `self:false` |

**Syntax rules**:
- No space between field name and colon: `title:keyword` ✓
- Space after colon breaks search: `title: keyword` ✗
- Use quotes for multi-word values: `title:"alternative to"` ✓

### Time filtering

Reddit native search doesn't support date operators in query syntax. Use URL parameters or UI controls instead:

**URL parameter method** (append to search URL):
| Parameter | Function | Example |
|-----------|----------|---------|
| `&t=day` | Past 24 hours | `?q=alternative&t=day` |
| `&t=week` | Past week | `?q=alternative&t=week` |
| `&t=month` | Past month | `?q=alternative&t=month` |
| `&t=year` | Past year | `?q=alternative&t=year` |
| `&t=all` | All time | `?q=alternative&t=all` |

**Default**: Always append `&t=year` to search URLs to filter for posts from the past year.

**Full URL example** (past year):
```
https://www.reddit.com/search/?q=subreddit%3Aaccounting%20alternative%20QuickBooks&t=year
```

**UI method**: Use the "Time" dropdown filter after executing search.

### Comment search

Reddit supports searching within comments. This is valuable for finding "free solution" evidence, as real feedback often appears in comments rather than original posts.

Access via: Reddit search → filter by "Comments"

### Score/Upvote filtering

Reddit native search does **NOT** support filtering by upvote count (score). There is no `score:` or `upvotes:` operator.

**Workarounds**:

| Method | How to use | Precision |
|--------|-----------|-----------|
| Sort by top | Append `&sort=top` to URL | Low (ranked, not filtered) |
| JSON API (High Risk) | Fetch `.json` endpoint, filter `score >= N` | High (but volatile) |
| Third-party | Use Redditsearch.io or Pullpush.io | High |

**Sort parameter options** (append to search URL):
| Parameter | Function |
|-----------|----------|
| `&sort=relevance` | Default, by relevance |
| `&sort=top` | By upvote count (descending) |
| `&sort=new` | By post time (newest first) |
| `&sort=comments` | By comment count (descending) |

**JSON API example (High-Risk / Volatile)**:
```
https://www.reddit.com/search.json?q=subreddit:accounting+QuickBooks&t=year&limit=100
```
Response includes `score` field for each post, enabling programmatic filtering. **Warning**: This endpoint is part of Reddit's API and may be restricted, changed, or deprecated without notice.

### Example queries (Reddit native)

```
subreddit:accounting ("alternative to" OR "replacement for") QuickBooks

subreddit:LawFirm ("can't trust AI" OR "human review") AND (draft OR contract)

title:"credits expire" AND (batch OR bulk) AND (tool OR app)

(self:true AND selftext:"every time") AND ("takes hours" OR tedious)

site:stripe.com AND subreddit:smallbusiness ("too expensive" OR "forced to upgrade")

subreddit:marketing Ahrefs ("alternative" OR "cheaper" OR "budget")
```

---

## Google site search

Google often returns better results than Reddit's native search, especially for long-tail queries. Google's indexing is more comprehensive and its syntax is more stable.

### Core operators

| Operator | Function | Example |
|----------|----------|---------|
| `site:` | Limit to domain | `site:reddit.com` |
| `"..."` | Exact phrase match | `"alternative to Notion"` |
| `OR` | Either term | `alternative OR replacement` |
| `-` | Exclude term | `-free` |
| `()` | Group terms | `(alternative OR replacement)` |
| `intitle:` | Search page titles | `intitle:alternative` |

**Syntax rules**:
- No space between operator and value: `site:reddit.com` ✓
- Quotes enforce exact phrase matching
- Combine operators freely

### Recommended Reddit URL constraints (Google site search)

- Posts only: `site:reddit.com inurl:/comments/ <terms>`
- Specific subreddit posts: `site:reddit.com inurl:/r/<sub>/comments/ <terms>`
- Specific subreddit (looser): `site:reddit.com/r/<sub>/ <terms>`
- Alternative discussion query: `intext:"reddit discussion" "alternative to [product]"`

### Adapting to Google SGE (Search Generative Experience)

By 2026, Google's results are often AI-generated summaries. This requires a new approach:
1.  **Seek Source Links**: Do not rely on the summarized text. Look for explicit source carousels, footnotes, or "More results" buttons to access the original Reddit thread.
2.  **Use `intext:` to force keyword presence**: Using `intext:"reddit"` can help ensure the term "reddit" appears in the raw text of the result, not just the URL.

### Time filtering

Google supports date-based filtering using `before:` and `after:` operators with `YYYY-MM-DD` format:

| Operator | Function | Example |
|----------|----------|---------|
| `after:` | Posts after date | `after:2025-07-03` |
| `before:` | Posts before date | `before:2026-01-01` |
| Combined | Date range | `after:2025-07-03 before:2026-01-01` |

**Default: 180 days (6 months)**

The search query **MUST** include a dynamic `after:YYYY-MM-DD` operator, calculated as 180 days prior to the current execution date.

**Agent Instruction**: The skill implementation must dynamically calculate the date for the `after:` operator (`today - 180 days`) before executing any Google search.

### Example queries (Google)

All examples include `after:[dynamic-date]` which must be calculated by the agent.

```
site:reddit.com "alternative to [product]" after:[dynamic-date]

site:reddit.com [product] "not worth it" after:[dynamic-date]

site:reddit.com "[X] vs [Y]" after:[dynamic-date]

site:reddit.com "switched from" [product] after:[dynamic-date]

site:reddit.com ([task] OR [job]) ("every time" OR constantly) tedious after:[dynamic-date]

site:reddit.com "credits expire" [product] after:[dynamic-date]

site:reddit.com inurl:/r/accounting/ "cheaper alternative to" QuickBooks after:[dynamic-date]

site:reddit.com intitle:"alternative to" [product] after:[dynamic-date]
```

**Concrete example** (assuming execution on 2026-01-02):
```
site:reddit.com "alternative to Notion" after:2025-07-06
```

---

## Query templates

Copy and customize these templates for common research objectives.

**Time filtering convention**:
- Reddit native queries: Append `&t=year` to URL (unreliable, use as fallback only).
- Google queries: The agent MUST add a dynamic `after:[date-180]` to every query.

### Discovery queries

**Find active pain points**:
```
site:reddit.com inurl:/r/[target]/ ("struggling with" OR "frustrated with" OR "hate when") [task] after:[dynamic-date]
```

**Find switching opportunities**:
```
site:reddit.com ("switching from" OR "alternative to" OR "replacement for") [product] after:[dynamic-date]
```

**Find pricing pain**:
```
site:reddit.com [product] ("too expensive" OR "not worth" OR "overpriced") after:[dynamic-date]
```

**Find automation opportunities**:
```
site:reddit.com inurl:/r/[target]/ ("spend hours on" OR "tedious" OR "repetitive") [task] after:[dynamic-date]
```

### Validation queries

**Check for recurring problems**:
```
site:reddit.com inurl:/r/[target]/ [problem] ("every time" OR "always" OR "constantly") after:[dynamic-date]
```

**Find existing spending**:
```
site:reddit.com inurl:/r/[target]/ ("paying for" OR "subscription to" OR "using [paid tool]") [task] after:[dynamic-date]
```

**Free solution test**:
```
site:reddit.com [pain point] ("just use" OR "try [free tool]" OR "open source") after:[dynamic-date]
```

### Competitive intelligence queries

**Find churn reasons**:
```
site:reddit.com ("stopped using" OR "gave up on" OR "cancelled") [product] after:[dynamic-date]
```

**Find feature gaps**:
```
site:reddit.com ("wish [product] had" OR "[product] doesn't have" OR "missing in [product]") after:[dynamic-date]
```

**Find UX complaints**:
```
site:reddit.com [product] ("confusing" OR "outdated UI" OR "clunky" OR "hard to use") after:[dynamic-date]
```

### Constraint-amplified queries (higher-value opportunities)

**Scale constraints**:
```
site:reddit.com inurl:/r/[target]/ ("bulk" OR "batch" OR "at scale") [task] ("every time" OR "tedious") after:[dynamic-date]
```

**Compliance constraints**:
```
site:reddit.com inurl:/r/[target]/ ("GDPR" OR "HIPAA" OR "SOC2" OR "audit trail") [task] after:[dynamic-date]
```

**Privacy constraints**:
```
site:reddit.com inurl:/r/[target]/ ("self-hosted" OR "on-prem" OR "offline" OR "no upload") [category] after:[dynamic-date]
```

---

## Platform selection guide

| Scenario | Recommended platform |
|----------|---------------------|
| **Primary Method** | **Google site:reddit.com** |
| Broad topic exploration | Google site:reddit.com |
| Specific subreddit deep-dive | Google `inurl:/r/<sub>/` |
| Long-tail multi-word queries | Google |
| Real-time/very recent posts | Reddit native (sort by new) |
| Comment-specific search | Reddit native |
| Absolute date range | Google (`after:` / `before:`) |
| Relative time filtering (fallback) | Reddit native (`&t=year`) |

**Best Practice: Syntax Verification**
Before running a large batch of queries, execute a single, simple test query (e.g., `site:reddit.com/r/accounting "tax" after:[dynamic-date]`) to ensure the search syntax is still valid and returning expected results. This acts as a canary test for platform changes.

**General rule**: Default to Google Search with a dynamic 180-day filter (`after:[dynamic-date]`) for all primary research.
