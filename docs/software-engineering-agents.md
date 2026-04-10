# Software Engineering Agents

This document catalogs AI agents focused on software engineering tasks, including code generation, debugging, code review, and developer workflow automation.

## Top Agents

### SWE-agent

**Repository**: https://github.com/swe-agent/swe-agent
**Stars**: 18,958
**Primary Language**: Python

**Description**: SWE-agent takes a GitHub issue and tries to automatically fix it using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges.

**Key Capabilities**:
- Autonomous issue fixing
- Cybersecurity vulnerability detection
- State-of-the-art on SWE-bench benchmark
- Configurable via single YAML file
- Supports multiple LLM providers

**Architecture**:
- Agent-Computer Interfaces (ACI) for tool use
- Configurable tools and environment
- Trajectory-based learning support

---

### mini-swe-agent

**Repository**: https://github.com/SWE-agent/mini-swe-agent
**Stars**: 3,615
**Primary Language**: Python

**Description**: The 100-line AI agent that solves GitHub issues or helps you in your command line. Radically simple, no huge configs, but scores >74% on SWE-bench verified.

**Key Capabilities**:
- Minimal implementation (~100 lines)
- High benchmark performance
- Local environment support
- Docker/Podman deployment
- Multi-model support via litellm

**Adopted by**: Meta, NVIDIA, IBM, Essential AI, Stanford, Princeton

---

### Docker Agent

**Repository**: https://github.com/docker/cagent
**Stars**: 2,786
**Primary Language**: Go

**Description**: AI Agent Builder and Runtime by Docker Engineering. Build, run, and share AI agents with a declarative YAML config.

**Key Capabilities**:
- Multi-agent architecture
- Rich tool ecosystem + MCP servers
- AI provider agnostic (OpenAI, Anthropic, Gemini, etc.)
- YAML-based configuration
- RAG with BM25, embeddings, hybrid search
- OCI registry push/pull

**Key Features**:
- Declarative agent definition
- Advanced reasoning (think, todo, memory tools)
- Package & share agents

---

### OpenAI Codex

**Repository**: https://github.com/openai/codex
**Releases**: 683

**Description**: Lightweight coding agent that runs in your terminal. Also available in IDEs (VS Code, Cursor, Windsurf).

**Key Capabilities**:
- CLI-based coding agent
- Full software engineering pipeline
- Agent Skills support (reusable expertise bundles)
- Multi-language SDK (Node.js, Python)

**Agent Skills Architecture**:
- `SKILL.md` containing instructions and metadata
- `scripts/` directory with optional executable code
- Built-in skills inspired by popular workflows

---

### GitHub Copilot

**Documentation**: https://docs.github.com/en/copilot

**Key Capabilities**:
- Agent mode for autonomous iteration
- Custom agents for specialized tasks
- Agent skills for repeatable workflows
- MCP tool integration
- Repository-specific memory

**Agent Skills Locations**:
- `.github/skills/` - Project skills
- `~/.copilot/skills/` - Personal skills
- Organization/enterprise skills (coming soon)

---

### Docker Agent (cagent)

**Key Features**:
- Multi-agent orchestration
- Declarative YAML configuration
- MCP server integration
- RAG capabilities
- Built-in tools: think, todo, memory

---

## Agent Capabilities Matrix

| Capability | SWE-agent | mini-swe-agent | Docker Agent | Codex | Copilot |
|------------|-----------|----------------|--------------|-------|---------|
| Issue Fixing | ✅ | ✅ | ❌ | ✅ | ✅ |
| Code Review | ❌ | ❌ | ❌ | ✅ | ✅ |
| Multi-Agent | ❌ | ❌ | ✅ | ❌ | ✅ |
| YAML Config | ✅ | ❌ | ✅ | ❌ | ❌ |
| Local Deploy | ✅ | ✅ | ✅ | ✅ | ❌ |
| MCP Support | ❌ | ❌ | ✅ | ❌ | ✅ |
| RAG | ❌ | ❌ | ✅ | ❌ | ✅ |
| Custom Skills | ❌ | ❌ | ❌ | ✅ | ✅ |

---

## Technical Patterns

### Agent-Computer Interfaces (ACI)

From SWE-agent research - optimal interface design for AI agents:
1. Name functions clearly (e.g., `git_commit` not `git`)
2. Single action per function
3. Return all relevant information in structured format

### Agent Skills Specification

Standard skill structure used across platforms:

```
skill-name/
├── SKILL.md          # Instructions + metadata
├── scripts/          # Executable code (optional)
└── examples/         # Example prompts/outputs
```

### Multi-Agent Orchestration

Common patterns:
- **Hierarchical**: Director → Specialist agents
- **Parallel**: Multiple agents work simultaneously
- **Sequential**: Pass results between agents
- **Swarm**: Dynamic agent allocation

---

## References

- SWE-agent Paper: https://arxiv.org/abs/2405.15793
- GitHub Agent Skills: https://docs.github.com/copilot/concepts/agents/about-agent-skills
- OpenAI Codex: https://github.com/openai/codex
- Docker Agent: https://github.com/docker/cagent