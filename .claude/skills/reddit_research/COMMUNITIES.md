# Community Selection Guide

Mapping target users to appropriate Reddit communities for product research.

## Contents

- [B2B vs B2C selection](#b2b-vs-b2c-selection)
- [Community function types](#community-function-types)
- [Tool-specific communities](#tool-specific-communities)
- [Community selection framework](#community-selection-framework)
- [By industry vertical](#by-industry-vertical)
- [By user type](#by-user-type)
- [Builder communities (use carefully)](#builder-communities)

---

## B2B vs B2C selection

**Strongly prefer B2B for Micro-SaaS.** Solo founders and small teams have significant advantages in B2B markets.

### Strategic comparison

| Factor | B2B | B2C |
|--------|-----|-----|
| **Pricing logic** | Time = money ($50/hr saved = measurable ROI) | "Zero price anchor" (free apps everywhere) |
| **Conversion pattern** | 10 upvotes → possibly 5 paying customers | 1000 upvotes → possibly 0 conversions |
| **Churn rate** | Lower (embedded in workflows) | Higher (easy to switch) |
| **Sales cycle** | Longer but predictable | Impulse or never |
| **Support load** | Lower (professionals self-serve) | Higher (consumer expectations) |

### B2C warning signs

High Reddit engagement does NOT correlate with sales in B2C markets:
- Users complain about $2 apps while spending hours finding free alternatives
- Viral posts rarely convert to revenue
- "Great idea!" comments are worthless validation

### When B2C can work

- **Prosumer tools**: This is a critical and growing category. It includes freelancers, creators, developers, researchers, and solo business owners who use tools with professional intent. They often participate in B2C-style communities (like `r/selfhosted` or `r/youtubers`) but exhibit B2B buying behaviors: they are willing to pay for tools that save time, improve output quality, or provide data ownership and control.
- **Painful enough to pay**: Health, finance, education (high motivation)
- **No free alternative exists**: Rare but valuable niches

### Community tier classification
| Tier | Type | Validation standard | Examples |
|------|------|---------------------|----------|
| **Tier 1** | B2B Professional | 3K+ members, 5+ posts/6mo, 10+ comments avg | r/sysadmin, r/accounting, r/LawFirm |
| **Tier 2** | Prosumer / Vertical B2C | 10K+ members, 10+ posts/6mo, 20+ upvotes avg | r/freelance, r/GetStudying, r/homelab, r/selfhosted |
| **Tier 3** | Mass Consumer | 50K+ members, high volume needed | r/productivity, r/apps |
| **Tier 4** | Hyper-niche B2B | 1K+ members, quality over quantity | r/MSP, r/taxpros, r/restaurateur |

**Tier 1, Tier 2 (Prosumer), and Tier 4 are optimal for Micro-SaaS.** Tier 3 is extremely difficult without significant marketing budget.

### Empirical payment signal density (9300+ sample reference)

Based on analysis of 9,363 "I wish there was an app" posts, these communities showed highest payment signal density:

| Community | Pay signals | WPI estimate | Research notes |
|-----------|------------|--------------|----------------|
| r/personalfinance | 23 signals | High (~15) | Finance = highest WPI category overall |
| r/shopify | 17 signals | High (~10) | E-commerce tools = business expense |
| r/SaaS | 13 signals | Medium (~6) | ⚠️ Builder community, use for competitive intel |
| r/smallbusiness | 10 signals | High (~8) | Operational efficiency focus |
| r/ADHD | High detail | Quality focus | 📝 Most detailed feature requests, workflow-tool mismatch |

**Special note on r/ADHD**: While not highest in raw payment signals, this community provides the most detailed "feature requests" because current tools often fail neurodivergent workflows. Use for product specification research, then cross-validate payment willingness in Tier 1-2 communities.

### Category volume distribution (9300+ sample)

| Category | Request volume | Payment signal density | Opportunity assessment |
|----------|---------------|----------------------|------------------------|
| **Productivity** | 1,231 (highest) | Low | High noise, low conversion |
| **Education** | 698 | High willingness sentiment | Cross-validate with student budget constraints |
| **Business Tools** | 696 | Medium-high | "Glue" opportunities dominate |
| **Health & Wellness** | 656 | Medium | Seasonal (Jan peak) |

**Key insight**: Volume ≠ opportunity quality. Productivity has 2x the requests of Finance, but Finance has 3x the payment signals per post.

---

## Payment willingness tiers

Beyond market type, communities can be ranked by **expected payment willingness**. This framework helps prioritize where to invest research time.

### 💎 Tier 1: Entrepreneurs & Indie Developers (Highest willingness)

**Characteristics**:
- Actively seeking ROI tools
- Clear time-money value calculation
- Fast decision cycles (often same-day)
- Budget authority = themselves

**Example communities**:
| Community | Members | Why high willingness |
|-----------|---------|---------------------|
| r/Entrepreneur | 2M+ | Business-building mindset |
| r/SaaS | 100K+ | Already paying for software |
| r/startups | 1M+ | Investment in growth tools |
| r/smallbusiness | 800K+ | Operational efficiency focus |
| r/sweatystartup | 200K+ | Practical, bootstrapped mentality |

**Search priority**: ★★★★★

**Best signal phrases**: "worth the investment", "pays for itself", "ROI on", "saved us $X"

**Caveat**: Beware echo chamber effect in r/SaaS and r/startups—use for competitive intelligence, not primary demand research.

### 💼 Tier 2: Professional Service Providers (High willingness)

**Characteristics**:
- Tool costs can be passed to clients
- Efficiency directly impacts revenue
- Professional identity tied to output quality
- Tax-deductible business expenses

**Example communities**:
| Community | Members | Why high willingness |
|-----------|---------|---------------------|
| r/freelance | 600K+ | Time is literally money |
| r/agencies | 20K+ | Client billing covers tools |
| r/consulting | 50K+ | Premium positioning requires premium tools |
| r/web_design | 400K+ | Deliverable-focused |
| r/graphic_design | 3M+ | Mixed pro/hobbyist, filter for professionals |

**Search priority**: ★★★★☆

**Best signal phrases**: "bill clients for", "saves me hours per project", "worth it for client work", "professional workflow"

### 🎬 Tier 3: Professional Creators (Medium-high willingness)

**Characteristics**:
- Content monetization depends on tools
- Visible output quality matters
- Audience growth = revenue growth
- Higher price sensitivity than Tier 1-2

**Example communities**:
| Community | Members | Why medium-high willingness |
|-----------|---------|----------------------------|
| r/videography | 200K+ | Professional video production |
| r/podcasting | 300K+ | Monetized audio content |
| r/youtubers | 400K+ | Platform-dependent income |
| r/photography | 5M+ | Mixed pro/hobbyist, large pool |
| r/Twitch | 1M+ | Streamer tools and overlays |

**Search priority**: ★★★★☆

**Best signal phrases**: "invest in my channel", "worth it for content", "upgrade from free version", "professional quality"

**Caveat**: High hobbyist noise. Filter for: mentions of monetization, subscriber counts, "full-time creator".

### 📊 Tier 4: B2B Functional Roles (Medium willingness)

**Characteristics**:
- Have departmental budgets but require approval
- Longer decision cycles (weeks to months)
- Solutions must integrate with enterprise stack
- Often evaluating multiple options

**Example communities**:
| Community | Members | Why medium willingness |
|-----------|---------|----------------------|
| r/marketing | 1M+ | Marketing budget allocation |
| r/SEO | 300K+ | Performance-driven spend |
| r/ProductManagement | 200K+ | Tool stack decisions |
| r/sales | 100K+ | Productivity tools |
| r/CustomerSuccess | 20K+ | Retention tooling |

**Search priority**: ★★★☆☆

**Best signal phrases**: "got approval for", "team budget", "enterprise plan", "vendor comparison"

**Caveat**: Enterprise sales cycle may not suit solo founders. Focus on SMB-oriented discussions.

### 🏥 Tier 5: Industry Verticals (Variable willingness)

**Characteristics**:
- Payment willingness depends heavily on specific industry
- Often overlooked by large SaaS players
- Regulatory/compliance can create must-have needs
- Requires domain knowledge to evaluate

**Example communities**:
| Community | Members | Payment driver |
|-----------|---------|---------------|
| r/realtors | 50K+ | Commission-based income |
| r/Accounting | 300K+ | Compliance requirements |
| r/LawFirm | 30K+ | Billable hour efficiency |
| r/dentistry | 30K+ | Practice management |
| r/restaurateur | 20K+ | Margin optimization |

**Search priority**: ★★★☆☆ (Requires validation)

**Best signal phrases**: "required for compliance", "industry standard", "other [role] use", "worth it for practice"

**Caveat**: Must validate that Reddit is actually used by this vertical in your target geography.

### Payment tier summary

| Tier | Willingness | Decision speed | Budget source | Research priority |
|------|------------|----------------|--------------|-------------------|
| **1: Entrepreneurs** | ★★★★★ | Hours-days | Own pocket | First choice |
| **2: Service providers** | ★★★★☆ | Days-week | Business expense | Strong |
| **3: Creators** | ★★★★☆ | Days-weeks | Content revenue | Strong (filter for pros) |
| **4: B2B roles** | ★★★☆☆ | Weeks-months | Department budget | Moderate (SMB focus) |
| **5: Verticals** | ★★★☆☆ | Variable | Industry-dependent | Validate first |

**Strategic recommendation**: Start research in Tier 1-2 communities, then expand to Tier 3-5 for validation and market sizing.

---

## Community function types

Beyond industry classification, evaluate communities by **why they produce SaaS opportunities**:

| Function type | Why valuable | Identification signals | Examples |
|---------------|--------------|----------------------|----------|
| **Role/Job-based** | Clear work output, time = money, will pay for efficiency | Workflow bottlenecks, delivery pressure, compliance requirements | r/sysadmin, r/accounting, r/LawFirm, r/realtors |
| **Tool/Platform-based** | Plugin, integration, replacement opportunities | "Can't export", "API limits", "doesn't integrate with" | r/Salesforce, r/Notion, r/shopify, r/ObsidianMD |
| **Compliance-heavy** | Will pay for certainty and audit trails | "Stay compliant", "audit trail", "permissions", "will we get banned" | r/HIPAA, r/gdpr, r/MSP, r/FulfillmentByAmazon |
| **High-frequency output** | Has delivery KPIs, efficiency = income | "Workflow", "batch process", "template", "delivery deadline" | r/editors, r/podcasting, r/PPC, r/content_marketing |
| **Money Talk dense** | Already has payment mindset, discusses budgets openly | "Worth it?", "ROI", "budget for", "subscription cost" | r/smallbusiness, r/ecommerce, r/restaurateur |

### Prioritization rule

**Communities matching 2+ function types are ideal targets.**

Examples of high-value overlaps:
- r/accounting = Role-based + Compliance-heavy + Money Talk dense
- r/FulfillmentByAmazon = Tool-based (Amazon platform) + Compliance-heavy (policy changes) + Money Talk dense
- r/MSP = Role-based + Compliance-heavy (client audits) + Tool-based (RMM/PSA tools)

### Function-specific search strategies

| Function type | What to search for |
|---------------|--------------------|
| Role/Job-based | "every week", "spend hours on", "client deadline" |
| Tool/Platform-based | "alternative to", "integrate with", "export from", "API"|
| Compliance-heavy | "audit", "compliance", "GDPR", "will I get banned", "policy change" |
| High-frequency output | "batch", "automate", "template", "workflow", "turnaround time" |
| Money Talk dense | "worth it", "pricing", "budget", "ROI", "too expensive" |

---

## Tool-specific communities

Communities centered around specific software products. **High-value for finding plugin, integration, and replacement opportunities.**

### Why these communities matter

1. Users are **already paying** for the core product
2. Complaints = feature gaps you can fill
3. Clear **compatibility requirements** (must work with X)
4. **Switching discussions** reveal decision criteria

### Major platform communities

| Platform | Community | Opportunity type |
|----------|-----------|------------------|
| **CRM** | r/Salesforce, r/HubSpot, r/Pipedrive | Reporting, automation, data cleanup |
| **Project management** | r/Notion, r/asana, r/clickup, r/Monday | Templates, integrations, export tools |
| **Knowledge management** | r/ObsidianMD, r/RoamResearch, r/logseq | Plugins, sync tools, publishing |
| **E-commerce** | r/shopify, r/woocommerce, r/magento | Inventory sync, analytics, automation |
| **Accounting** | r/QuickBooks, r/Xero | Reconciliation, reporting, client portals |
| **Email/Marketing** | r/Mailchimp, r/ActiveCampaign | Migration tools, analytics, integrations |
| **Design** | r/figma, r/sketch, r/AdobeIllustrator | Asset management, handoff, automation |
| **Dev tools** | r/vscode, r/neovim, r/github | Extensions, workflow tools, CI/CD |

### Search patterns for tool communities

```
subreddit:[tool] ("doesn't have" OR "wish it had" OR "missing feature")
subreddit:[tool] ("integrate with" OR "connect to" OR "sync")
subreddit:[tool] ("alternative" OR "switching to" OR "moving away")
subreddit:[tool] ("export" OR "import" OR "migrate")
subreddit:[tool] ("workaround" OR "hack" OR "ugly fix")
```

---

## Community selection framework

### Step 1: Define target user

Answer these questions before selecting communities:
- What is their job title or role?
- What industry are they in?
- What task are they trying to accomplish?

### Step 2: Find where they discuss work (not where they discuss building products)

The key distinction:
- **Customer communities**: Discuss using tools to accomplish goals
- **Builder communities**: Discuss creating and selling tools

### Step 3: Perform Community Health Check

Before committing to a community, perform this mandatory protocol to avoid wasting time on dead or low-quality sources.

1.  **Check Activity**: Review the submission dates of the top 10-15 posts.
    *   **Pass**: Multiple posts within the last week.
    *   **Fail**: No posts in the last month. Flag as dormant.
2.  **Check Engagement**: Scan the comment counts of the top posts.
    *   **Pass**: Substantive discussions (e.g., >5 comments for niche B2B, >15 for broader communities) are common.
    *   **Fail**: Most posts have 0-2 comments. Flag as low-engagement.
3.  **Check Moderation Quality**: Look for signs of spam, off-topic content, or excessive self-promotion in the feed.
    *   **Pass**: Feed is focused on relevant topics.
    *   **Fail**: Feed is dominated by spam or marketing. Flag as poor quality.

Only proceed with communities that pass all three checks.

---

## By industry vertical

### Legal

| Community | Focus | Size indicator |
|-----------|-------|----------------|
| r/LawFirm | Practice management, tools, workflows | Active |
| r/lawyers | General legal discussion | Large |
| r/LegalAdviceOffTopic | Casual legal professional chat | Medium |

**Common pain points**: Document management, billing/time tracking, client communication, research tools, compliance

### Accounting and Finance

| Community | Focus | Size indicator |
|-----------|-------|----------------|
| r/Accounting | Professional accountants | Large |
| r/taxpros | Tax professionals | Active |
| r/Bookkeeping | Bookkeepers, small business finance | Medium |
| r/CPA | CPA-specific discussion | Medium |

**Common pain points**: Client portals, document collection, tax software limitations, reconciliation tools

### Healthcare

| Community | Focus | Size indicator |
|-----------|-------|----------------|
| r/medicine | Physicians and medical professionals | Large |
| r/Residency | Medical residents | Active |
| r/nursing | Nurses | Large |
| r/pharmacy | Pharmacists | Medium |
| r/dentistry | Dentists | Medium |

**Common pain points**: EHR frustrations, scheduling, patient communication, compliance/HIPAA tools

### Education

| Community | Focus | Size indicator |
|-----------|-------|----------------|
| r/Teachers | K-12 teachers | Large |
| r/education | Education professionals | Large |
| r/Professors | Higher education faculty | Medium |
| r/edtech | Educational technology | Medium |

**Common pain points**: Grading tools, plagiarism detection, student communication, LMS limitations

### Real Estate

| Community | Focus | Size indicator |
|-----------|-------|----------------|
| r/realtors | Real estate agents | Active |
| r/RealEstate | Real estate general | Large |
| r/CommercialRealEstate | Commercial RE professionals | Medium |

**Common pain points**: CRM, lead management, transaction coordination, marketing tools

### E-commerce

| Community | Focus | Size indicator |
|-----------|-------|----------------|
| r/ecommerce | General e-commerce | Large |
| r/FulfillmentByAmazon | Amazon sellers | Very active |
| r/dropship | Dropshipping | Active |
| r/Etsy | Etsy sellers | Active |
| r/shopify | Shopify users | Active |

**Common pain points**: Inventory management, product photography, listing optimization, shipping/fulfillment

---

## By user type

### Developers and Programmers

| Community | Focus |
|-----------|-------|
| r/programming | General programming |
| r/webdev | Web development |
| r/selfhosted | Self-hosting solutions |
| r/devops | DevOps and infrastructure |
| r/learnprogramming | Beginners |
| r/ExperiencedDevs | Senior developers |
| r/javascript | JavaScript ecosystem |
| r/python | Python ecosystem |
| r/reactjs | React development |

**Research note**: Developers express highly specific technical needs. Look for "I spend X hours doing Y" patterns.

### Designers

| Community | Focus |
|-----------|-------|
| r/design | General design |
| r/graphic_design | Graphic design |
| r/UI_Design | UI design |
| r/userexperience | UX design |
| r/web_design | Web design |
| r/logodesign | Logo design |
| r/typography | Typography |

**Research note**: Designers frequently discuss workflow efficiency and tool integrations. "What tools do you use?" threads reveal satisfaction levels.

### Marketers

| Community | Focus |
|-----------|-------|
| r/marketing | General marketing |
| r/SEO | Search engine optimization |
| r/PPC | Paid advertising |
| r/content_marketing | Content marketing |
| r/digital_marketing | Digital marketing |
| r/bigseo | Advanced SEO |
| r/analytics | Analytics |
| r/socialmedia | Social media marketing |

**Research note**: Marketers vocally complain about premium tool pricing (Semrush, Ahrefs). "Alternative to [premium tool]" searches are extremely common.

### AI Professionals

| Community | Focus |
|-----------|-------|
| r/LocalLLaMA | Local/private large language models |
| r/StableDiffusion | AI image generation |
| r/PromptEngineering | Crafting and optimizing AI prompts |
| r/aipromptprogramming | Technical prompt-based development |
| r/Singularity | High-level discussion of AI's future |

**Research note**: This vertical has highly technical pain points around model management, fine-tuning, data privacy, output validation, and GPU resource management. Users value control and data ownership.

### Creator Economy

| Community | Focus |
|-----------|-------|
| r/youtubers | YouTube creators |
| r/podcasting | Podcasters and audio creators |
| r/VideoEditing | Video editing workflows |
| r/streaming | Live streamers (Twitch, YouTube) |
| r/virtualyoutubers | VTubers and avatar-based creators |

**Research note**: Pain points have evolved beyond basic editing. Look for discussions on content repurposing (e.g., "long-form to shorts"), audience analytics, sponsorship management, and complex media asset workflows.

### Students and Academics

| Community | Focus |
|-----------|-------|
| r/GetStudying | Study techniques |
| r/studytips | Study tips |
| r/college | College students |
| r/GradSchool | Graduate students |
| r/AskAcademia | Academic career |
| r/medicalschool | Medical students |
| r/lawschool | Law students |

**Research note**: Students have severe budget constraints but clear recurring needs. Tools addressing study efficiency have viral potential through campus word-of-mouth.

### Freelancers and Solopreneurs

| Community | Focus |
|-----------|-------|
| r/freelance | General freelancing |
| r/digitalnomad | Digital nomads |
| r/forhire | Job seeking/offering |
| r/freelanceWriters | Freelance writers |
| r/sidehustle | Side businesses |

**Research note**: Freelancers willingly pay for tools that save admin time. Pain points around non-paying clients, scope management, and tax complexity are common.

### Small Business Owners

| Community | Focus |
|-----------|-------|
| r/smallbusiness | General small business |
| r/restaurateur | Restaurant owners |
| r/retail | Retail business |

**Research note**: Small business owners value tools that consolidate functions and reduce overhead. They're practical buyers focused on ROI.

---

## Builder communities

**These are NOT for primary demand research. Use only for competitive intelligence.**

| Community | Use for |
|-----------|---------|
| r/SaaS | What products are saturated, pricing strategies |
| r/Entrepreneur | Launch tactics, what others are building |
| r/startups | Market trends, funding landscape |
| r/microsaas | Indie SaaS patterns, revenue benchmarks |
| r/SideProject | Technical implementation, solo founder tactics |
| r/indiehackers | Growth tactics, validation approaches |

**Valid use cases for builder communities**:
- Competitive intelligence (what others are building)
- Identifying saturated markets
- Learning from launch post-mortems
- Go-to-market tactics
- Pricing feedback

**Invalid use cases**:
- Discovering customer pain points
- Validating demand for your product idea
- Understanding what users actually want

### How to identify builder vs customer community

**Builder community signals**:
- "How do I validate my SaaS idea"
- "What's your MRR"
- "How did you get your first 100 users"
- "Looking for co-founder"

**Customer community signals**:
- "This tool keeps crashing when I try to export"
- "Why is there no app that does X"
- "What do you use for [specific task]"
- Complaints about specific workflow friction
