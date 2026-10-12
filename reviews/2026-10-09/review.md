# LLM Wiki skill review — 9 October 2026

> **Historical document:** This file records an earlier review. For active guidance, see the [current skill instructions](../../skills/llm-wiki/SKILL.md).

**Recommendation: keep the design, shorten repeated guidance, and show the generated content.** The package is small and the evidence rules are useful. The main issue is that it explains its process much more clearly than its output. It also repeatedly loads rules that have already been stated.

This review inspected all eight original repository files, delegated five independent public-repository comparisons, and ran one isolated mixed-source forward test. Existing skill and publication files were not changed. This review folder contains only review evidence and a synthetic example; it is outside the installable skill.

## What the folder contains

Reviewed local commit: `a4996afa5e2e540a9beaaf41bc20e72256fc4348`.

| Original file | Lines | Words | Assessment |
| --- | ---: | ---: | --- |
| `skills/llm-wiki/SKILL.md` | 106 | 1,249 | Good boundaries; repeated workflow and invariants; output shapes mostly implicit. |
| `references/wiki-conventions.md` | 99 | 877 | Useful source and disagreement guidance; repeats the main file. |
| `references/quality-checklist.md` | 50 | 430 | Mostly another version of the instructions; should emphasize observable completion checks. |
| `agents/openai.yaml` | 4 | 29 | Small and valid; default prompt emphasizes ingestion. No substantial problem. |
| `README.md` | 168 | 1,305 | Reasonable human-facing installation documentation; narrative example needs an actual resulting page. |
| `VALIDATION.md` | 74 | 519 | Clearly states small-fixture limits; historical execution evidence is absent from this repository. |
| `LICENSE` | 21 | 169 | Ordinary MIT license; no relevant bloat. |
| `.gitignore` | 1 | 1 | No relevant issue. |

Reference and metadata paths in the table are relative to `skills/llm-wiki/`. Word counts use whitespace splitting, not model tokens.

The usual add/compare/save route explicitly requires the main file and both references: **2,556 words across 255 lines**. README and validation documentation are not part of those required runtime reads. Do not count the entire repository as an always-loaded prompt.

The skill is well below the Agent Skills specification's recommended 500-line main-file limit. That does not prove good quality or mean it cannot be simplified. The specification recommends loading supporting resources only as needed. [Agent Skills specification](https://agentskills.io/specification)

## What this skill actually generates

It maintains a layer of knowledge between original sources and conversational answers. Its strongest intended outputs are:

| Output | Useful content | When to create it |
| --- | --- | --- |
| Topic or entity page | Current understanding assembled from relevant sources, nearby citations, useful connections. | A topic has lasting value; otherwise update its existing page. |
| Saved analysis or comparison | A conclusion, calculation, comparison or recommendation, labeled as derived and supported by sources. | The user requests saving reusable analysis. |
| Disagreement block | Competing claims, what differs, whether the mismatch is explained, and what remains unresolved. | Evidence warrants it; it can live inside a topic page. |
| Source record and navigation | Enough source metadata to retrieve the evidence; topic index, local conventions and activity log. | Needed for tracing or navigating the wiki. |
| Cited answer or health findings | A direct answer or review findings with uncertainty and evidence. | Usually a read-only conversational result. |

It does not currently define an article-writing, newsletter, slide-design or report-layout workflow. Those outputs can use wiki knowledge, but their audience, voice and presentation need separate instructions. Avoid expanding this focused skill just to cover all possible content.

The original [Karpathy LLM Wiki idea](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) likewise describes maintained entity, concept, comparison and synthesis pages, while leaving domain-specific formats configurable. Our narrower safeguards are reasonable adaptations. Its examples of many-page updates are not a page-count target.

### Actual output observed today

The independent agent read the current skill and both references, created three clearly synthetic fixtures, and followed this request: create a reusable wiki from a product proposal, two customer interviews and a usage-data note; then answer what is known about export demand, what is assumed, and what to validate next without changing files.

Result: three unchanged raw sources, one **337-word topic page**, and index/schema/log. Seven files, 7,033 bytes. No detached summary per source, standalone disagreement page, or saved answer snapshot.

- The page kept one interview participant's CSV request separate from another participant's preference for scheduled email.
- It distinguished account-list export activity from demand for a proposed saved-report feature.
- It labeled the retention benefit as unproven rather than converting the proposal into a fact.
- It cited the sources and offered derived validation steps.

Read the actual [generated topic page](example/wiki/export-demand.md), [original fixtures](example/raw/customer-interviews.md), and [index](example/wiki/index.md). The example is synthetic and is not product research.

The original agent's evidence manifest records identical hashes, sizes and modification times before and after the question for all seven files. All three initial source hashes matched after writing and querying. Sixteen relative links and anchors had no missing targets. The parent independently checked the seven current file hashes against the manifest and confirmed recorded before/after equality. [Evidence manifest](forward-test-evidence.json)

One too-broad citation was caught and corrected before completion. This is a successful final execution, not proof of error-free first-pass generation. It demonstrates a useful small result; it does not establish performance on corrections, evolving disagreements, large collections, non-text sources, private material or source injection.

## Five public comparisons

Selection: public GitHub repository search for `skills in:name,description stars:>50000 archived:false`, sorted by stars descending. The first five returned repositories were reviewed, with one subagent per repository. Counts below are API snapshots from 9 October 2026. Individual skill files do not have separate GitHub star counts. This is a defined search sample, not a universal ranking across every repository or skill registry.

Reviewers inspected representative actual skill files, not every skill in each collection. Competitor instructions were treated as source material; they were not installed or invoked. Commits and query metadata are saved in [research metadata](research-metadata.json).

| Repository | Stars | Representative files | Main lesson |
| --- | ---: | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers) | 296,785 | writing-skills; verification-before-completion; dispatching-parallel-agents | Define the output and test observable behavior. The writing guide itself is long. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 282,109 | writing-for-agents; research | State a concrete deliverable; route additional mechanics by need. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 275,713 | article-writing; market-research; search-first | Describe output modes clearly and disclose unavailable coverage. |
| [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 217,649 | karpathy-guidelines; CLAUDE.md and examples | A few principles and success indicators can guide a narrow task. |
| [anthropics/skills](https://github.com/anthropics/skills) | 180,112 | skill-creator; frontend-design | Complexity belongs where it is needed; different tasks justify different sizes. |

### Superpowers

Pinned [writing-skills](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/writing-skills/SKILL.md) is 681 raw lines and 3,814 words. It recommends defining a positive output recipe and using a complete example. Its testing guidance supports inspecting actual results rather than treating a loaded skill as successful.

The narrower [verification](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/verification-before-completion/SKILL.md) and [parallel delegation](https://github.com/obra/superpowers/blob/8ca22dba9a94f28898bbce59f2537ff4d87c747d/skills/dispatching-parallel-agents/SKILL.md) skills are 120 and 167 raw lines. Borrow checkable results and bounded delegation. Avoid copying repeated enforcement language or a universal testing ceremony for trivial wording changes.

### Matt Pocock

Pinned [writing-for-agents](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/writing-for-agents/SKILL.md) is 81 lines but 1,777 words—larger than our core by word count. [Skill mechanics](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/writing-for-agents/SKILL-MECHANICS.md) is a conditional reference. The [research skill](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/research/SKILL.md) is only 12 lines and 131 words, with a concrete cited-Markdown deliverable.

Borrow clear completion criteria and selective loading. Do not transplant the entire writing guide or treat its claims about model attention as experimentally verified. The comparison supports better allocation of instructions, not a universal word limit.

### ECC

Pinned [article-writing](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/article-writing/SKILL.md) and [market-research](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/market-research/SKILL.md) are 73 and 80 lines. They name deliverables and modes explicitly. [search-first](https://github.com/affaan-m/ECC/blob/ef648e01899ba3e8dc6371642deaaf64b4477775/skills/search-first/SKILL.md), 168 lines, distinguishes simple inline work from delegated research and asks for coverage limits.

Borrow those choices. Avoid importing ECC's entire ecosystem: it contains 293 canonical skill files plus mirrors and integrations. Concision and repository popularity do not establish comparative effectiveness.

### Karpathy guidelines

Pinned [karpathy-guidelines](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/skills/karpathy-guidelines/SKILL.md) is an actual packaged skill: 67 lines, 371 words, four principles, no required references. [Examples](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/EXAMPLES.md) sit separately.

Borrow one home per rule and observable success. Avoid copying broad stop-and-ask language. This is a narrower coding-behavior task, so its length cannot determine the correct size of wiki maintenance. Also, examples are not tests proving correctness.

### Anthropic

Pinned [skill-creator](https://github.com/anthropics/skills/blob/9d630808e4add0a7146de4af9384155d5dee350a/skills/skill-creator/SKILL.md) has 406 source lines and substantial optional evaluation machinery. [frontend-design](https://github.com/anthropics/skills/blob/9d630808e4add0a7146de4af9384155d5dee350a/skills/frontend-design/SKILL.md) is 52 lines and self-contained.

Borrow selective resources, concrete quality criteria and comparisons against the previous version when behavior changes. Avoid adding the creator's full evaluation/viewer infrastructure to the wiki skill or treating a maximum line guideline as a target.

## Changes that matter

### 1. Show the page before adding more rules

`SKILL.md:44` asks a new schema to record page types but does not define useful defaults. `README.md:109` provides a narrative scenario, not the generated artifact. Add one compact source → topic-page example, including a real citation pattern and a conditional uncertainty or disagreement section.

Describe a useful page as current understanding, evidence, and any reasoning or unanswered questions needed by the topic. These are editorial expectations, not mandatory headings on every page. Preserve existing usable layouts.

### 2. Remove repeated explanations and make references selective

`SKILL.md:26` forces the full conventions reference for almost every write and the checklist before completion. Useful repeated topics include:

- Unchanged evidence: main lines 12/53/68, conventions 19, checklist 8.
- Citation versus truth: main 14, conventions 19/47, checklist 13.
- Read-only questions: main 22/78, checklist 38.
- Disagreement lifecycle: main 85–90, conventions 63–75, checklist 24–28.

Keep short critical invariants in the main file. Keep detailed conventions in one place. Read layout/schema defaults for initialization; changing-source guidance when a source can change; disagreement guidance when competing claims need analysis. Compress the checklist to a few checks of results.

A reasonable first editing budget is **650–850 words for the main file**, rather than 1,249. This is a proposal, not a measured optimum or an acceptance requirement. Avoid pushing vital rules into references that the agent then fails to read.

### 3. Correct the status vocabulary

`wiki-conventions.md:65–71` describes disagreement states but defines **Superseded** as an older claim. `SKILL.md:87` applies it to a disagreement, while line 89 applies it to a claim.

Keep the dimensions distinct:

- Incoming change: new, update, disputed, no useful change.
- Evidence relationship: attributed source statement versus derived interpretation; uncertainty can qualify either.
- Disagreement: candidate, explained, open, resolved.
- Claim currency: current or superseded, with a link to its replacement.

These distinctions need clear wording, not a required structured database. The first three existing vocabularies are not inherently contradictory. Do not require literal badges for every sentence.

### 4. Bound maintenance claims and clarify repair authority

`SKILL.md:84` says to locate every affected page. Require searching topic names, aliases, links and repeated claims, then disclose inaccessible or uninspected areas when relevant. Do not imply complete coverage merely because a search ran.

The human-judgment instruction at `SKILL.md:98` is scoped to wiki checking, so it is not a direct contradiction with authorized comparison at line 89. Still, clarify that evidence-backed repairs already requested by the user can proceed; uncertain meaning changes should be reported for a decision.

### 5. Make validation reviewable

Keep `VALIDATION.md` as a historical report. It says its tests were small and is dated 25 August 2026. The original fixtures, prompts, outputs, hash records, model identity and tested commit are not included here, so this review cannot independently reproduce those historical passes.

Before merging a behavioral simplification, compare old and proposed instructions on the same small set: mixed-source addition; correction versus different definitions; unresolved disagreement; read-only answer; saved derived analysis; source injection; and health check. Inspect evidence support, unchanged source bytes, scope of edits and unnecessary generated content. A structural validator alone is insufficient.

Today's baseline YAML parsing, identity, description-length, UI invocation and local Markdown-link checks passed. The bundled Python validator could not run because its `PyYAML` dependency was missing in both available Python runtimes; that is an environment limitation, not a detected defect in this skill. No installer check or competitor performance benchmark was run today.

## Suggested smaller shape

Keep one skill with these parts:

1. **Purpose and outputs:** maintained topic pages, requested reusable analysis, cited answers, health findings.
2. **Essential invariants:** unchanged evidence, traceable claims, derived reasoning distinguished, unresolved disagreements preserved, existing conventions respected, read-only questions by default.
3. **Short operation guidance:** initialize, add/update/compare, query/save, check/repair.
4. **Conditional references:** defaults, changing sources and disagreements only where needed.
5. **Completion checks:** relevant pages coherent, citations verified, sources unchanged, necessary index/log updates, unrelated files untouched.

Use today's example as a demonstration rather than forcing its headings or 337-word length on every domain. Keep the append-only log and a short local schema; do not remove them solely because the demonstration has one topic. Keep source summaries optional, and avoid a new content-generation framework, page taxonomy or tool dependency without an observed need.

**Proposed next change:** simplify the common guidance, correct Superseded's meaning, and add one tangible example. Run a small old-versus-new comparison before claiming the revision preserves behavior.
