# Sales Agents

This document catalogs AI agents and skills focused on sales tasks including lead generation, prospect research, lead qualification, outreach, CRM automation, and pipeline management.

## Top Agent Systems

### AI Sales Team Claude

**Repository**: https://github.com/zubair-trabzada/ai-sales-team-claude
**Skills**: 14 skills, 5 agents, 4 scripts, PDF generation

**Description**: AI-powered sales team for Claude Code. Research prospects, qualify leads (BANT + MEDDIC), find decision makers, generate outreach sequences, prepare meetings, write proposals, produce PDF pipeline reports.

**Architecture**: Three-layer system
1. **Orchestrator** - Routes commands to sub-skills
2. **5 Parallel Sub-agents** - Execute in parallel
3. **13 Sub-skills** - Specialized sales tasks

**Skills**:
| Skill | Description |
|-------|-------------|
| sales-prospect | Full prospect audit (launches 5 agents) |
| sales-research | Company research & firmographics |
| sales-qualify | Lead qualification (BANT + MEDDIC) |
| sales-contacts | Decision maker identification |
| sales-outreach | Cold outreach email sequences |
| sales-prep | Meeting preparation brief |
| sales-proposal | Client proposal generator |
| sales-objections | Objection handling playbook |
| sales-icp | Ideal Customer Profile builder |
| sales-competitors | Competitive intelligence |
| sales-report | Pipeline report (Markdown) |
| sales-report-pdf | Pipeline report (PDF) |

**Usage**:
```bash
/sales prospect https://target.com
/sales qualify https://lead.com
/sales icp
```

---

### SalesGPT

**Repository**: https://github.com/filip-michalsky/SalesGPT
**Stars**: (original) | **License**: MIT

**Description**: Context-aware AI Sales Agent to automate sales outreach. Works across voice, email, texting (SMS, WhatsApp, WeChat, etc.).

**Key Capabilities**:
- **Sales Stage Awareness**: Understands conversation stage and acts accordingly
  - Introduction, Qualification, Value Proposition, Demo, Proposal, Close
- **Product Knowledge**: References business info to reduce hallucinations
- **Close Sales**: Generates Stripe payment links

**Tech Stack**:
- LangChain for agent orchestration
- LiteLLM for multi-model support
- Twilio integration for voice/SMS

---

### AI CRM Agents

**Repository**: https://github.com/KlementMultiverse/ai-crm-agents
**Stars**: 28

**Description**: Production-ready AI-powered CRM with 6 autonomous agents for lead qualification, email intelligence, sales pipeline, customer success, meeting scheduling, and analytics.

**6 Autonomous Agents**:

| Agent | Function |
|-------|----------|
| Lead Qualification Agent | Score and qualify leads |
| Email Intelligence Agent | Sentiment analysis, response drafting |
| Sales Pipeline Agent | Deal tracking, forecast |
| Customer Success Agent | Retention, upsell |
| Meeting Scheduler | Calendar coordination |
| Analytics Agent | Reports, insights |

**Tech Stack**: Python, FastAPI, PostgreSQL, Redis, Celery, LangChain, Claude/GPT-4

---

### GTM Skills (Sales & RevOps)

**Repository**: https://github.com/gtm-skills/gtm
**Prompts**: 300+

**Description**: The Open-Source Operating System for Agentic GTM. Comprehensive prompts for sales methodologies, workflows, and RevOps.

**Sales Methodologies**:
- MEDDPICC
- SPIN
- Challenger
- Gap Selling
- Value Selling
- Sandler

**MCP Server Tools**:
- `research_company` - Company research
- `research_lead` - Lead research
- `draft_cold_email` - Personalized emails
- `handle_objection` - Strategic responses
- `generate_cold_call_script` - Call scripts
- `generate_discovery_questions` - SPIN/MEDDPICC questions
- `account_strategy` - Full account strategy

---

### Radiant AI CRM

**Repository**: https://github.com/dylanmeyford/radiant-ai-crm-oss

**Description**: Open-source AI CRM that works autonomously in the background—analysing pipeline, drafting next moves, keeping deals moving forward.

**Key Features**:
- AI-first CRM with agentic behavior
- Stripe subscriptions (revenue-ready)
- Nylas email/calendar integration
- Full-stack TypeScript monorepo
- Eval framework included

**Tech Stack**: TypeScript, Express, MongoDB, Stripe, Nylas, OpenAI

---

### NexusAI Agentic Sales CRM

**Repository**: https://github.com/MDalamin5/NexusAI-Agentic-Sales-Campaign-CRM

**Description**: Autonomous Agentic CRM powered by LangGraph. Multi-agent workflows for lead scoring, persona enrichment, personalized outreach.

**6 Specialized Agents**:
1. Lead Scorer & Prioritizer (1-10 scoring)
2. Persona Enricher Agent
3. Outreach Drafter Agent
4. Email Sender Agent
5. Response Categorizer
6. Campaign Summarizer

**Tech Stack**: LangGraph, LangChain, Groq/OpenAI, FastAPI, Docker

---

## Sales Skills by Category

### Research & Intelligence

| Skill | Description |
|-------|-------------|
| company-research | Firmographics, news, digital presence |
| lead-research | Contact info, LinkedIn analysis |
| competitive-intelligence | Competitor analysis, positioning |
| icp-builder | Ideal customer profile definition |

### Qualification

| Skill | Description |
|-------|-------------|
| bant-qualification | Budget, Authority, Need, Timeline |
| meddic-qualification | Metrics, Economic buyer, Decision criteria, Identity, Champion |
| lead-scoring | Fit scoring, intent signals |

### Outreach

| Skill | Description |
|-------|-------------|
| cold-email | Personalized outreach sequences |
| cold-call-script | Phone script generation |
| linkedin-outreach | Social selling |
| video-outreach | Personalized video creation |

### Pipeline Management

| Skill | Description |
|-------|-------------|
| deal-tracking | Pipeline visibility |
| forecast-automation | Revenue prediction |
| activity-logging | Call/email logging |
| pipeline-reporting | Visual reports, PDF exports |

### Meeting & Close

| Skill | Description |
|-------|-------------|
| meeting-prep | Discovery call preparation |
| discovery-questions | SPIN/MEDDICC questioning |
| proposal-generation | Formal proposals |
| objection-handling | Common objection responses |
| negotiation-playbook | Deal closing strategies |

---

## Technical Patterns

### Lead Qualification Flow

```
New Lead → Data Enrichment → Scoring → Routing → Auto-Email → CRM Entry
```

### Multi-Agent Sales Architecture

```python
# LangGraph orchestration
graph = StateGraph(SalesState)
graph.add_node("research", research_agent)
graph.add_node("qualify", qualify_agent)
graph.add_node("enrich", enrich_agent)
graph.add_node("outreach", outreach_agent)
graph.add_edge("research", "qualify")
graph.add_edge("qualify", "enrich")
graph.add_edge("enrich", "outreach")
```

### CRM Integration Patterns

| CRM | Integration Method |
|-----|-------------------|
| HubSpot | API, Webhooks |
| Airtable | API |
| Google Sheets | API |
| Notion | MCP Protocol |
| Custom | REST API |

---

## Cost & ROI Metrics

| Solution | Est. Cost | Key Benefit |
|----------|-----------|--------------|
| SalesGPT | API costs | Stage-aware conversations |
| AI CRM Agents | $0.02-0.05/lead | Full automation |
| GTM Skills | Free (prompts) | Methodology-driven |
| Radiant | Self-hosted | No per-seat pricing |
| NexusAI | Docker deployment | LangGraph workflow |

---

## References

- AI Sales Team: https://github.com/zubair-trabzada/ai-sales-team-claude
- SalesGPT: https://github.com/filip-michalsky/SalesGPT
- AI CRM Agents: https://github.com/KlementMultiverse/ai-crm-agents
- GTM Skills: https://github.com/gtm-skills/gtm
- Radiant CRM: https://github.com/dylanmeyford/radiant-ai-crm-oss
- NexusAI: https://github.com/MDalamin5/NexusAI-Agentic-Sales-Campaign-CRM