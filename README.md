# Source-Grounded LLM Wiki

An agent skill for maintaining a connected Markdown wiki from project discussions, designs, code, and research. It keeps supported context, decisions, and their reasons easy to find, with links back to the evidence.

The skill is named `llm-wiki`. Use it to keep knowledge useful as a project develops or new sources arrive.

## What you get

A wiki with readable topic pages, links between related ideas, and preserved sources. For example, a project wiki might look like this:

```text
raw/                  Stored sources and source records
wiki/
  index.md            Where to start
  project.md          Purpose, scope, and open decisions
  billing.md          Billing rules, reasons, and related code
  invoice-editor.md   UI design and its connection to billing
  log.md              Append-only update history
  schema.md           Local wiki conventions
```

This is an example, not a required template. The skill reuses an existing structure when it is usable and creates topic pages only when they have a meaningful role.

Browse the saved fictional examples:

- [Project wiki](reviews/2026-10-10/examples/project/wiki/index.md): decisions, module relationships, UI design, and a later discount feature.
- [Research wiki](reviews/2026-10-10/examples/research/wiki/index.md): research notes, a corrected result, and uncertainty that remains open.

## Installation

Use the native plugin for Codex or Claude Code. Both use the same skill folder. In a desktop app, you can ask your agent to run the one-time setup commands below if the matching CLI is installed. Reopen the app afterward.

**Codex**

```bash
codex plugin marketplace add ip1618/source-grounded-llm-wiki
codex plugin add llm-wiki@source-grounded-llm-wiki
```

**Claude Code**

```bash
claude plugin marketplace add ip1618/source-grounded-llm-wiki
claude plugin install llm-wiki@source-grounded-llm-wiki
```

For other agents, use the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add https://github.com/ip1618/source-grounded-llm-wiki --skill llm-wiki
```

Append `-a opencode`, `-a codex`, or `-a claude-code` to choose an agent, and `-g` to install across projects. Check for an existing skill named `llm-wiki` before installing, and back up an unrelated skill rather than overwriting it.

For manual installation, copy [skills/llm-wiki](skills/llm-wiki) into the skill directory supported by your agent. Consult that agent's documentation for the correct location.

## Plugin updates

- **Codex:** the Git-backed plugin automatically downloaded a new release and loaded it after quitting and reopening the app in our test.
- **Claude Code:** [enable marketplace auto-update](https://code.claude.com/docs/en/plugins/host-marketplace#turn-on-auto-update) under `/plugin` → Marketplaces. In our desktop test, the plugin downloaded a new release in the background and loaded it in a fresh local Code session.
- **Skills CLI or manual copies:** these do not use the plugin update mechanism. Update them through the installer or replace the copied folder.

Maintainers publish a release by changing the version in [.claude-plugin/plugin.json](.claude-plugin/plugin.json) and pushing the updated package. See [VALIDATION.md](VALIDATION.md) for the tested versions and limits.

## Usage

Select `llm-wiki` in your agent, or name the skill in your request:

**Create a wiki**

```text
Use the llm-wiki skill to create a wiki from this folder and relevant project discussions, designs, and code.
```

**Update it**

```text
Use the llm-wiki skill to add this report or feature change and update the affected pages.
```

**Ask a question**

```text
Use the llm-wiki skill to explain how billing works, with links to the original evidence.
```

You can also ask it to compare sources, save reusable analysis, or check the wiki for missing context, weak citations, and broken links. It is for maintained project or research knowledge; standalone coding-session checkpoints and general personal memory are outside its scope.

## How updates work

- **Capture supported context:** include requirements, decisions, reasons, and business, technical, or UI details present in the evidence. Keep proposals, agreements, implementation, and verification distinct. Missing context stays visible.
- **Split by meaning:** a topic gets its own page when its role or reading and maintenance needs justify it, even if it is short. Connect related topics. Page length alone does not decide the structure.
- **Update connected pages:** change the affected explanations and relationships at stable paths. Record the update in the log and retain useful history instead of creating competing versions for each feature or discussion.
- **Keep evidence traceable:** preserve stored source files, cite original evidence, and keep selected code paths and function names in a short related-code list. Show uncertainty and unresolved disagreements; a citation does not guarantee truth.
- **Keep questions read-only:** asking a question does not change the wiki unless saving is requested or authorized. Saved analysis is identified as an interpretation, not an original source.

For example: discuss billing rules, capture the decision and its reason, connect the UI design and relevant functions, then update those same pages when billing changes.

## Repository and status

| Location | Purpose |
|---|---|
| [SKILL.md](skills/llm-wiki/SKILL.md) | Current agent instructions |
| [Wiki conventions](skills/llm-wiki/references/wiki-conventions.md) and [quality checklist](skills/llm-wiki/references/quality-checklist.md) | Supporting guidance used when relevant |
| [agents/openai.yaml](skills/llm-wiki/agents/openai.yaml) | Optional display metadata for OpenAI interfaces |
| [.claude-plugin/](.claude-plugin/) | Shared plugin manifest, release version, and marketplace catalog |
| [reviews/](reviews/) | Historical reviews, proposals, and fictional test examples with their evidence |

`skills/llm-wiki/` contains the shared skill instructions and supporting files. The Skills CLI installs that folder. A plugin install can also download repository files, including reviews; those reviews are not skill instructions or required references.

**Status: beta.** Plugin discovery and automatic download/activation passed focused tests in Codex and Claude desktop. Small fictional wiki workflows also completed in both apps: creation, feature updates, review and repair, and read-only questions. Initial outputs needed content corrections; independent reviews confirmed the repairs. OpenCode runtime behavior and large production wikis remain unverified. See [VALIDATION.md](VALIDATION.md) for the checks and limits.

Inspired by [Andrej Karpathy's LLM Wiki idea](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). This is an independent community implementation, with no affiliation or endorsement from Karpathy or agent providers.

MIT licence. See [LICENSE](LICENSE).
