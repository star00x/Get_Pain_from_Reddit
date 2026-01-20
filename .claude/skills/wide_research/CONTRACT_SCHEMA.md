# Contract-Based Execution Schema

Defines verifiable contracts for all subagent tasks. Every subagent output is mechanically validated against these schemas.

## Core Principle

> **Don't trust what subagents SAY they did. Verify what they PROVE they did.**

## Contract Structure

Every subagent task follows this structure:

```
┌─────────────────────────────────────────────────────┐
│                     CONTRACT                         │
│                                                      │
│  PRE:   Input conditions (verify before starting)   │
│  EXEC:  Required steps (with checkpoints)           │
│  POST:  Output guarantees (mechanically verified)   │
│                                                      │
│  OUTPUT: JSON Schema (strict, all fields required)  │
│  EVIDENCE: Required for every judgment              │
└─────────────────────────────────────────────────────┘
```

## Verification Flow

```
Subagent completes task
        ↓
Returns JSON output
        ↓
Main agent runs mechanical verification:
  1. Schema validation (all required fields present)
  2. POST conditions check (evidence length, finding count, etc.)
        ↓
If ANY check fails → Task FAILED → Retry or escalate
If ALL checks pass → Accept output
```

---

## Base JSON Schema (all subagents inherit)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["task_id", "status", "checks_performed", "output_file"],
  "properties": {
    "task_id": {
      "type": "string",
      "description": "Unique task identifier"
    },
    "status": {
      "type": "string",
      "enum": ["completed", "partial", "failed"],
      "description": "Task completion status"
    },
    "checks_performed": {
      "type": "object",
      "description": "Record of all required checks with evidence",
      "additionalProperties": {
        "type": "object",
        "required": ["executed", "evidence", "verdict"],
        "properties": {
          "executed": {
            "type": "boolean",
            "description": "Whether this check was performed"
          },
          "evidence": {
            "type": "string",
            "minLength": 50,
            "description": "Specific evidence supporting the verdict"
          },
          "verdict": {
            "type": "string",
            "enum": ["pass", "fail", "partial"],
            "description": "Check result"
          }
        }
      }
    },
    "output_file": {
      "type": "string",
      "description": "Path to the written output file"
    }
  }
}
```

---

## POST Condition Verification (Main Agent)

Main agent performs these mechanical checks on every subagent output:

### Universal Checks (all subagents)

```python
def verify_universal(output: dict) -> list[str]:
    errors = []

    # 1. Required fields exist
    for field in ["task_id", "status", "checks_performed", "output_file"]:
        if field not in output:
            errors.append(f"Missing required field: {field}")

    # 2. All checks have evidence
    for check_name, check_data in output.get("checks_performed", {}).items():
        if not check_data.get("executed"):
            errors.append(f"Check not executed: {check_name}")
        if len(check_data.get("evidence", "")) < 50:
            errors.append(f"Insufficient evidence for: {check_name} (min 50 chars)")

    # 3. Status is valid
    if output.get("status") not in ["completed", "partial", "failed"]:
        errors.append(f"Invalid status: {output.get('status')}")

    return errors
```

### Researcher-Specific Checks

```python
def verify_researcher(output: dict) -> list[str]:
    errors = verify_universal(output)

    # Minimum findings
    findings = output.get("findings", [])
    if len(findings) < 3:
        errors.append(f"Insufficient findings: {len(findings)} < 3")

    # Each finding has source
    for i, f in enumerate(findings):
        if not f.get("source_url"):
            errors.append(f"Finding {i} missing source_url")
        if not f.get("content"):
            errors.append(f"Finding {i} missing content")

    # Required checks performed
    required_checks = ["relevance_check", "signal_quality_check"]
    for check in required_checks:
        if check not in output.get("checks_performed", {}):
            errors.append(f"Missing required check: {check}")

    return errors
```

### Aggregator-Specific Checks

```python
def verify_aggregator(output: dict) -> list[str]:
    errors = verify_universal(output)

    # Quality assessment present
    qa = output.get("quality_assessment", {})
    if not qa:
        errors.append("Missing quality_assessment")

    # Collective findings
    if len(qa.get("collective_findings", [])) < 3:
        errors.append("Insufficient collective_findings: need >= 3")

    # Required checks
    required_checks = ["format_validation", "content_quality", "cross_task_consistency"]
    for check in required_checks:
        if check not in output.get("checks_performed", {}):
            errors.append(f"Missing required check: {check}")

    return errors
```

### Synthesizer-Specific Checks

```python
def verify_synthesizer(output: dict) -> list[str]:
    errors = verify_universal(output)

    # Executive summary present
    summary = output.get("executive_summary", {})
    if not summary:
        errors.append("Missing executive_summary")

    if len(summary.get("key_findings", [])) < 3:
        errors.append("Insufficient key_findings: need >= 3")

    # Required checks
    required_checks = ["completeness_check", "coherence_check"]
    for check in required_checks:
        if check not in output.get("checks_performed", {}):
            errors.append(f"Missing required check: {check}")

    return errors
```

---

## Evidence Requirements

Every judgment MUST include specific evidence:

### Bad Evidence (will fail validation)

```
❌ "内容相关"
❌ "质量良好"
❌ "检查通过"
❌ "All good"
```

### Good Evidence (will pass validation)

```
✅ "内容相关：5 篇文章中 4 篇直接讨论 invoice 痛点，
    具体包括 [URL1] 的追款问题、[URL2] 的格式问题"

✅ "质量良好：引用来自 r/smallbusiness (↑42) 和
    r/freelance (↑28)，包含用户原话和具体数字"

✅ "跨任务一致：task-001 和 task-002 都将'追款'
    列为 #1 痛点，仅在次要痛点排序上有差异"
```

### Evidence Minimum Length

| Check Type | Minimum Length |
|------------|----------------|
| Simple validation | 50 characters |
| Quality judgment | 100 characters |
| Cross-task analysis | 150 characters |

---

## Failure Handling

When verification fails:

```
1. Log failure reason
2. Decide action:
   - Minor issue (e.g., 2 findings instead of 3) → Retry once
   - Major issue (e.g., no evidence) → Retry with stronger prompt
   - Persistent failure → Escalate to user
3. Track retry count (max 2 retries per task)
```

---

## Implementation in Prompts

Each subagent prompt MUST include:

```markdown
## ⚠️ CONTRACT

### PRE-CONDITIONS
- [ ] [List input requirements]

### REQUIRED CHECKS (with evidence)
You MUST perform these checks and record evidence:

| Check | What to verify | Evidence requirement |
|-------|---------------|---------------------|
| [check_name] | [what to check] | [min X chars, include Y] |

### POST-CONDITIONS (mechanically verified)
Your output will be validated. Task FAILS if:
- Any required field is missing
- Any evidence is < 50 characters
- Findings count < 3
- Any check.executed != true

### OUTPUT FORMAT (JSON - strict)
[JSON Schema here]
```

---

## Verification Pseudocode for Main Agent

```
for each subagent_output:
    # Parse JSON
    try:
        output = json.parse(subagent_output)
    except:
        FAIL("Invalid JSON")

    # Run verification
    errors = verify_{subagent_type}(output)

    if errors:
        if retry_count < 2:
            retry_task(stronger_prompt)
        else:
            escalate_to_user(errors)
    else:
        accept_output(output)
```
