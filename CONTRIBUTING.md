# Contributing

Thank you for helping improve this guide. Add resources because they help a reader understand, build, or evaluate personal agent memory.

## Inclusion criteria

- Explain the connection to persistent personal evidence or user-dependent outcomes.
- Link to a primary paper, official dataset, repository, or technical report.
- Add a concise description of the task or mechanism and a concrete reason to read it.
- Keep personal outcomes, memory components, and adjacent diagnostics distinguishable.
- Identify preprints, vendor reports, and unresolved limitations where relevant.
- Popularity alone is not evidence of quality; recent research can enter the watchlist.

## Updating an entry

1. Update `data/catalog.json` for benchmark or method evidence. Preserve the source URLs and caveats; record a per-entry `reviewed_on` date only when you have actually checked its sources.
2. Run `python3 scripts/render_catalog.py` and `python3 scripts/render_readme.py` to refresh the evidence cards and both homepages.
3. Keep `summary_en` concise. Add official implementation links under `resources`, with the link-check date and scope. Update the category selection in `scripts/render_readme.py` when adding a new record; both language editions must cover the same entries.
4. Add meaningful changes to `CHANGELOG.md`.
5. Run `python3 scripts/check_catalog.py`.

The local check validates required fields, duplicate record names, source URL syntax, local file links, and explicit/Markdown heading anchors. It does not verify external availability, scientific correctness, or reproducibility.

## Reporting results

Use the [result-card template](docs/evaluation-protocol.md). Include benchmark version, split, sample count, answer and memory models, judge, metric aggregation, budgets, source, and limitations. Use “not reported” for missing fields.

Distinguish source-reported mechanisms from code-audited implementation. For a code audit, cite a commit, file, and line. Distinguish author reports from independent reproductions, and provide configs and raw outputs for the latter.

Do not merge incompatible scores into a leaderboard. Explain whether code or data are available without treating their availability as proof of reproducibility. Disclose affiliation when submitting your own work. AI assistance should be disclosed; do not claim manual verification or reproduction that did not happen.

## Maintenance

Correct dead links with an official replacement or record the loss of availability. Keep historical versions distinguishable. Before publishing this initial draft, settle licensing and review the outstanding items in [TODO.md](TODO.md).
