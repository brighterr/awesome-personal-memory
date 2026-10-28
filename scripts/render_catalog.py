"""Render detailed evidence cards from the curated catalog; standard library only."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'data/catalog.json').read_text(encoding='utf-8'))
date = data['as_of']
benchmarks = ['# Benchmark 证据卡', '[返回首页](../README.md) · [中文导读](../README.zh-CN.md)', f'资料快照：{date}。来自前期调研记录；未独立复跑。本页由 `data/catalog.json` 生成，规模与定义按所链接来源解释。']
for i, item in enumerate(data['benchmarks'], 1):
    links = f'- 来源：[原始来源]({item["url"]})'
    if item.get('url2'):
        links += f' · [第二来源]({item["url2"]})'
    for r in item.get('resources', []):
        links += f' · [{r["label"]}]({r["url"]})（{r["note"]} 链接核对：{r["link_checked_on"]}；未执行或审计代码。）'
    benchmarks.extend([f'## {i}. {item["name"]}', f'**类别**：{item["group"]} · **阅读定位**：{item["priority"]} · **时间标记**：{item["year"]}', f'- 任务：{item["task"]}', f'- 规模：{item["scale"]}', f'- 指标：{item["metric"]}', f'- 限制：{item["limit"]}', links])
methods = ['# 方法与成绩证据卡', '[返回首页](../README.md) · [评测协议](evaluation-protocol.md)', f'资料快照：{date}。所有成绩均为论文或作者报告，**没有本仓库独立复现成绩**。顺序按研究用途组织，不代表排名；不同模型、judge、数据子集或指标不能直接排序。机制说明来自文献，尚未逐项核验源码。']
for i, item in enumerate(data['methods'], 1):
    links = f'- 来源：[主要来源]({item["url"]})'
    if item.get('url2'):
        links += f' · [第二来源]({item["url2"]})'
    if item.get('evidence'):
        links += f' · [第三方评测来源]({item["evidence"]})'
    for r in item.get('resources', []):
        links += f' · [{r["label"]}]({r["url"]})（{r["note"]} 链接核对：{r["link_checked_on"]}；未执行或审计代码。）'
    methods.extend([f'## {i}. {item["name"]}', f'**阅读定位**：{item["type"]}', f'- 机制：{item["idea"]}', f'- 报告结果：{item["result"]}', f'- 评测条件：{item["setting"]}', f'- 解释边界：{item["caveat"]}', links])
for name, sections in [('benchmarks.md', benchmarks), ('methods.md', methods)]:
    (ROOT / 'docs' / name).write_text('\n\n'.join(sections) + '\n', encoding='utf-8')
print('Rendered benchmark and method evidence cards.')
