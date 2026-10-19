# Evidence Discipline

An OpenAI Codex skill for evidence-based work under uncertainty.

## Purpose

This skill helps Codex distinguish verified facts from user claims, inferences, assumptions, and unknowns. It sets a practical threshold for asking focused questions and prevents unsupported conclusions, speculative changes, and unauthorized side effects.

Material conclusions and actions require at least one explicit basis: current code or a directly code-linked artifact, or a fact, decision, permission, or value explicitly supplied by the user or an authorized operator. Memory, plausibility, similarity, and model capability do not count as evidence.

For every material conclusion or side effect, the response must visibly state one of `证据依据：代码依据`, `证据依据：操作人员输入依据`, or `证据依据：两者都有`. When neither basis exists, it must stop with `证据不足，无法继续` and request the missing basis.

## Scope

Use it for tasks involving factual claims, diagnosis, requirements interpretation, code changes, tool use, or decisions with incomplete information. It is intentionally lightweight for deterministic tasks with complete inputs and for pure creative writing.

## Included files

- `SKILL.md`: the skill instructions.
- `agents/openai.yaml`: Codex interface metadata.
- `scripts/validate_skill.py`: dependency-free structural validation.
- `.github/workflows/validate.yml`: validation on pushes and pull requests.

## Local validation

Run:

```text
python scripts/validate_skill.py .
```

The validator checks the skill frontmatter, required files, required sections, naming, and unfinished TODO markers. It does not prove that the behavior is correct for every task.

## Privacy

This repository contains no user-specific credentials, local paths, or personal contact details. Git commit identity should be configured locally with a GitHub noreply address when publishing changes.

## License

MIT. See `LICENSE`.
