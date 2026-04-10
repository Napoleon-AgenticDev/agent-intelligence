# Onboarding Agent Skill

## Purpose
Enable AI agents to execute business onboarding tasks including employee onboarding, client onboarding, and workflow automation for startups.

## Triggers
- New employee starting
- New client onboard
- Process documentation needed
- Workflow automation requested

## Workflows

### Employee Onboarding
1. Generate role-based checklist
2. Provision accounts (Slack, GitHub, email, etc.)
3. Assign training modules
4. Schedule introductions
5. Track progress and send reminders

### Client Onboarding
1. Send welcome sequence
2. Collect required documents
3. Verify compliance/KYC
4. Configure account/setup
5. Guide through activation
6. Set up success check-ins

### Developer Onboarding
1. Explain codebase architecture
2. Generate environment setup scripts
3. Create onboarding documentation
4. Suggest good first issues
5. Walk through key processes

## Common Tasks

### HR Onboarding
- Checklist generation by role
- Tool provisioning (Slack, Google, GitHub, Notion)
- Training assignment
- 1:1 scheduling
- Progress tracking

### Client Onboarding
- Welcome emails/videos
- Document collection
- Compliance verification
- Account setup
- Activation tracking

### Process Documentation
- Workflow documentation
- SOP creation
- Training materials
- Knowledge base articles

## Tools
- HRIS (BambooHR, Deel, Workday)
- Communication (Slack, email)
- Identity (Google, Microsoft, Okta)
- Training (Loom, Notion, LMS)
- CRM (HubSpot, Salesforce)

## Rules
- Personalize by role/industry
- Set clear milestones
- Automate where possible
- Escalate when needed
- Track completion rates
- Gather feedback

## Examples

### New Employee
```
User: Onboard a new engineer starting Monday
Agent: 1. Create engineer checklist (accounts, access, training)
       2. Provision Slack, GitHub, email
       3. Assign engineering onboarding modules
       4. Schedule intro calls
       5. Set up progress tracking
```

### New Client
```
User: Onboard our new enterprise client
Agent: 1. Send welcome sequence
       2. Collect required documents
       3. Verify compliance requirements
       4. Configure account
       5. Guide through setup
       6. Schedule success check-in
```

## Related Skills
- employee-onboarding
- client-onboarding
- tool-provisioning
- compliance-automation
- documentation-generation
- workflow-automation