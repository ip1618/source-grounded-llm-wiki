# Validation report

The latest results are in [Repetition guidance and desktop workflow — 2026-10-12–13](#repetition-guidance-and-desktop-workflow--2026-10-1213): creation, feature updates, guided repairs, and read-only questions completed in Codex and Claude desktop. Initial outputs needed corrections; the repairs passed independent review. Earlier checks below are historical results for their stated versions and stages.

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

## Plugin distribution checks — 2026-10-12

- Added a plugin manifest and marketplace catalog under `.claude-plugin/`. The four skill files remain byte-identical to the approved revision; both manifests pass strict Claude validation and independent review.
- Published release A only on [the separate test branch](https://github.com/ip1618/source-grounded-llm-wiki/tree/codex/llm-wiki-desktop-update-test-20261012), commit `279dae77bb63ce40c5fc5c877403c81079ef4378`. Its distinct plugin and marketplace name is `llm-wiki-desktop-test`, version `0.1.0-test.a`. A harmless reference marker is confined to that branch. `main` was not changed remotely.
- Codex CLI `0.159.0` registered the Git-backed source and installed A using `plugin add`; its test plugin is enabled. Claude CLI `2.1.234` installed A with local scope for a disposable fixture project. At this installation baseline, both cached manifests and all five skill-file hashes matched release A; Claude's install record also matched the A commit. Cache checks alone do not establish runtime behavior.
- A separate, user-authorized Codex app chat discovered `llm-wiki-desktop-test:llm-wiki` and read marker A from its installed cache, without being given that cache path. The running app is `26.1007.21159`, build `20052`, with bundled runtime `0.162.0-alpha.17.2`.
- In that app chat, creation and a later feature update preserved all four synthetic inputs, retained seven logical wiki pages, and preserved the prior log bytes. Two independent reviews confirmed supported decisions/reasons, honest code and design limits, and all 97 local links. The subsequent question cited original evidence and changed zero of the project's nine files. No skill-repository file changed during these runs.
- **Readability finding at this stage:** profiles and masterdata repeated billing-helper and integration-limit details. Their page boundaries are useful, but the repeated explanations create avoidable maintenance and reading effort. The later guidance change and revised workflow checks are recorded below; this initial run did not establish universally low-bloat output.
- B is published only on the same test branch, commit `03f213327b231bb26f40a3615825d0ad46169e56`, version `0.1.0-test.b`. Only its version and harmless reference marker differ from A. Source URL/ref and plugin identity remain fixed. No manual update, refresh, reinstall, or installed-file edit has been performed after publication.
- **Codex automatic update passed:** while the app stayed open, two read-only observations and a normal app-chat follow-up still found A. After the user quit and reopened the app, the Git marketplace moved to B's commit and the installed manifest, marker, and all five skill-file hashes matched B. The same test chat then discovered B's supplied skill path and read marker B. No manual plugin update, refresh, reinstall, or installed-file edit was used. This confirms the A-to-B transition for the tested app build and Git source. The [matching runtime source](https://github.com/openai/codex/blob/rust-v0.162.0-alpha.17.2/codex-rs/app-server/src/message_processor.rs#L528-L546) schedules Git marketplace updates at app-server startup; continuous updating while the app remains open was not established.
- **Claude automatic update passed:** desktop app `2.31226.1`, with Code runtime `2.1.295` confirmed through `/status`, loaded A from the supplied namespaced skill in the disposable local project. Marketplace auto-update was enabled before B publication. While that session remained open, Claude automatically fetched B at `2026-10-12T15:15:21.728Z`; the Git source commit, installed manifest, marker, and all five skill-file hashes matched B. After accepting the already-authorized workspace trust confirmation through the [documented launch link](https://support.claude.com/en/articles/14729294-open-claude-desktop-with-a-link), a fresh session confirmed the correct working directory, supplied B skill path, and marker B. No manual plugin update, refresh, reinstall, reload, or cache edit was used.
- **Claude test limits:** its runtime A baseline was observed after B had already been published, although the recorded A installation predates publication. The test therefore proves the observed automatic A-to-B transition, with a different sequence from Codex. Earlier fresh-session attempts started without the primary folder and were excluded from activation evidence. Accepting the linked workspace confirmation resolved the final attempt; no app bug diagnosis is established. Claude wiki creation/update/query behavior was outside this phase and was tested subsequently below.

**Disposition at this stage:** automatic plugin download and activation pass for the tested Codex and Claude desktop builds and Git source. Codex focused functional checks also pass, with a readability finding. Subsequent functional results follow below. These are focused tests, not a guarantee for every client version or installation scope.

## Repetition guidance and desktop workflow — 2026-10-12–13

The conventions now keep detailed explanations with their owning topic, allow useful local summaries and necessary limitations, and require consolidation of repeated explanations. The checklist adds a corresponding finishing check. Only these two reference files changed; `SKILL.md` and `agents/openai.yaml` remain unchanged. Independent instruction review found no loss of context, forced page template, or page-length rule.

| Check | Result |
|---|---|
| Revised skill validation | The skill-creator validator passes. JSON manifest/path checks and `git diff --check` pass. |
| Independent Codex forward test | Created and updated seven stable wiki pages. Source bytes and earlier log bytes were preserved; the read-only question changed zero of ten project files. Review found a repeated catalog reason and ambiguous old/new helper wording, so the initial generation is recorded as needing repair. A separate authorized wiki-check repair corrected both; its recheck found 74 valid links and zero query writes. |
| Claude test setup | A project-local test copy uses the unique name `llm-wiki-review`; only its frontmatter name differs. The instruction body and supporting files match this repo. No global skill, installed plugin, or cache was edited. The app confirmed the supplied local skill path and correct working directory. |
| Claude creation | Created seven topic/navigation/convention pages and stored evidence copies. All original inputs and protected skill/settings files stayed byte-identical. The skill repo was unchanged during the run. |
| Claude feature update | Kept the seven wiki paths, preserved the previous log prefix, and stored all four inputs byte-identically. The original repository helper remains unchanged; the discount helper is explicitly separate supplied evidence. All 119 local links, heading anchors, and line locators in the update snapshot passed checks. |
| Claude initial source/readability review | Meaningful context and the discount update were preserved. Review found inconsistent wording for an inferred catalog-access boundary and repeated calculation steps, examples, and display status within Billing. Initial generation needed repair. |
| Claude guided wiki-check repair | Completed on 2026-10-13 in the confirmed fixture session. Qualified the catalog inference and consolidated the repeated Billing/Profile explanations. An independent source-to-output review confirmed the findings are fixed, with decisions, reasons, citations, history, and code status preserved. Only five wiki pages and the appended log changed; stored sources, code, skills, settings, schema, and all earlier log bytes stayed unchanged. All 124 local links, heading anchors, and line locators passed checks. |
| Claude read-only query | Answered why cents and a shared catalog were chosen, and how the discount affects tax, citing original evidence. Preserved open questions and distinguished the unchanged repository helper from the separate supplied helper. Before/after hashes confirmed zero changes across all 19 project files. |

The revised content was tested locally because publication is not authorized. These functional checks are separate from the earlier A/B plugin-update test; the revised references have not been published or tested through a new plugin release. Claude's computer-use controls were intermittently unreliable, and some desktop steps needed user assistance. A folderless launch was excluded; the recorded workflow ran in the confirmed disposable project. One temporary log backup created during the feature update was reported removed; no lasting writes outside the wiki/source-record areas were found in the project.

These are small fictional workflows with guided repairs, not clean first-pass generation or production-scale proof. The app used Claude Code runtime `2.1.295`; CLI manifest validation used `2.1.234`. Structural checks and citation locators do not establish factual correctness. Independent review found no remaining material source or repetition issue in the repaired pages. The latest query was also checked against its original sources.

Query review noted two minor wording improvements: “same monetary amounts” would be more precise than “identical results” because the new helper returns an extra discount field; “no test evidence supplied” would be more precise than “nothing has been tested.” Neither changes the three supported answers. The observed response is retained without rewriting it.

Current instruction fingerprints:

```text
SKILL.md                            875d77511470dff211f8bb618d30bd657358f45159473db12582c3b05b326262
references/wiki-conventions.md      a684c270f38aa6d84365dd8debf26ac0ec3ce7020adc2906fba64cf0f56124a9
references/quality-checklist.md     5ea5c373456bf83297b236c929ad713eecbc4f4796a2d70cf5fa90dd4b6d8d8b
agents/openai.yaml                  d1ab7c7f4822e70ccdd519b5e0e6b3398edb1e9c3575e34b587f4435ca07383c
```

**Disposition:** the narrow guidance fix and focused create/update/repair/query workflows pass within these limits. OpenCode runtime behavior and large production wikis remain unverified. No push was made.
