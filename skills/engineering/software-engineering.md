# Software Engineering Agent Skill

## Purpose
Enable AI coding agents to perform software engineering tasks with structured workflows and best practices.

## Triggers
- User asks to fix a bug or implement a feature
- Code review request
- Documentation generation needed
- Test coverage analysis requested

## Workflow

### Phase 1: Understanding
1. Read the relevant codebase files
2. Understand the architecture and patterns
3. Identify the specific area needing changes
4. Check existing tests and documentation

### Phase 2: Implementation
1. Write the code changes following project conventions
2. Ensure type safety and error handling
3. Add inline documentation where complex
4. Update relevant tests

### Phase 3: Validation
1. Run existing tests to ensure no regressions
2. Run linters and type checkers
3. Verify code follows project style guides
4. Check for security vulnerabilities

### Phase 4: Review
1. Create a clear PR description
2. Explain the changes made
3. Highlight any breaking changes
4. Note testing performed

## Tools
- Code execution (bash, python, node)
- File read/write
- Git operations
- Test runners
- Linters
- Type checkers

## Rules
- Always run tests before submitting
- Never commit secrets or credentials
- Follow project coding conventions
- Keep commits small and focused
- Write meaningful commit messages

## Examples

### Bug Fix
```
User: Fix the login timeout issue
Agent: 1. Find login-related code
       2. Identify timeout configuration
       3. Fix the timeout value
       4. Run tests
       5. Create PR
```

### Feature Implementation
```
User: Add user profile picture upload
Agent: 1. Review existing user model
       2. Design storage approach
       3. Implement upload handler
       4. Add image processing
       5. Write tests
       6. Update API docs
       7. Create PR
```

## Related Skills
- code-review
- documentation
- testing
- security-audit
- refactoring