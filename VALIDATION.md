# Validation report

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
