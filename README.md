# Evidence Discipline

An OpenAI Codex skill for evidence-based work under uncertainty.

## Purpose

This skill helps Codex distinguish verified facts from user claims, inferences, assumptions, and unknowns. It sets a practical threshold for asking focused questions and prevents unsupported conclusions, speculative changes, and unauthorized side effects.

Material conclusions and actions require evidence appropriate to the claim:
code or runtime evidence for current-system claims, authoritative external
sources for external facts, and operator input for intent, decisions,
permissions, expected behavior, or values controlled by that operator. User
statements about independently observable external conditions remain attributed
claims until verified. Memory, plausibility, similarity, and model capability
do not count as evidence.

For every material conclusion or side effect, the response must visibly state
one of `证据依据：代码或运行证据`, `证据依据：权威外部来源`,
`证据依据：操作人员输入`, or `证据依据：组合依据`. When no appropriate basis
exists, it must stop with `证据不足，无法继续` and request the missing basis.

Repository documents, comments, README files, Wiki pages, and historical records are context or leads by default. They cannot independently establish current behavior, root cause, or an implementation decision; current code, tests, or runtime results must corroborate those claims.

Code content and code provenance are separate claims. A local file, package name, code similarity, local Git commit, or local Git history proves only that the content exists in that local source; it does not prove official vendor or upstream origin. Official-origin claims require a directly verifiable authoritative repository, URL, artifact, or commit.

Assumptions are not an allowed working basis. When an unverified detail could affect correctness, scope, provenance, permission, or a side effect, ask the operator for the smallest required input or confirmation. Do not choose a default or continue under an assumption; stop at the evidence boundary when the input is unavailable.

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
