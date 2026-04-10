# Onboarding Agents

This document catalogs AI agents and systems focused on business onboarding, including employee onboarding, client onboarding, and startup workflow automation.

## Top Systems

### HR Onboarding Agents

**Key Capabilities**:
- **Checklist Generation**: Personalized by role (engineer, designer, sales)
- **Tool Provisioning**: Automatic account creation in Slack, Google Workspace, GitHub, Notion
- **Training Assignment**: Enroll in courses, schedule 1:1s
- **Progress Tracking**: Monitor completion, send reminders

**Typical Workflow**:
```
Trigger: New hire added to HRIS with start date
    ↓
Generate checklist based on role template
    ↓
Provision tools: Create accounts, add to groups
    ↓
Assign training: Send Loom links, enroll in courses
    ↓
Schedule: 1:1s, team introductions
    ↓
Track: Monitor completion, nudge overdue
```

**Real Example: Deel**
- 12 tools auto-provisioned within 10 minutes of hire acceptance
- Reduced time-to-productivity from 18 days to 11 days

---

### Client Onboarding Agents

**Key Capabilities**:
- **Compliance Automation**: KYC data validation, document collection
- **Workflow Orchestration**: Multi-step onboarding journey
- **Personalization**: Tailored welcome videos, task sequences
- **Escalation**: Human handoff when needed

**Key Stats**:
- 74% of customers switch providers after poor onboarding
- AI agents reduce onboarding from 10 days to <48 hours
- 37.5% B2B SaaS users reach activation (62.5% drop-off)

**Tech Approach**:
- RAG + Knowledge Graph (80% hallucination reduction vs standard chatbots)
- Audit-ready knowledge flows

---

### Repository Onboarding Agents

**Use Cases**:
- New developer ramp-up
- Codebase exploration
- Environment setup
- Documentation generation

**Key Capabilities**:
- **Code Exploration**: Natural language queries about codebase
- **Environment Setup**: Generate setup scripts from package.json/Dockerfile
- **Documentation**: Create "how-to" guides from code comments
- **Task Assignment**: Suggest unit tests, refactoring opportunities

**Tools**: GitHub Copilot, OpenAI Codex

---

### Startup Operations Agents

**High-ROI Automation Areas** (from Athenic research):

| Area | Hours Saved/Week | Automation Level |
|------|------------------|------------------|
| Sales Pipeline | 30+ | 70% |
| Customer Support | 20+ | 70% |
| Finance Reconciliation | 8+ | 80% |
| HR Onboarding | 6+ | 60% |
| Content Operations | 12+ | 50% |

**ROI Example** (10-person startup):
- 36+ hours/week reclaimed
- $142K/year operational leverage
- Equivalent to hiring 1+ FTE

---

## Onboarding Skills by Category

### Employee Onboarding

| Skill | Description |
|-------|-------------|
| onboarding-checklist | Role-based task lists |
| tool-provisioning | Account creation (Slack, GitHub, etc.) |
| training-assignment | Course enrollment, 1:1 scheduling |
| progress-tracking | Completion monitoring, reminders |
| welcome-sequence | Email sequences, intros |

### Client Onboarding

| Skill | Description |
|-------|-------------|
| kyc-validation | Identity verification, compliance |
| document-collection | Gather required documents |
| workflow-orchestration | Multi-step journey management |
| welcome-personalization | Tailored onboarding experience |
| escalation-handling | Human handoff triggers |

### Developer Onboarding

| Skill | Description |
|-------|-------------|
| codebase-exploration | Natural language code queries |
| environment-setup | Script generation from configs |
| docs-generation | Auto-create how-to guides |
| task-suggestion | Good first issues, tests |
| architecture-explanation | System design documentation |

---

## Technical Patterns

### HRIS Integration

```python
# Trigger-based onboarding
async def onboard_employee(hire_data):
    role = hire_data.role
    
    # Generate checklist
    checklist = await generate_checklist(role, hire_data)
    
    # Provision tools
    await provision_slack(hire_data.email)
    await provision_github(hire_data.email, role)
    await provision_notion(hire_data.email, team)
    
    # Assign training
    await enroll_training(hire_data, role_modules[role])
    
    # Schedule
    await schedule_onboarding_calls(hire_data)
    
    # Track
    await start_tracking(checklist)
```

### Client Onboarding Flow

```
Welcome → Document Collection → Compliance Check → Setup → Activation → Success
   ↓              ↓                    ↓            ↓          ↓
Human        Auto              Auto         Auto      Human
Review       Reminder          Validation   Create    Check-in
```

### RAG for Onboarding

```python
# Knowledge base structure
onboarding_kb = {
    "company_policies": [...],
    "product_docs": [...],
    "process_guides": [...],
    "faq": [...],
    "escalation_rules": [...]
}

# Query with context
response = await rag.query(
    user_question,
    context={"role": "engineer", "week": 1}
)
```

---

## Agent Systems for Onboarding

### Arahi AI (GitHub Integration)

**Capabilities**:
- Employee onboarding automation
- Lead qualification
- Customer onboarding
- Data entry automation

**GitHub Integration Features**:
- Accept repository invitations
- Add email for auth users
- Add app access restrictions
- Add repository collaborators
- Team membership management

### UIX Store AI Toolkit

**Onboarding Form**:
- Captures business challenges and objectives
- Defines tech stack preferences
- Determines desired output format
- Generates metadata-rich AI Toolkit

**Deliverables**:
- Complete AI Toolkit Profile
- Ready-to-fork GitHub repo
- QuickStart Guide
- Developer Guide
- Deployment Plan

---

## Best Practices

### Employee Onboarding

1. **Role-Based Checklists**: Customize by department/role
2. **Tool Provisioning First**: Get access before day 1
3. **Buddy System**: Assign onboarding buddy
4. **Week 1 Goals**: Clear expectations for first week
5. **Automated Reminders**: Don't let tasks slip

### Client Onboarding

1. **Clear Milestones**: Define success criteria
2. **Personalization**: Tailor to industry/role
3. **Self-Service Where Possible**: Reduce human touchpoints
4. **Escalation Triggers**: Know when to involve humans
5. **Feedback Loop**: Continuous improvement from drop-offs

### Developer Onboarding

1. **Exploration First**: Let them ask questions
2. **Environment Automation**: Reduce setup friction
3. **Good First Issues**: Small wins early
4. **Documentation Auto-Gen**: Keep docs fresh
5. **Architecture Overview**: Big picture first

---

## References

- Athenic Blog: https://getathenic.com/blog/ai-agent-workflow-automation-startup-operations
- AgentiveAIQ: https://agentiveaiq.com/
- Arahi AI: https://arahi.ai/ai-agent/github
- UIX Store: https://uixstore.com/onboarding/
- Deel HR Automation: https://www.deel.com/