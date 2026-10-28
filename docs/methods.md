# 方法与成绩证据卡

[返回首页](../README.md) · [评测协议](evaluation-protocol.md)

资料快照：2026-10-28。所有成绩均为论文或作者报告，**没有本仓库独立复现成绩**。顺序按研究用途组织，不代表排名；不同模型、judge、数据子集或指标不能直接排序。机制说明来自文献，尚未逐项核验源码。

## 1. PersonaMem-v2 RL Agentic Memory

**阅读定位**：直接个性化证据

- 机制：GRPO 学习顺序压缩与更新一份有界、可读的用户记忆。

- 报告结果：MCQ 55.2%；open-ended 60.7%。

- 评测条件：Qwen3-4B；32k 历史压到约 2k 记忆；论文 §4.3。

- 解释边界：同论文 GRPO 长上下文为 53.8% / 56.0%；只在该设置比较，不能外推为全领域最优。

- 来源：[主要来源](https://arxiv.org/html/2512.06688v1)

## 2. Hindsight

**阅读定位**：长期 QA 强基线

- 机制：事实、经历、摘要、信念分层；retain / recall / reflect，时间与实体感知检索。

- 报告结果：LongMemEval-S 91.4%；LoCoMo 89.61%。

- 评测条件：论文 Gemini-3 Pro 回答配置；judge 为 GPT-OSS-120B。S=500 题；论文表 3–4。

- 解释边界：论文历史成绩，不冒充当前统一榜第一；同骨干 OSS-20B 对照为 39.0→83.6%，更能说明记忆贡献。

- 来源：[主要来源](https://arxiv.org/html/2512.12818v1) · [Code](https://github.com/vectorize-io/hindsight)（Current project repository; pin the paper implementation for reproduction. 链接核对：2026-10-28；未执行或审计代码。）

## 3. EverMemOS

**阅读定位**：长期 QA 强基线

- 机制：MemCells → MemScenes → agentic recollection，把片段整合为主题场景并重建证据。

- 报告结果：LoCoMo 93.05%（GPT-4.1-mini）；86.76%（GPT-4o-mini）。

- 评测条件：同论文 LoCoMo 对照；1,540 题；三 judge 平均，两个辅助 judge 未在该段具名。

- 解释边界：优先看同表增益；不可直接与单一 judge 的 93% 比较。LongMemEval 表的基线来自外部榜单。

- 来源：[主要来源](https://arxiv.org/html/2601.02163v1) · [Current repo](https://github.com/EverMind-AI/EverOS)（The paper-linked EverMemOS URL redirects to EverOS; current HEAD is not a pinned paper version. 链接核对：2026-10-28；未执行或审计代码。）

## 4. Mastra Observational Memory

**阅读定位**：工程高分候选

- 机制：Observer / Reflector 维护日期化观察日志，形成稳定可缓存上下文。

- 报告结果：LongMemEval-S 94.87%（GPT-5-mini）；84.23%（GPT-4o）。

- 评测条件：Gemini-2.5-Flash 建记忆；GPT-4o judge；作者报告。

- 解释边界：关键：六类题型的未加权宏平均；并非 500 题逐题 micro accuracy。

- 来源：[主要来源](https://mastra.ai/research/observational-memory)

## 5. Mem0 · 2026 temporal update

**阅读定位**：工程高分候选

- 机制：提取 / 更新事实，加入时间签名、时态和时间感知排序。

- 报告结果：作者 headline：LoCoMo 92.5%；LongMemEval 94.4%。

- 评测条件：2026 官方算法 / 时间推理报告；与 2025 原论文配置区分。

- 解释边界：后续同页还出现其他检索深度结果；此处保留 headline。该页未充分说明回答模型和 judge，不进入同口径排名。

- 来源：[主要来源](https://mem0.ai/blog/introducing-temporal-reasoning-in-mem0)

## 6. Zep · 2026 research page

**阅读定位**：工程高分候选

- 机制：时间失效管理 + 多范围图检索和重排，按预算组装上下文。

- 报告结果：作者页面：LoCoMo 94.7%；LongMemEval 90.2%。

- 评测条件：回答和 judge 均为 GPT-5.4；1,540 / 500 题；页面快照。

- 解释边界：页面 LoCoMo 总数与分项加总不一致，先当作待审计自报值；不能等同于开源 Graphiti 单独成绩。

- 来源：[主要来源](https://www.getzep.com/research/)

## 7. Agent Zero Memory

**阅读定位**：近期高分待复核

- 机制：事件时间线 + 实体图 + 分层文档记忆；检索保留来源证据。

- 报告结果：作者预印本：LongMemEval 95.60%；LoCoMo 93.60%。

- 评测条件：分别取最佳配置；LME 的 GPT-5.5 为 95.60%；500 / 1,540 题。

- 解释边界：主要与其他系统自报历史结果对比，不是统一骨干与 judge 的重跑；不足以确立统一 SOTA。

- 来源：[主要来源](https://arxiv.org/html/2608.29606v1)

## 8. A-MEM

**阅读定位**：结构化记忆基线

- 机制：Zettelkasten 式笔记、动态链接和记忆演化。

- 报告结果：Mem2ActBench：72B 下参数 F1=35.93，LTMemory=35.32。

- 评测条件：来自 Mem2ActBench 作者的同一 Qwen2.5-72B 设置，gold tool 已给定。

- 解释边界：动作参数场景的强对照；不是 35.93% 完整任务成功率。

- 来源：[主要来源](https://arxiv.org/abs/2502.12110) · [第三方评测来源](https://arxiv.org/html/2601.19935v1) · [System](https://github.com/agiresearch/A-mem)（Memory library for constructing agents. 链接核对：2026-10-28；未执行或审计代码。） · [Paper experiments](https://github.com/WujiangXu/A-mem)（Paper evaluation repository; the former AgenticMemory URL redirects here. 链接核对：2026-10-28；未执行或审计代码。）

## 9. MAGMA / Memory-R1

**阅读定位**：研究型消融候选

- 机制：MAGMA：语义、时间、因果、实体多图检索；Memory-R1：RL 学习增删改和证据选择。

- 报告结果：用于比较图结构与学习式管理两条路线；不强排跨论文总分。

- 评测条件：均有 LoCoMo / LongMemEval 相关实验。

- 解释边界：论文主张与部署配置分开；训练数据、模型、指标一致后再比较。

- 来源：[主要来源](https://arxiv.org/abs/2601.03236) · [第二来源](https://arxiv.org/abs/2508.19828)

## 10. AgentMemRec / FlexA-Mem

**阅读定位**：2026-10 新作观察

- 机制：前者把选记忆视为推荐排序；后者以不可变历史和预算自适应时间线恢复细节。

- 报告结果：AgentMemRec 报告 LME multi-session 子集增益；FlexA-Mem 强调紧预算及 AppWorld。

- 评测条件：分别发布于 10 月 26 日和 23 日；本次核对摘要及范围。

- 解释边界：最新预印本、不同任务 / 子集；列为跟进对象，不据此宣称 Personal 全局领先。

- 来源：[主要来源](https://arxiv.org/abs/2610.34673) · [第二来源](https://arxiv.org/abs/2610.33274)

## 11. PersonaMem-v3 agentic search configurations

**阅读定位**：跨平台个性化证据

- 机制：Agent 使用工具在多平台历史中搜索与组合证据。

- 报告结果：论文最佳配置 Claude Opus 4.8 + Claude Code High：53.7% overall。

- 评测条件：同文 GPT-5.5 Long Context 为 53.4%，Codex High 为 53.2%。

- 解释边界：这是模型 + harness 配置比较，不能把差距归因于单独 memory 模块；无单一访问模式全面占优。

- 来源：[主要来源](https://arxiv.org/html/2608.21381v1)

## 12. Supermemory

**阅读定位**：指标口径示例

- 机制：聚合式检索与记忆组织。

- 报告结果：官网标注 LongMemEval-S Recall@20 with aggregation = 97%。

- 评测条件：500 题；页面同时提及回答 judge，口径需结合完整评测代码确认。

- 解释边界：按页面明确标签记录为 Recall@20，不混入 QA accuracy 排名。

- 来源：[主要来源](https://supermemory.ai/research/)
