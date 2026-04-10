# Marketing Agents

This document catalogs AI agents and skills focused on marketing tasks including content creation, SEO, paid ads, email automation, analytics, and growth engineering.

## Top Agent Systems

### Claude Marketing

**Repository**: https://github.com/thatrebeccarae/claude-marketing
**Stars**: -
**Skills**: 56 open-source skills

**Description**: A full marketing department for Claude Code. Skill packs for Klaviyo, Shopify, GA4, Looker Studio, paid media, and more.

**Categories**:
| Category | Skills Count |
|----------|--------------|
| Paid Media | Platform-specific ad skills |
| E-commerce | Shopify optimization |
| Content | Copywriting, strategy |
| SEO | Technical and on-page |
| Analytics | GA4, measurement |
| Strategy | Frameworks, planning |

**Multi-Tool Support**: Works with Claude Code, Cursor, Aider, Windsurf, GitHub Copilot, Gemini CLI

---

### AdClaw

**Repository**: https://github.com/Citedy/adclaw
**Skills**: 118 built-in skills

**Description**: Multi-agent AI marketing team powered by Citedy. Fork of CoPaw by AgentScope.

**Key Features**:
- Multi-agent personas with custom identities
- 118 built-in skills (SEO, ads, content, social media, analytics)
- 52 marketing tools via Citedy MCP server
- 23 LLM providers, 100+ models
- Self-healing skills (auto-fix broken YAML)
- Security scanning (208-pattern static analysis)

**Pre-installed Skills**:
- citedy-seo-agent: Full-stack SEO with 52 tools
- citedy-trend-scout: X/Twitter and Reddit trend scouting
- citedy-video-shorts: AI UGC short-form videos
- skill-creator: Custom skill creation

---

### Marketing Skills (Corey Haines)

**Repository**: https://github.com/coreyhaines31/marketingskills
**Author**: Corey Haines

**Skill Categories**:

**Conversion Optimization**:
- `page-cro` - Marketing pages
- `signup-flow-cro` - Registration flows
- `onboarding-cro` - Post-signup activation

**Content & Copy**:
- `copywriting` - Marketing page copy
- `copy-editing` - Edit existing copy

**SEO**:
- `seo-audit` - Technical and on-page SEO
- `ai-seo` - AI search optimization (AEO, GEO, LLMO)

**Growth Engineering**:
- `free-tool-strategy` - Marketing tools and calculators
- `referral-program` - Referral and affiliate programs

**Measurement**:
- `analytics-tracking` - Event tracking setup
- `ab-test-setup` - Experiment design

---

### Opensoul

**Repository**: https://github.com/iamevandrake/opensoul

**Description**: Open-source agentic marketing stack. Pre-configured Paperclip deployment for marketing agencies.

**Marketing Team Roles**:

| Role | Responsibility |
|------|----------------|
| Director | Overall strategy, budget, coordination |
| Strategist | Market research, competitive analysis |
| Creative | Content creation, campaigns |
| Producer | Video, social media production |
| Growth | SEO, paid acquisition, CRO |
| Analyst | Analytics, reporting |

**Features**:
- Autonomous execution on scheduled heartbeats
- Goal-driven campaigns
- Budget control per agent
- Multi-channel coordination
- Phone-accessible management

---

### GTM Skills

**Repository**: https://github.com/gtm-skills/gtm

**Description**: The Open-Source Operating System for Agentic GTM. Prompts, workflows, MCP server for AI sales and marketing.

**Content**:
- 300+ sales methodologies
- Role-based playbooks (SDR, AE, Manager, RevOps, CSM)
- Industry-specific prompts (SaaS, FinTech, Healthcare)
- End-to-end workflows (Cold-to-Close, Discovery, Expansion)

**MCP Server Tools**:
- `research_company` - Company research
- `research_lead` - Lead research
- `draft_cold_email` - Personalized email drafts
- `handle_objection` - Strategic objection responses
- `generate_cold_call_script` - Cold call scripts

---

### Agent GTM Skills

**Repository**: https://github.com/chadboyda/agent-gtm-skills
**Lines**: 9,800+ lines

**Description**: 18 AI agent skills for go-to-market. Turn any coding agent into a GTM operator.

**Skill Structure**:
```
STRATEGY      - positioning, pricing, sales motion
OUTBOUND      - cold outreach, SDR, lead enrichment
INBOUND       - content, SEO, paid channels
RETAENTION    - expansion, partner programs
OPERATIONS    - gtm engineering, metrics
```

**Strategy Skills**:
- positioning-icp: ICP definition with enrichment signals
- ai-pricing: Consumption/workflow/outcome pricing
- sales-motion-design: PLG vs sales-led selection

---

## Marketing Skills by Category

### Content & Creative

| Skill | Description |
|-------|-------------|
| content-marketing | Content strategy, copywriting |
| copywriting | Landing page and ad copy |
| social-content | Social media scheduling |
| video-marketing | Video strategy, YouTube SEO |
| video-automation | Automated marketing via Remotion |

### Growth & Acquisition

| Skill | Description |
|-------|-------------|
| growth-hacking | Viral loops, AARRR framework |
| ppc-advertising | Google Ads, Meta Ads |
| lead-gen-scraper | Lead generation, prospect research |
| referral-program | Referral and affiliate programs |

### SEO & Analytics

| Skill | Description |
|-------|-------------|
| seo-fundamentals | SEO best practices, E-E-A-T |
| seo-audit | Technical and on-page audit |
| ai-seo | AI search optimization |
| analytics-marketing | KPIs, attribution, GA4 |
| conversion-optimization | CRO, A/B testing |

### Email & Automation

| Skill | Description |
|-------|-------------|
| email-sequence | Drip campaigns |
| analytics-tracking | Event tracking |
| marketing-automation | Lead nurturing, workflows |
| n8n-automation | n8n workflow building |

---

## Technical Patterns

### Skill Installation Methods

```bash
# npm skills
npx skills add coreyhaines31/marketingskills

# Claude Code plugin
/plugin marketplace add chadboyda/agent-gtm-skills
/plugin install agent-gtm-skills

# Clone directly
git clone https://github.com/coreyhaines31/marketingskills.git
cp -r marketingskills/skills/* .agents/skills/
```

### Multi-Agent Marketing Architecture

```
User → Director → Strategist → Creative/Growth/Producer
                     ↓
              Shared Knowledge Base
                     ↓
              Analytics & Reporting
```

### Knowledge Base Structure

Common marketing knowledge base includes:
- `unit-economics.md` - CPA/ROAS formulas, LTV calculations
- `industry-verticals.md` - Vertical-specific playbooks
- `channel-tactics.md` - Platform-specific strategies
- `measurement-frameworks.md` - Attribution models

---

## References

- Claude Marketing: https://github.com/thatrebeccarae/claude-marketing
- AdClaw: https://github.com/Citedy/adclaw
- Marketing Skills: https://github.com/coreyhaines31/marketingskills
- Opensoul: https://github.com/iamevandrake/opensoul
- GTM Skills: https://github.com/gtm-skills/gtm
- Agent GTM Skills: https://github.com/chadboyda/agent-gtm-skills