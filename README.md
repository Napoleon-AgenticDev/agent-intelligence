# Agent Intelligence Repository

A comprehensive collection of AI agents and skills for software engineering, marketing, video production, sales, and business onboarding.

## Overview

This repository aggregates capabilities, attributes, and characteristics from open-source AI agents and skills found across GitHub. The focus areas include:

- **Software Engineering**: Code generation, debugging, code review, documentation
- **Marketing**: Content creation, SEO, paid ads, analytics, email automation
- **Video Production**: Script generation, video editing, voice-over, publishing
- **Sales**: Lead generation, prospect research, outreach, CRM automation
- **Business Onboarding**: Employee onboarding, client onboarding, workflow automation

## Repository Structure

```
agent-intelligence-repo/
├── README.md
├── docs/
│   ├── software-engineering-agents.md
│   ├── marketing-agents.md
│   ├── video-production-agents.md
│   ├── sales-agents.md
│   └── onboarding-agents.md
├── skills/
│   ├── engineering/
│   ├── marketing/
│   ├── video/
│   ├── sales/
│   └── onboarding/
└── agents/
    ├── engineering-agents.json
    ├── marketing-agents.json
    ├── video-agents.json
    ├── sales-agents.json
    └── onboarding-agents.json
```

## Categories

### Software Engineering Agents

| Agent | Description | Stars | Key Capabilities |
|-------|-------------|-------|------------------|
| SWE-agent | Autonomous GitHub issue fixer | 18.9k | Code fixing, cybersecurity, benchmark testing |
| mini-swe-agent | Minimal 100-line coding agent | 3.6k | CLI tool, local execution, high benchmark scores |
| Docker Agent | Declarative YAML AI agent builder | 2.8k | Multi-agent, MCP tools, RAG support |
| OpenAI Codex | Terminal-based coding agent | - | Full software engineering pipeline |
| GitHub Copilot | IDE coding assistant | - | Agent mode, custom agents, skill loading |

### Marketing Agents

| Agent/Skill Pack | Description | Skills Count |
|------------------|-------------|--------------|
| Claude Marketing | Full marketing department for Claude Code | 56 skills |
| AdClaw | Multi-agent AI marketing team | 118 skills |
| Marketing Skills (Corey Haines) | SaaS marketing stack | 20+ skills |
| GTM Skills | GTM toolkit for AI agents | 300+ prompts |
| Opensoul | Agentic marketing stack | 6 roles |

### Video Production Agents

| Agent | Description | Capabilities |
|-------|-------------|--------------|
| AgentCut | Multi-agent video pipeline | 6 agents, parallel execution |
| OpenMontage | Agentic video production | 11 pipelines, 49 tools, 400+ skills |
| AITuber Skill | AI video creation | YouTube, TikTok, Instagram automation |
| VideoDB Skills | Server-side video workflows | Ingest, understand, search, edit, stream |

### Sales Agents

| Agent | Description | Capabilities |
|-------|-------------|--------------|
| AI Sales Team Claude | AI-powered sales team | 14 skills, 5 agents, PDF reports |
| SalesGPT | Context-aware sales agent | Stage awareness, Stripe integration |
| AI CRM Agents | AI-powered CRM | 6 autonomous agents |
| GTM Skills | Sales & RevOps prompts | 300+ methodologies |

### Onboarding Agents

| Solution | Description | Capabilities |
|----------|-------------|--------------|
| HR Onboarding Agents | Automated employee onboarding | Tool provisioning, training assignment |
| Client Onboarding | AI-powered client onboarding | Compliance, KYC, workflow orchestration |
| Repository Onboarding | Codebase onboarding | Environment setup, documentation generation |

## Key Findings

### Agent Architecture Patterns

1. **Multi-Agent Orchestration**: Teams of specialized agents with delegation
2. **Skill-Based Systems**: Modular, reusable skill packs that load on demand
3. **Pipeline Execution**: Sequential/parallel workflows for complex tasks
4. **Memory & Context**: Persistent context across sessions

### Skill Specification Standards

- `.github/skills/` - GitHub Copilot skills
- `.claude/skills/` - Claude Code skills
- `.agents/skills/` - General agent skills
- `SKILL.md` - Skill definition files with instructions, metadata, examples

### Common Capabilities

- RAG (Retrieval-Augmented Generation) for knowledge access
- MCP (Model Context Protocol) for tool integration
- Multi-model support (OpenAI, Anthropic, Google, local models)
- API integrations for external services

## References

- [SWE-agent](https://github.com/swe-agent/swe-agent)
- [Claude Marketing](https://github.com/thatrebeccarae/claude-marketing)
- [GTM Skills](https://github.com/gtm-skills/gtm)
- [AdClaw](https://github.com/Citedy/adclaw)
- [Opensoul](https://github.com/iamevandrake/opensoul)
- [AgentCut](https://github.com/calderbuild/agentcut)
- [OpenMontage](https://github.com/calesthio/OpenMontage)
- [AI Sales Team](https://github.com/zubair-trabzada/ai-sales-team-claude)

### Ruflo (buildmotion/ruflo)

100+ specialized agent skills for enterprise AI workflows:

| Category | Agents |
|----------|--------|
| **Coordinators** | swarm, hierarchical, mesh, ring, star, consensus, raft, gossip |
| **Development** | coder, code-analyzer, reviewer, tester, sandbox, refiner |
| **Operations** | cicd-github, release-manager, security-manager, performance-analyzer |
| **Data/ML** | data-ml-model, neural-network, pagerank-analyzer |
| **Architecture** | architecture, specification, repo-architect, system-design |

[Browse all ruflo skills](https://github.com/buildmotion/ruflo/tree/main/.agents/skills)

## License

MIT License - See individual repositories for their respective licenses.