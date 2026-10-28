# Awesome Personal Agentic Memory [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of papers, benchmarks, and systems for agents that remember individual users, understand their preferences, and act on personal history.

**[简体中文](README.zh-CN.md)** · **[Results & settings](docs/methods.md)** · **[Visual guide](docs/visual-guide.md)** · **[Contribute](CONTRIBUTING.md)**

Evidence snapshot: **2026-10-28** · **15 benchmark families** · **12 method/configuration records**. Some records group related works.

## Start Here

| Research question | Start with |
| --- | --- |
| Remember facts, updates, and time? | [LongMemEval](https://arxiv.org/abs/2410.10813) |
| Infer preferences and personalize answers? | [PersonaMem-v2](https://arxiv.org/html/2512.06688v1) + [PrefEval](https://arxiv.org/abs/2502.09597) |
| Use memory in actions? | [Mem2ActBench](https://arxiv.org/html/2601.19935v1) |
| Understand representative mechanisms? | [A-MEM](https://arxiv.org/abs/2502.12110), [Hindsight](https://arxiv.org/html/2512.12818v1), [PersonaMem-v2 RL](https://arxiv.org/html/2512.06688v1) |

## Contents

- [Scope](#scope)
- [Benchmark Data Provenance](#benchmark-data-provenance)
- [Benchmarks](#benchmarks)
- [Research Methods](#research-methods)
- [Systems and Implementations](#systems-and-implementations)
- [Watchlist](#watchlist)
- [Evaluation and Results](#evaluation-and-results)
- [Related Lists](#related-lists)
- [Contributing](#contributing)

## Scope

**Personal** means persistent evidence about an individual changes the appropriate answer or action. **Agentic memory** covers writing, organizing, retrieving, updating, and using that evidence.

We distinguish personal outcomes (preferences, profiles, actions), supporting memory components (facts, time, updates), and adjacent diagnostics (general memory or environment experience). Conversational recall alone does not establish effective personalization.

<details>
<summary>Benchmark capability map — Chinese annotations</summary>

![Benchmark capability map](assets/01-benchmarks.png)

[Three-page visual guide](docs/visual-guide.md) · [Editable draw.io](assets/personal-memory-eval.drawio)

</details>

## Benchmark Data Provenance

**Check the data origin before reading scores.** Classify the evaluated personal histories or behaviors as **real-user**, **synthetic**, or **mixed**. For mixed data, the table specifies what the real material actually contributes.

**Human review does not make synthetic data real. Live simulator interaction is not human interaction. Real-data seeds are not untouched individual histories.** This table covers 12 reviewed personal-evaluation datasets; other entries are not classified by name alone.

| Benchmark | Real or synthetic? | How the data are constructed | What scores primarily reflect |
| --- | --- | --- | --- |
| [MemoryCD](https://arxiv.org/html/2603.25973v1) | **Real-user data** | Real Amazon ratings, reviews and cross-domain histories, reorganized into prediction and generation tasks. | Predicting ratings, rankings and review text; not an online user-satisfaction study. |
| [PersonaMem-v3](https://arxiv.org/html/2608.21381v1) | **Mixed data** | Real engagement data are pooled and resampled into synthetic users, then expanded into personas and multi-platform histories by an LLM. | Personalization grounded in behavioral signals, not untouched individual life histories. |
| [PrefEval](https://arxiv.org/html/2502.09597v1) | **Mixed data** | LLM-generated preferences and queries, human-filtered, with real LMSYS chats as distractors. Target preferences are synthetic. | Preference adherence across long contexts; real distractors are not one real user history. |
| [Mem2ActBench](https://arxiv.org/html/2601.19935v1) | **Mixed data** | Combines ToolACE, BFCL and OASST1 material into fact chains; constructs grounded tool arguments before generating underspecified queries. | Memory-grounded argument completion; main experiments supply the tool and do not measure executed task success. |
| [PersonaBench](https://arxiv.org/html/2502.20616v1) | **Synthetic data** | Synthetic persona seeds → social graphs and profiles → private documents → personal questions. | Recovering personal attributes and relationships from documents. |
| [PersonaMem v1](https://arxiv.org/html/2504.14225v1) | **Synthetic data** | PersonaHub seeds → preference timelines → simulated sessions → questions about the current state. | Tracking and using currently valid user preferences. |
| [PersonaMem-v2](https://arxiv.org/html/2512.06688v1) | **Synthetic data** | Synthetic personas and preferences → implicit-cue conversations → QA; generated and filtered with GPT-5. | Implicit preference inference, attribution and personalized responses. |
| [PerMemBench](https://arxiv.org/html/2605.25535v1) | **Synthetic data** | Synthetic Nemotron personas → long-horizon/transient use profiles → projects and reference memories → simulated dialogues. | Retention of designated useful personal memories, not final answer quality. |
| [AMemGym](https://arxiv.org/html/2603.01966v1) | **Synthetic data** | Synthetic personas → evaluation questions → evolving state variables → live interaction with a simulated user. | State maintenance in ongoing interaction; evaluation users are simulated. |
| [PraxisMemBench](https://arxiv.org/html/2610.20022v1) | **Synthetic data** | Synthetic personas and events combined with engineered stateful applications, SOPs and execution-validated tasks. | Coupled personal/procedural memory; diagnostic SR and strict execution success must be distinguished. |
| [OP-Bench](https://arxiv.org/html/2601.13722v2) | **Synthetic data** | Extracts profiles from synthetic LoCoMo conversations, then generates and human-reviews over-personalization probes. | Stress testing irrelevant references, repetition and sycophancy. |
| [PersistBench](https://arxiv.org/html/2602.01146v1) | **Synthetic data** | Generates memory-query pairs, searches for failure-inducing combinations, then verifies them with human reviewers. | Memory-misuse stress testing; failure rates are not natural-use prevalence. |

Based on paper/appendix descriptions, not a record-level audit of every released dataset. Reviewed 2026-10-28. Structured records: [benchmark-provenance.json](data/benchmark-provenance.json).

## Benchmarks

Each entry links to a primary source and an evidence card covering scale, metrics, and limitations.

### Facts and History

| Year | Work | Focus | Resources |
| --- | --- | --- | --- |
| 2024 | **LoCoMo** | Cross-session facts, multi-hop and temporal reasoning; distinguish original metrics from later QA protocols. | [Source](https://github.com/snap-research/locomo) · [Evidence](docs/benchmarks.md#1-locomo) |
| 2024 / ICLR 2025 | **LongMemEval** | Long-term facts, temporal changes, updates and abstention; keep S, M and oracle separate. | [Source](https://arxiv.org/abs/2410.10813) · [Code](https://github.com/xiaowu0162/LongMemEval) · [Evidence](docs/benchmarks.md#2-longmemeval) |
| 2025 / 2026 | **BEAM** | Conversational memory at extreme history lengths; compare within the same length setting. | [Source](https://arxiv.org/abs/2510.27246) · [Evidence](docs/benchmarks.md#3-beam) |
| 2025 | **ConvoMem** | Facts, preferences, temporal changes and implicit connections across conversation history. | [Source](https://arxiv.org/abs/2511.10523) · [Evidence](docs/benchmarks.md#4-convomem) |

### Preferences and User Understanding

| Year | Work | Focus | Resources |
| --- | --- | --- | --- |
| 2025 | **PrefEval** | Explicit and implicit preference inference and adherence. | [Source](https://arxiv.org/abs/2502.09597) · [Evidence](docs/benchmarks.md#5-prefeval) |
| 2025 | **PersonaMem v1** | Evolving user profiles and personalized response selection. | [Source](https://arxiv.org/abs/2504.14225) · [Code](https://github.com/bowen-upenn/PersonaMem) · [Evidence](docs/benchmarks.md#6-personamem-v1) |
| 2025 | **PersonaMem-v2** | Implicit preferences, attribution, changes and forgetting requests; separate MCQ from open-ended scoring. | [Source](https://arxiv.org/html/2512.06688v1) · [Evidence](docs/benchmarks.md#7-personamem-v2) |
| 2026 | **MemoryCD** | Cross-domain recommendation and review tasks based on behavioral histories. | [Source](https://arxiv.org/html/2603.25973v1) · [Evidence](docs/benchmarks.md#11-memorycd) |
| 2026 | **KnowMe-Bench** | Personal understanding from autobiographical narratives, including subjective perspectives. | [Source](https://arxiv.org/abs/2601.04745) · [Evidence](docs/benchmarks.md#12-knowme-bench) |

### Actions and Multiple Sources

| Year | Work | Focus | Resources |
| --- | --- | --- | --- |
| 2026 | **PersonaMem-v3** | Cross-platform user evidence, agentic tasks and proactive intervention. | [Source](https://arxiv.org/html/2608.21381v1) · [Evidence](docs/benchmarks.md#8-personamem-v3) |
| 2026 | **Mem2ActBench** | Historical information used in tool arguments; the main setting supplies the gold tool. | [Source](https://arxiv.org/html/2601.19935v1) · [Code & data](https://github.com/Cantaloupe-M/Mem2ActBench) · [Evidence](docs/benchmarks.md#9-mem2actbench) |
| 2026 | **LifeBench** | Longitudinal, multi-source life traces; specifically arXiv:2603.03781. | [Source](https://arxiv.org/abs/2603.03781) · [Evidence](docs/benchmarks.md#10-lifebench) |

### Adjacent Diagnostics

| Year | Work | Focus | Resources |
| --- | --- | --- | --- |
| 2025 / 2026 | **MemoryAgentBench** | Incremental retrieval, learning, long-range understanding and selective forgetting. | [Source](https://arxiv.org/abs/2507.05257) · [Evidence](docs/benchmarks.md#13-memoryagentbench) |
| 2023–2024 | **LaMP / LongLaMP** | Personalized classification and generation; complements memory-lifecycle evaluation. | [Source](https://arxiv.org/abs/2304.11406) · [2](https://arxiv.org/abs/2407.11016) · [Evidence](docs/benchmarks.md#14-lamp--longlamp) |
| 2026 | **LongMemEval-V2** | Web-agent experience and environment memory; a different scope from personal-chat LongMemEval. | [Source](https://arxiv.org/abs/2605.12493) · [Code](https://github.com/xiaowu0162/LongMemEval-V2) · [Evidence](docs/benchmarks.md#15-longmemeval-v2) |

## Research Methods

Organized by mechanism to help select baselines; ordering does not indicate performance rank.

### Learned Memory Management

| Work | Focus | Resources |
| --- | --- | --- |
| **PersonaMem-v2 RL Agentic Memory** | Learns sequential compression and updates of bounded user memory. | [Source](https://arxiv.org/html/2512.06688v1) · [Evidence](docs/methods.md#1-personamem-v2-rl-agentic-memory) |

### Structured Memory and Retrieval

| Work | Focus | Resources |
| --- | --- | --- |
| **A-MEM** | Linked notes with evolving memory structure; evaluated on tool arguments in Mem2ActBench. | [Source](https://arxiv.org/abs/2502.12110) · [System](https://github.com/agiresearch/A-mem) · [Paper experiments](https://github.com/WujiangXu/A-mem) · [Evidence](docs/methods.md#8-a-mem) |
| **Hindsight** | Retain, recall and reflect operations over structured evidence and beliefs. | [Source](https://arxiv.org/html/2512.12818v1) · [Code](https://github.com/vectorize-io/hindsight) · [Evidence](docs/methods.md#2-hindsight) |
| **EverMemOS** | Memory cells and scenes support organized evidence recollection. | [Source](https://arxiv.org/html/2601.02163v1) · [Current repo](https://github.com/EverMind-AI/EverOS) · [Evidence](docs/methods.md#3-evermemos) |

### Graph and Reinforcement Learning Comparisons

| Work | Focus | Resources |
| --- | --- | --- |
| **MAGMA / Memory-R1** | MAGMA: multi-graph retrieval. Memory-R1: reinforcement learning for management and evidence selection. | [Source](https://arxiv.org/abs/2601.03236) · [2](https://arxiv.org/abs/2508.19828) · [Evidence](docs/methods.md#9-magma--memory-r1) |

## Systems and Implementations

| Work | Focus | Resources |
| --- | --- | --- |
| **Mastra Observational Memory** | Observer and reflector processes maintain compact chronological observations. | [Source](https://mastra.ai/research/observational-memory) · [Evidence](docs/methods.md#4-mastra-observational-memory) |
| **Mem0 · 2026 temporal update** | Time-aware fact updates and retrieval; distinguish product reports from paper settings. | [Source](https://mem0.ai/blog/introducing-temporal-reasoning-in-mem0) · [Evidence](docs/methods.md#5-mem0--2026-temporal-update) |
| **Zep · 2026 research page** | Temporal graph memory and context assembly; product scores are not Graphiti-only scores. | [Source](https://www.getzep.com/research/) · [Evidence](docs/methods.md#6-zep--2026-research-page) |

Additional source-code entry points:

- [A-MEM system](https://github.com/agiresearch/A-mem) · [A-MEM paper experiments](https://github.com/WujiangXu/A-mem). The library and paper experiments are separate repositories.
- [Hindsight](https://github.com/vectorize-io/hindsight). Current project repository; reproduction requires a pinned version.
- [EverOS](https://github.com/EverMind-AI/EverOS). The paper-linked EverMemOS repository now redirects here; current HEAD is not a pinned paper implementation.

## Watchlist

Recent work, configuration-level comparisons, and results needing further protocol checks.

| Work | Focus | Resources |
| --- | --- | --- |
| **Agent Zero Memory** | Event timelines, entity graphs and hierarchical documents; reported best settings need matched comparisons. | [Source](https://arxiv.org/html/2608.29606v1) · [Evidence](docs/methods.md#7-agent-zero-memory) |
| **AgentMemRec / FlexA-Mem** | AgentMemRec: memory selection as recommendation. FlexA-Mem: budget-adaptive history recovery. | [Source](https://arxiv.org/abs/2610.34673) · [2](https://arxiv.org/abs/2610.33274) · [Evidence](docs/methods.md#10-agentmemrec--flexa-mem) |
| **PersonaMem-v3 agentic search configurations** | Cross-platform search evaluated as model plus harness configurations, not an isolated memory module. | [Source](https://arxiv.org/html/2608.21381v1) · [Evidence](docs/methods.md#11-personamem-v3-agentic-search-configurations) |
| **Supermemory** | Retrieval and memory organization; the cited 97% figure is labelled Recall@20, not QA accuracy. | [Source](https://supermemory.ai/research/) · [Evidence](docs/methods.md#12-supermemory) |

## Evaluation and Results

**Starter battery: LongMemEval-S + PersonaMem-v2 + Mem2ActBench.** Report facts, personalization, and tool-argument grounding separately. This is an editorial selection, not a standardized aggregate score.

| Need | Resource |
| --- | --- |
| Tasks, scale, metrics and limitations | [Benchmark evidence cards](docs/benchmarks.md) |
| Reported scores, models, judges and caveats | [Method results and settings](docs/methods.md) |
| Matched comparisons and a reusable result template | [Evaluation protocol](docs/evaluation-protocol.md) |
| Structured review records | [catalog.json](data/catalog.json) |

Results are paper- or author-reported, with no independent reproduction here. Mechanism descriptions are not complete code audits. Keep retrieval, QA, preference adherence, and task success separate, and distinguish macro from per-question averages. Detailed evidence notes are currently in Chinese.

## Related Lists

- [Awesome Personalized AI](https://github.com/LikeACloud7/awesome-personalized-ai) - Broader personalization research and evaluation.
- [Awesome Personalized Graph Memory](https://github.com/icedpanda/awesome-personalized-graph-memory) - Graph-based personal memory.
- [Awesome Agent Memory](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory) - General agent memory systems and research.

## Contributing

Add a resource with its personal-memory relevance, primary source, and evaluation limits. See the [contribution guide](CONTRIBUTING.md), [roadmap](TODO.md), and [change log](CHANGELOG.md).

Structure inspired by [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM): reading highlights, categorized research tables, and separate evaluation and implementation resources. See [design notes](docs/design-references.md).
