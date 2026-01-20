---
name: search-router
description: MCP search tool availability check and routing. Determines which search providers are available (Tavily, SerpApi, WebSearch) and provides configuration guidance. Use before executing web searches to ensure proper tool selection.
---

# Search Router

MCP tool availability check and routing for web search operations.

## Triggers

- Wide Research Phase 0 (reconnaissance)
- Any task requiring web search tool selection
- User asks about available search tools
- Reference to this skill directory

## Tool priority order

| Priority | Tool | Use case | Operators supported |
|----------|------|----------|---------------------|
| 1 | **SerpApi MCP** (Google engine) | Google site search, structured queries | `site:`, `inurl:`, `intitle:`, `after:`, `before:` |
| 2 | **Tavily MCP** | General web search, content extraction | Natural language queries |
| 3 | **WebSearch** (built-in) | Fallback only | Basic queries |
| ❌ | `curl`/`wget` | **NEVER USE** | — |

## Availability check protocol

Before executing web searches, verify tool availability:

```
1. Check if SerpApi MCP is available:
   - Try: serpapi.search with simple test query
   - If available: Use for all Google site searches

2. Check if Tavily MCP is available:
   - Try: tavily_search with simple test query
   - If available: Use for general searches

3. If BOTH unavailable:
   - STOP and report to user
   - Do not proceed with research
   - Provide clear error message about missing dependencies
```

## MCP unavailable handling

**Critical**: If both Tavily and SerpApi MCP are unavailable, the research workflow MUST stop.

```markdown
⚠️ **研究无法继续**

所需的 MCP 搜索工具不可用：
- Tavily MCP: 未检测到
- SerpApi MCP: 未检测到

**解决方案**：
1. 检查 MCP 服务器配置
2. 确认 API 密钥已正确设置
3. 重启 Claude Code 后重试

内置 WebSearch 工具不足以支持全面研究。
```

## Dynamic time filter (mandatory)

All Google site searches MUST include a dynamically calculated 180-day filter.

```python
from datetime import datetime, timedelta

# Calculate filter date (180 days ago)
filter_date = (datetime.now() - timedelta(days=180)).strftime('%Y-%m-%d')

# Construct query with filter
query = f'site:reddit.com "alternative to Notion" after:{filter_date}'
```

**Example** (execution date: 2026-01-04):
```
site:reddit.com "invoice management" after:2025-07-08
```

## Canary test (best practice)

Before running large query batches, execute a single test query:

```
# Canary test query
site:reddit.com/r/test "test" after:[dynamic-date]
```

If results are anomalous or empty, investigate platform changes before proceeding.

## Tool configuration

### SerpApi MCP

```yaml
serpapi.search:
  mode: "compact"          # Reduces response size
  params:
    engine: "google"       # Use Google engine
    q: "site:reddit.com inurl:/r/accounting/ QuickBooks after:2025-07-08"
    num: 10                # Results per page
```

**Supported operators**:
- `site:reddit.com` — Limit to domain
- `inurl:/r/<sub>/` — Specific subreddit
- `inurl:/comments/` — Posts only (not wiki, about pages)
- `intitle:` — Title contains term
- `after:YYYY-MM-DD` — Posts after date
- `before:YYYY-MM-DD` — Posts before date

### Tavily MCP

```yaml
tavily_search:
  query: "invoice management pain points site:reddit.com"
  max_results: 6           # Default, increase to 10 if insufficient
  search_depth: "advanced" # More thorough search
  include_images: false    # Usually not needed
  # Avoid include_raw_content to prevent oversized payloads
```

```yaml
tavily_extract:
  urls: ["https://reddit.com/r/accounting/comments/abc123"]
  format: "markdown"       # or "text"
  include_images: false
```

### WebSearch (built-in fallback)

```yaml
WebSearch:
  query: "site:reddit.com invoice management pain points 2025"
```

**Limitations**:
- Less reliable than MCP tools
- May have rate limits
- Use only as last resort

## Platform selection guide

| Scenario | Recommended tool |
|----------|-----------------|
| **Primary method** | SerpApi (Google engine) |
| Broad topic exploration | SerpApi or Tavily |
| Specific subreddit deep-dive | SerpApi with `inurl:/r/<sub>/` |
| Long-tail multi-word queries | SerpApi (Google) |
| Content extraction from URLs | Tavily Extract |
| Real-time/newest posts | Not recommended (Reddit native only) |
| Absolute date range | SerpApi with `after:`/`before:` |

## Search operator quick reference

### Google-style (SerpApi)

| Operator | Example | Notes |
|----------|---------|-------|
| `site:` | `site:reddit.com` | Domain restriction |
| `inurl:` | `inurl:/r/accounting/` | URL path contains |
| `intitle:` | `intitle:alternative` | Title contains |
| `after:` | `after:2025-07-08` | Posts after date |
| `before:` | `before:2026-01-01` | Posts before date |
| `"..."` | `"alternative to"` | Exact phrase |
| `OR` | `alternative OR replacement` | Either term |
| `-` | `-free` | Exclude term |

### Reddit URL constraints

- **Posts only**: `site:reddit.com inurl:/comments/ <terms>`
- **Specific subreddit posts**: `site:reddit.com inurl:/r/<sub>/comments/ <terms>`
- **Specific subreddit (loose)**: `site:reddit.com/r/<sub>/ <terms>`

## Caching strategy

Persist MCP raw responses to `raw/` directory for audit:

```
Write:
  file_path = "runs/.../raw/search-query-001.json"
  content = JSON.stringify(search_result)
```

Benefits:
- Reproducibility
- Debugging
- Cost optimization (avoid duplicate queries)

## Error handling

| Error | Cause | Action |
|-------|-------|--------|
| 403 Forbidden | Rate limited or blocked | Wait and retry with backoff |
| 429 Too Many Requests | Rate limit exceeded | Exponential backoff (2s → 4s → 8s) |
| Empty results | Query too specific | Broaden query terms |
| Timeout | Network or service issue | Retry once, then report |
| MCP not available | Configuration issue | Stop and report to user |
