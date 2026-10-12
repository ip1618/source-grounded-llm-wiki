# Validation report

The original beta results are preserved below as historical checks. Results for the approved instruction changes are recorded in [Approved instruction revision — 2026-10-10](#approved-instruction-revision--2026-10-10). A later review found two example-output issues; their corrections and rechecks are recorded in [Example corrections and closure — 2026-10-12](#example-corrections-and-closure--2026-10-12).

## Original beta baseline

Candidate: `v0.1.0-beta`  
Tested: 2026-08-25

This report records practical checks completed before the first beta release. The tests used disposable folders and fresh agents. They show that the main workflow works on small examples; they do not prove that every future source or wiki will be handled perfectly.

## Result

The beta candidate passed the planned forward tests and the practical installer check.

## Forward tests

### Add and compare sources — Pass

Three sources were added in order. They included a new claim, a corrected number, a different measurement that looked conflicting at first, repeated context, and an instruction-injection attempt inside source text.

Observed result:

- stored source copies remained byte-for-byte unchanged;
- the untrusted instruction was not followed or copied into the wiki as an instruction;
- 10,000 registered accounts was kept as superseded history after a correction to 9,800;
- 8,500 monthly active users was marked Explained rather than Open because it measured a different population;
- new product and company claims were added with nearby source citations;
- the index and append-only log were updated.

### Read-only question — Pass

The agent answered an ambiguous question about user count by explaining both definitions and citing the underlying source files. Pre-test and post-test hashes confirmed that no files changed.

### Save reusable analysis — Pass

The agent saved a Basic-versus-Pro plan comparison. It labeled the comparison and recommendation as Derived, cited the two original plan sources, recorded missing purchase details as open questions, and updated the index and log. Source hashes did not change.

### Check wiki health — Pass

The agent found broken links, a hard-to-find page, missing provenance, a weakly supported claim, lost date and estimate qualifications, an unsupported competing number, and an incomplete log entry. It separated mechanical findings from judgment findings and made no changes during the read-only check. Pre-test and post-test hashes matched.

## Installer check

The documented command was run from the root of a disposable repository copy:

```bash
npx skills add . --skill llm-wiki
```

The Vercel Labs Skills CLI found one skill named `llm-wiki`, detected Codex, installed it at `.agents/skills/llm-wiki`, and exited successfully. The installed files were byte-for-byte identical to `skills/llm-wiki`.

A second explicit Codex-only check also passed:

```bash
npx skills add /path/to/source-grounded-llm-wiki --skill llm-wiki -a codex --copy -y
```

## Structural validation

The current `skill-creator` validator reported `Skill is valid!` for:

- the publication candidate in this repository;
- the review copy in the Documents folder;
- the locally installed Codex skill.

YAML parsing and relative-file checks also passed.

## Known limits

- These tests use small Markdown fixtures, not a long-running production wiki.
- Citation quality and disagreement decisions still require human review for important work.
- A successful literal or structural check does not prove that a factual claim is true.
- The installed name `llm-wiki` may collide with another community skill. Review and back up any existing folder before installation.

## Beta recommendation

The repository is ready for review as a `v0.1.0-beta` candidate. Keep the beta label until it has been used on several real wikis with different source types and sizes.

## Approved instruction revision — 2026-10-10

Scope: supported project-context completeness, readable code pointers, meaningful page boundaries, navigation, connected updates, read-only discussion, and tool-neutral instructions. Three instruction files changed; `agents/openai.yaml` is unchanged. The skill package still contains four files.

The initial positive reviews below did not catch the omitted discount business purpose or repeated research conclusions. Both findings were addressed in the later correction pass recorded below; they were output/review weaknesses, not additional instruction requirements.

### Structural and independent review checks

- The skill-creator validator reported `Skill is valid!`; YAML parsing, local reference targets, package layout, and `git diff --check` passed.
- Two independent read-only reviews found no material scope expansion, unnecessary instruction bloat, portability gap, or regression of source-grounded behavior.
- Original source protection, citations, claim/disagreement handling, saved analysis, read-only questions, append-only history, and privacy/injection protections remain intact.

### Focused forward tests

Fresh agents in Codex used the revised skill against isolated synthetic artifacts. Evaluators received requests and evidence, without expected page counts, filenames, or generated wording.

| Scenario | Observed result |
|---|---|
| Create a project wiki from discussion and code | Captured purpose, module responsibilities, decisions/reasons, rejected alternatives, open matters, and missing earlier history. A brief shared company boundary received its own page immediately because several responsibilities depend on it. Code inspection stayed distinct from runtime verification. |
| Add separately delivered UI design | Added one design topic and connected existing module explanations. Unapproved publishing wording and static-design limits remained visible. Original discussion, code, and design artifacts were unchanged. |
| Update the same wiki for a feature/code change | Updated existing topic pages without adding another topic document. Preserved the earlier calculation and delivery-time patch status as history, while describing current code and six coordinator-executed helper checks. Stored evidence and the prior log were preserved. UI, integration, and deployment correctness were not inferred. |
| Ingest research correction, then ask a read-only question | Corrected the current completion figure; explained differently defined timing measures; retained useful history and uncertainty; ignored an embedded instruction. Complete before/after inventories and hashes confirmed that the question changed zero files. |
| Independent fresh-reader reviews | Readers found current knowledge, reasons, related topics, evidence, and update locations in both wikis. No material unsupported claims, confusing ownership, unnecessary splits, or competing explanations were found. |

### Runtime coverage and limits

These checks used fresh Codex-hosted agents and small synthetic examples, not a large production wiki. They do not establish completeness for inaccessible history or universal content quality. The coordinator's six helper assertions validate only the synthetic calculation cases; they do not prove application behavior.

Claude Code `2.1.234` was present but reported no authenticated session, so Claude runtime behavior was not tested. OpenCode runtime behavior was not tested. Shared-format and instruction portability were reviewed; the historical installer check was not rerun. No additional agent configuration was introduced.

Tested instruction fingerprints (SHA-256):

```text
SKILL.md                         875d77511470dff211f8bb618d30bd657358f45159473db12582c3b05b326262
references/wiki-conventions.md   10a55af8fc7684961e64bf7248b5d152bcb96c21c605c33cf0fe62f230c2c221
references/quality-checklist.md  0bbae9c504bd66a531ca25fb90ae78d9fde8a9670bac54ba95ab0b095b5f0902
```

## Example corrections and closure — 2026-10-12

The later six-axis review identified two concrete issues in the synthetic examples: a missing business reason for the discount feature and repeated completion, timing, and causal-limit conclusions in the research page.

Corrected examples and their linked evidence are now preserved under `reviews/2026-10-10/examples/`. The original test outputs were temporary artifacts; this follow-up kept all writes inside the repository and retained the linked context needed to review the complete pages. The skill instructions, metadata, and four-file package are unchanged from the tested fingerprints above.

| Finding | Correction | Independent recheck |
|---|---|---|
| Discount mechanics were retained, but the stated business purpose was omitted | [Billing](reviews/2026-10-10/examples/project/wiki/billing.md#fixed-invoice-discount) now records the need for goodwill discounts, citing the original request. Calculation decisions and reasons, pending UI wording, delivery history, and verification limits remain intact. | A read-only reviewer compared the complete project example with its discussions, design, patch, code snapshots, and check record. No concrete source mismatch or material omission was found. |
| Research conclusions were repeated under several status labels | [Invoice preparation trial](reviews/2026-10-10/examples/research/wiki/invoice-preparation.md) consolidates the repeated interpretations while preserving figures, denominator, timing definitions, uncertainty, proposed trial status, open questions, and meaningful history. | A separate read-only reviewer compared the corrected page, index, and log with both original research notes. No material content issue or unnecessary repeated conclusion was found. |

Additional checks:

- Only the two owning example pages and their append-only logs differ from the imported example set. All 36 other copied files, including source records, original inputs, code, design, and supporting pages, remain byte-identical. Prior log entries remain unchanged prefixes.
- All 233 local example links resolve inside the repository; source-register anchors and the validation report's example links also resolve.
- Instruction fingerprints still match the 2026-10-10 checks; `git diff --check` passes.

This was a manual correction followed by independent source-to-output review. It was not a fresh skill-generation test, a helper-code rerun, or a Claude/OpenCode runtime test. The earlier runtime and production-scale limits still apply.

**Disposition:** both known example findings are closed. The approved repository revision is ready to finalize within the documented validation limits.
