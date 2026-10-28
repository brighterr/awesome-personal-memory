# Personal Memory 评测协议

[返回首页](../README.md) · [Benchmark 证据卡](benchmarks.md) · [方法证据卡](methods.md)

这是本仓库提出的实验记录与比较建议，不是已有 benchmark 的官方协议。各 benchmark 的实际运行应以对应官方版本为准。

## 先确定要支持的结论

| 结论 | 需要的证据 | 不足以单独支持结论的指标 |
| --- | --- | --- |
| 能记住用户历史 | 事实、时间、跨会话与拒答结果 | 仅向量检索 Recall@k |
| 能理解用户 | 偏好推断、当前状态、归属辨别、个性化输出 | 普通知识问答准确率 |
| 能帮助用户行动 | 工具参数正确性、执行结果和端到端任务成功率 | 给定正确工具后的参数分数 |
| 能处理用户变化 | 新旧事实冲突、时间有效性、更新与遗忘 | 静态事实检索 |
| 能在部署中持续使用 | 生命周期成本、延迟、存储、错误传播与用户反馈 | 压缩后 token 数 |

## 推荐的起步实验

LongMemEval-S、PersonaMem-v2、Mem2ActBench 作为三个独立结果面板。新增 PrefEval 补充偏好遵循；根据场景加入多平台、推荐或个人理解评测。选择依据见[benchmark 卡片](benchmarks.md)，不合并不相容的指标。

至少比较：无记忆、全上下文（标明截断策略）、简单检索（标明 chunk 与 top-k）和候选方法。固定回答模型、数据划分、judge、提示词与预算。训练式方法必须隔离训练与测试用户及其历史。

## 每条结果必须带的字段

| 字段 | 记录内容 |
| --- | --- |
| 数据 | benchmark、版本、split、题目数量、排除规则 |
| 模型 | 回答模型、记忆写入模型、检索器、embedding、reranker |
| 记忆预算 | 写入、检索、返回上下文 token 限制与压缩策略 |
| 打分 | 原始指标、judge 版本、rubric、宏平均或逐题平均 |
| 成本 | 初始化、增量写入、更新、检索、回答成本；查询次数与摊销方式 |
| 延迟 | 各阶段耗时；在有足够样本时报告 p50 / p95 |
| 来源 | 论文表号/章节或代码 commit、配置与原始输出路径 |
| 证据身份 | 作者报告、第三方评测、本仓库复现、仅摘要范围核对 |
| 不确定性 | 重复次数、随机性；适当时使用配对 bootstrap 区间 |

字段未公开就填写“未报告”，不要推断一个值来补齐表格。

## 需要保留的区分

- Recall@k 与最终回答 accuracy。
- 类别宏平均与按题目计算的总体 accuracy。
- LoCoMo 原始指标与后续 LLM judge 协议。
- MCQ 与开放式生成。
- 产品整套系统与单个开源组件。
- model + harness 配置效果与 memory 模块的因果贡献。
- 论文描述的算法与代码实现；源码核对时保存 commit、文件和行号。

## 可复制的结果卡

```text
Method / version:
Benchmark / version / split / N:
Answer model:
Memory-building model:
Retriever / embedding / reranker:
Memory budget / retrieved token budget:
Judge / rubric / aggregation:
Metric and result:
Baseline under the same setting:
Runs / uncertainty:
Cost / latency:
Paper section or code commit + file + lines:
Raw outputs / configuration:
Evidence type:
Known limitations / unreported fields:
```
