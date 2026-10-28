"""Build both curated homepages from catalog metadata. Standard library only."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'data/catalog.json').read_text(encoding='utf-8'))
def slug(s):
    return re.sub(r'[^\w\s-]', '', s.lower()).replace(' ', '-')
def evidence(kind,i):
    x=d[kind][i]
    return f'docs/{kind}.md#'+slug(f'{i+1}. {x["name"]}')
def res(x,zh):
    label=('原文' if zh else 'Source')
    a=[f'[{label}]({x["url"]})']
    if x.get('url2'): a.append(f'[2]({x["url2"]})')
    a += [f'[{r["label"]}]({r["url"]})' for r in x.get('resources',[])]
    return ' · '.join(a)
def table(kind,idx,zh):
    heads=['时间','工作','研究重点','资料'] if kind=='benchmarks' else ['工作','研究重点','资料']
    if not zh: heads=['Year','Work','Focus','Resources'] if kind=='benchmarks' else ['Work','Focus','Resources']
    rows=['| '+' | '.join(heads)+' |','| '+' | '.join(['---']*len(heads))+' |']
    for i in idx:
        x=d[kind][i]
        summary=x['task' if kind=='benchmarks' else 'idea'] if zh else x['summary_en']
        cells=[f'**{x["name"]}**',summary,res(x,zh)+' · '+f'[{"评测详情" if zh else "Evidence"}]({evidence(kind,i)})']
        if kind=='benchmarks': cells.insert(0,x['year'])
        rows.append('| '+' | '.join(s.replace('|',r'\|').replace('\n',' ') for s in cells)+' |')
    return '\n'.join(rows)
def provenance(zh):
    data=json.loads((ROOT/'data/benchmark-provenance.json').read_text(encoding='utf-8'))
    labels={'real':('真人数据','Real-user data'),'mixed':('混合数据','Mixed data'),'synthetic':('合成数据','Synthetic data')}
    if zh:
        intro=['## Benchmark 数据来源',
            '**先看数据来自谁，再看榜单分数。** 按被评估的个人历史 / 行为来源分类：**真人数据**来自实际用户记录；**合成数据**由人设、脚本或模拟器构造；**混合数据**结合真实语料与合成内容，具体作用见表。',
            '**人工审核 ≠ 真人数据；模拟用户实时交互 ≠ 真人交互；真实数据作种子 ≠ 原始真人完整轨迹。** 本表先覆盖已核对的 12 项个人场景评测，其余条目不据名称推断。',
            '| Benchmark | 真人还是合成？ | 数据怎样构造 | 榜单主要反映什么 |',
            '| --- | --- | --- | --- |']
    else:
        intro=['## Benchmark Data Provenance',
            '**Check the data origin before reading scores.** Classify the evaluated personal histories or behaviors as **real-user**, **synthetic**, or **mixed**. For mixed data, the table specifies what the real material actually contributes.',
            '**Human review does not make synthetic data real. Live simulator interaction is not human interaction. Real-data seeds are not untouched individual histories.** This table covers 12 reviewed personal-evaluation datasets; other entries are not classified by name alone.',
            '| Benchmark | Real or synthetic? | How the data are constructed | What scores primarily reflect |',
            '| --- | --- | --- | --- |']
    for x in data['benchmarks']:
        lang='zh' if zh else 'en'
        intro.append('| ['+x['name']+']('+x['source']+') | **'+labels[x['origin']][0 if zh else 1]+'** | '+x['construction_'+lang]+' | '+x['interpretation_'+lang]+' |')
    intro.append(('依据论文正文/附录描述，尚未逐条审计全部发布数据。分类快照：2026-10-28。结构化记录：[benchmark-provenance.json](data/benchmark-provenance.json)。' if zh else 'Based on paper/appendix descriptions, not a record-level audit of every released dataset. Reviewed 2026-10-28. Structured records: [benchmark-provenance.json](data/benchmark-provenance.json).'))
    return '\n\n'.join(intro[:3])+'\n\n'+'\n'.join(intro[3:-1])+'\n\n'+intro[-1]

for zh in [False,True]:
    parts=['# Awesome Personal Agentic Memory [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)']
    if zh:
        parts += ['精选个人助手长期记忆的论文、benchmark 和系统，关注 Agent 如何记住用户、理解用户，并根据个人历史采取合适行动。',
        '**[English](README.md)** · **[评测结果与条件](docs/methods.md)** · **[图解](docs/visual-guide.md)** · **[贡献](CONTRIBUTING.md)**',
        '资料快照：**2026-10-28** · **15 个 benchmark 家族** · **12 条方法/配置记录**。部分条目包含多个相关工作。',
        '## 从这里开始',
        '| 研究问题 | 起点 |\n| --- | --- |\n| 能记住用户事实、更新和时间吗？ | [LongMemEval](https://arxiv.org/abs/2410.10813) |\n| 能理解隐式偏好并个性化回答吗？ | [PersonaMem-v2](https://arxiv.org/html/2512.06688v1) + [PrefEval](https://arxiv.org/abs/2502.09597) |\n| 能把记忆用于行动吗？ | [Mem2ActBench](https://arxiv.org/html/2601.19935v1) |\n| 哪些机制值得先读？ | [A-MEM](https://arxiv.org/abs/2502.12110)、[Hindsight](https://arxiv.org/html/2512.12818v1)、[PersonaMem-v2 RL](https://arxiv.org/html/2512.06688v1) |',
        '## 目录',
        '- [研究范围](#研究范围)\n- [Benchmark 数据来源](#benchmark-数据来源)\n- [Benchmarks](#benchmarks)\n- [研究方法](#研究方法)\n- [系统与实现](#系统与实现)\n- [近期观察](#近期观察)\n- [评测与结果](#评测与结果)\n- [相关清单](#相关清单)\n- [贡献](#贡献)',
        '## 研究范围',
        '**Personal**：历史中的个人证据会改变应当给出的回答或行动。**Agentic Memory**：Agent 对这些证据进行写入、组织、检索、更新和使用。',
        '按三个层次标注用途：个人结果（偏好、画像、行动）、记忆组件（事实、时间、更新）和邻接诊断（通用记忆或环境经验）。事实问答能力是个人助手的基础，但不能单独证明个性化行动有效。',
        '<details>\n<summary>展开 Benchmark 能力地图（可编辑图见链接）</summary>\n\n![Benchmark 能力地图](assets/01-benchmarks.png)\n\n[全部三页图解](docs/visual-guide.md) · [可编辑 draw.io](assets/personal-memory-eval.drawio)\n\n</details>',
        provenance(zh),'## Benchmarks','每项附原始来源和详细证据卡，包含规模、指标与适用边界。']
    else:
        parts += ['A curated list of papers, benchmarks, and systems for agents that remember individual users, understand their preferences, and act on personal history.',
        '**[简体中文](README.zh-CN.md)** · **[Results & settings](docs/methods.md)** · **[Visual guide](docs/visual-guide.md)** · **[Contribute](CONTRIBUTING.md)**',
        'Evidence snapshot: **2026-10-28** · **15 benchmark families** · **12 method/configuration records**. Some records group related works.',
        '## Start Here',
        '| Research question | Start with |\n| --- | --- |\n| Remember facts, updates, and time? | [LongMemEval](https://arxiv.org/abs/2410.10813) |\n| Infer preferences and personalize answers? | [PersonaMem-v2](https://arxiv.org/html/2512.06688v1) + [PrefEval](https://arxiv.org/abs/2502.09597) |\n| Use memory in actions? | [Mem2ActBench](https://arxiv.org/html/2601.19935v1) |\n| Understand representative mechanisms? | [A-MEM](https://arxiv.org/abs/2502.12110), [Hindsight](https://arxiv.org/html/2512.12818v1), [PersonaMem-v2 RL](https://arxiv.org/html/2512.06688v1) |',
        '## Contents',
        '- [Scope](#scope)\n- [Benchmark Data Provenance](#benchmark-data-provenance)\n- [Benchmarks](#benchmarks)\n- [Research Methods](#research-methods)\n- [Systems and Implementations](#systems-and-implementations)\n- [Watchlist](#watchlist)\n- [Evaluation and Results](#evaluation-and-results)\n- [Related Lists](#related-lists)\n- [Contributing](#contributing)',
        '## Scope',
        '**Personal** means persistent evidence about an individual changes the appropriate answer or action. **Agentic memory** covers writing, organizing, retrieving, updating, and using that evidence.',
        'We distinguish personal outcomes (preferences, profiles, actions), supporting memory components (facts, time, updates), and adjacent diagnostics (general memory or environment experience). Conversational recall alone does not establish effective personalization.',
        '<details>\n<summary>Benchmark capability map — Chinese annotations</summary>\n\n![Benchmark capability map](assets/01-benchmarks.png)\n\n[Three-page visual guide](docs/visual-guide.md) · [Editable draw.io](assets/personal-memory-eval.drawio)\n\n</details>',
        provenance(zh),'## Benchmarks','Each entry links to a primary source and an evidence card covering scale, metrics, and limitations.']
    for en,cn,idx in [('Facts and History','事实与历史',[0,1,2,3]),('Preferences and User Understanding','偏好与用户理解',[4,5,6,10,11]),('Actions and Multiple Sources','行动与多源信息',[7,8,9]),('Adjacent Diagnostics','邻接能力诊断',[12,13,14])]:
        parts += ['### '+(cn if zh else en),table('benchmarks',idx,zh)]
    parts += [('## 研究方法' if zh else '## Research Methods'),('按机制组织，便于选择对照实验；条目顺序不代表成绩排名。' if zh else 'Organized by mechanism to help select baselines; ordering does not indicate performance rank.')]
    for en,cn,idx in [('Learned Memory Management','学习式记忆管理',[0]),('Structured Memory and Retrieval','结构化记忆与检索',[7,1,2]),('Graph and Reinforcement Learning Comparisons','图结构与强化学习对照',[8])]:
        parts += ['### '+(cn if zh else en),table('methods',idx,zh)]
    parts += [('## 系统与实现' if zh else '## Systems and Implementations'),table('methods',[3,4,5],zh)]
    parts += [('已核实的源码入口：' if zh else 'Additional source-code entry points:'),
    '- [A-MEM system](https://github.com/agiresearch/A-mem) · [A-MEM paper experiments](https://github.com/WujiangXu/A-mem). '+('系统库和论文实验仓库分开。' if zh else 'The library and paper experiments are separate repositories.')+'\n'+
    '- [Hindsight](https://github.com/vectorize-io/hindsight). '+('当前项目入口，复现需要固定版本。' if zh else 'Current project repository; reproduction requires a pinned version.')+'\n'+
    '- [EverOS](https://github.com/EverMind-AI/EverOS). '+('论文的 EverMemOS 仓库链接目前跳转至此；不把当前代码默认视为论文版本。' if zh else 'The paper-linked EverMemOS repository now redirects here; current HEAD is not a pinned paper implementation.'),
    ('## 近期观察' if zh else '## Watchlist'),('新作、配置级比较与指标待核条目，保留在观察区。' if zh else 'Recent work, configuration-level comparisons, and results needing further protocol checks.'),table('methods',[6,9,10,11],zh)]
    if zh:
        parts += ['## 评测与结果',
        '**起步组合：LongMemEval-S + PersonaMem-v2 + Mem2ActBench。** 分别衡量事实、个性化和工具参数；这是本清单的选型建议，不合成为统一总分。',
        '| 要查什么 | 入口 |\n| --- | --- |\n| 各 benchmark 测什么、有哪些限制 | [Benchmark 证据卡](docs/benchmarks.md) |\n| 方法报告了多少分、用了什么模型与 judge | [方法成绩与条件](docs/methods.md) |\n| 如何固定预算、模型、指标并记录复现 | [评测协议与结果模板](docs/evaluation-protocol.md) |\n| 结构化原始整理 | [catalog.json](data/catalog.json) |',
        '成绩均为论文或作者报告，尚未独立复跑；机制说明也未全部核到源码。Recall@k、QA accuracy、偏好遵循率与任务成功率分开记录，宏平均与逐题平均分开记录。',
        '## 相关清单']
    else:
        parts += ['## Evaluation and Results',
        '**Starter battery: LongMemEval-S + PersonaMem-v2 + Mem2ActBench.** Report facts, personalization, and tool-argument grounding separately. This is an editorial selection, not a standardized aggregate score.',
        '| Need | Resource |\n| --- | --- |\n| Tasks, scale, metrics and limitations | [Benchmark evidence cards](docs/benchmarks.md) |\n| Reported scores, models, judges and caveats | [Method results and settings](docs/methods.md) |\n| Matched comparisons and a reusable result template | [Evaluation protocol](docs/evaluation-protocol.md) |\n| Structured review records | [catalog.json](data/catalog.json) |',
        'Results are paper- or author-reported, with no independent reproduction here. Mechanism descriptions are not complete code audits. Keep retrieval, QA, preference adherence, and task success separate, and distinguish macro from per-question averages. Detailed evidence notes are currently in Chinese.',
        '## Related Lists']
    parts += ['- [Awesome Personalized AI](https://github.com/LikeACloud7/awesome-personalized-ai) - '+('广义个性化研究与评测。' if zh else 'Broader personalization research and evaluation.')+'\n'+
    '- [Awesome Personalized Graph Memory](https://github.com/icedpanda/awesome-personalized-graph-memory) - '+('图结构个人记忆。' if zh else 'Graph-based personal memory.')+'\n'+
    '- [Awesome Agent Memory](https://github.com/TeleAI-UAGI/Awesome-Agent-Memory) - '+('通用 Agent Memory 系统与研究。' if zh else 'General agent memory systems and research.')]
    if zh:
        parts += ['## 贡献','补充条目时，请说明个人场景用途、原始来源和评测边界。见[贡献规范](CONTRIBUTING.md)、[待办](TODO.md)与[更新记录](CHANGELOG.md)。',
        '页面结构参考 [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM)，采用重点入口、分类论文表和独立评测/实现资源区。见[设计说明](docs/design-references.md)。']
    else:
        parts += ['## Contributing','Add a resource with its personal-memory relevance, primary source, and evaluation limits. See the [contribution guide](CONTRIBUTING.md), [roadmap](TODO.md), and [change log](CHANGELOG.md).',
        'Structure inspired by [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM): reading highlights, categorized research tables, and separate evaluation and implementation resources. See [design notes](docs/design-references.md).']
    (ROOT/('README.zh-CN.md' if zh else 'README.md')).write_text('\n\n'.join(parts)+'\n',encoding='utf-8')
print('Rendered matching English and Chinese homepages.')
