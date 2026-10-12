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

Use the [Skills CLI](https://github.com/vercel-labs/skills) to install for the current project:

```bash
npx skills add https://github.com/ip1618/source-grounded-llm-wiki --skill llm-wiki
```

To choose an agent, append one of these options:

| Agent | Option |
|---|---|
| Claude Code | `-a claude-code` |
| OpenCode | `-a opencode` |
| Codex | `-a codex` |

Add `-g` to install across projects. Check for an existing skill named `llm-wiki` before installing, and back it up rather than overwriting an unrelated skill.

For manual installation, copy [skills/llm-wiki](skills/llm-wiki) into the skill directory supported by your agent. Consult that agent's documentation for the correct location.

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
| [reviews/](reviews/) | Historical reviews, proposals, and fictional test examples with their evidence |

Only `skills/llm-wiki/` is the skill package. The review material is not installed with it.

**Status: beta.** The recorded checks used Codex and small fictional examples. Claude Code and OpenCode runtime behavior, and use on large production wikis, remain untested. Shared instructions do not guarantee identical behavior across agents. See [VALIDATION.md](VALIDATION.md) for the checks and limits.

Inspired by [Andrej Karpathy's LLM Wiki idea](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). This is an independent community implementation, with no affiliation or endorsement from Karpathy or agent providers.

MIT licence. See [LICENSE](LICENSE).
