# Skill review: scope, operations, and one project example

> **Historical document:** This file records an earlier discussion and proposed changes. For active guidance, see the [current skill instructions](../../skills/llm-wiki/SKILL.md).

**Agreed direction:** keep the source-grounded wiki workflow. Improve completeness, readability, page boundaries, and connected updates.

This records the corrected discussion, replacing the earlier overly broad proposal. These are proposed changes for discussion, not authorization to implement them. The operation descriptions below explain the baseline and proposed behavior.

## 1. Your requirement, understood correctly

- Review the relevant session history to recover project context: requirements, constraints, decisions, reasons, corrections, and unresolved matters.
- When context was compacted or is incomplete, inspect accessible earlier history. Use subagents for long records when useful, then reconcile their findings.
- Capture the supported project knowledge in its appropriate place. Reading history does not require a separate conversation archive or a page per session.
- Check coverage against available history and artifacts. Disclose missing records rather than claiming guaranteed completeness.

My earlier proposal made conversation capture sound like a new central purpose. That was too broad. It is a context-gathering step within the existing project-wiki workflow.

## 2. What the existing SKILL.md operations mean

Current instructions: [SKILL.md](/Users/ipu/Documents/source-grounded-llm-wiki/skills/llm-wiki/SKILL.md).

| Term | Plain meaning | In your system-design + UI-design scenario |
|---|---|---|
| Setup | Find the existing wiki, or create a small starting structure and local rules. | Establish where a reader starts and where project topics belong. |
| Add sources | Read supporting material and integrate useful information into the right pages. | Use the system discussion, diagrams, UI designs, and relevant project files. Keep links to what supports the explanation. |
| Questions | Answer from existing knowledge and evidence; do not edit merely because someone asks. | “How does this screen connect to the system?” |
| Comparisons | Check whether new information adds, changes, or conflicts with existing knowledge. | If a UI flow needs behavior the architecture has not specified, identify the gap. Do not invent a backend decision. |
| Saved analysis | Keep reasoning that will be useful again, clearly identified as analysis. | Explain a discussed design tradeoff without presenting an assistant recommendation as approved. |
| Health checks | Look for weak evidence, broken links, duplication, and unclear/outdated knowledge. | Can a reader find both designs, understand their relationship, and tell what remains undecided? |
| Excludes conversational memory | This skill is not a general system for remembering personal preferences or entire chats across interactions. | It can still review session history to capture project context. |
| Excludes coding checkpoints | A checkpoint records where work stopped and how to resume: branch, unfinished work, next action. | The wiki explains the project; a companion checkpoint can link to it for continuation. |

One-off summaries, Notion capture, standalone coding checkpoints, and general personal memory would remain outside the scope. The proposed scope clarification would avoid incorrectly excluding a maintained project wiki through the baseline's broad generic-documentation exclusion.

## 3. One continuous example: system design first, UI design later

This uses your scenario. It does not assume a particular product, technology, business model, or approved decision.

### Step A — system design is discussed

Read the relevant discussion and supplied artifacts. Capture:

- What the system is meant to do and its stated constraints.
- Components, responsibilities, and flows actually discussed.
- Decisions, why they were made, and meaningful alternatives considered.
- What is proposed, agreed, implemented, or unverified, where relevant.
- Questions still open.

If no UI design exists yet, do not fill a UI document with speculative screens.

### Step B — UI designs are added

Add the screens, user journeys, relevant states, design decisions, and links to the actual designs. Relate them to the system design wherever the connection is supported.

**UI deserves an identifiable place.** Choose a section or page by its responsibility, importance, relationships, and reading/update needs, not length. A short supported core concept can have its own page immediately. Keep closely connected material together when splitting would make it harder to follow; possible future expansion alone does not justify an empty page.

When the topics have distinct useful roles, a reasonable reading map is:

| Page | What belongs there | Reading / update role |
|---|---|---|
| `index.md` | Short project context and links to the main topics. | Start here; find the topic you need. |
| `system-design.md` | Architecture, responsibilities, flows, decisions/reasons, and system questions. | Understand or change how the system works. |
| `ui-design.md` | Screens, user journeys, design references, decisions/reasons, and supported system connections. | Understand or change the user experience. |
| Existing `log.md` | Significant changes, reasons, and affected pages. | Understand what changed over time. |

The existing source area and `schema.md` retain their roles. The schema is a short maintenance guide, not another project explanation. These filenames illustrate this scenario; they are not a required template.

### Step C — connect the two topics

- The UI page links a relevant flow to the system responsibility it uses.
- The system page links back when the UI clarifies a system behavior or constraint.
- Explain each relationship where it belongs; link instead of copying the full explanation into both pages.
- If a connection is not yet decided, record that gap. Do not manufacture an API, component, or approval.

### Step D — a design changes later

Update the affected section of `ui-design.md`. Update `system-design.md` only if responsibilities, flows, contracts, or constraints are affected. Record a meaningful decision change and its reason in history.

Keep the current explanation easy to find. Do not create competing `ui-v2`, `ui-final`, or dated current pages merely because another discussion occurred. Actual design revisions and significant historical records can still be retained and linked.

## 4. Focused skill changes

| Location | What already exists | Focused adjustment |
|---|---|---|
| SKILL.md scope | Maintained source-grounded knowledge; broad exclusions. | Clarify that reviewing session history for project completeness is supported. Keep the original purpose. |
| Discover / Add a source | Read local rules, index, related pages; update topic owners and dependents. | Review relevant session history and artifacts when needed to recover context. Check requirements, constraints, decisions/reasons, corrections, and unresolved points; disclose gaps. |
| Pages and links convention | One topic home; create pages only for a lasting role. | Choose boundaries by meaning and navigation, allowing short core concepts immediately. Explain relationships using this architecture/UI example. |
| Compare / update workflow | Compare new evidence; preserve history; update affected pages. | Apply it to design changes without treating newer discussion as approval or creating another current version. |
| Quality checklist | Evidence, links, duplicates, history, and safe changes. | Check whether supported context is covered, explanations are clear, and readers can find both a topic and the place to update it. |

These proposed changes fit in the existing skill and references. No new reference file, template set, or required folder tree is proposed.

Release/publication and checkpoint-companion changes remain outside this proposal.
