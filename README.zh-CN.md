<p align="center">
  <img src="assets/hero-logo.png" width="144" alt="Codex Native Dream Loop logo">
</p>

<h1 align="center">Codex Native Dream Loop</h1>

<p align="center">
  给 Codex 用的本地优先路线记忆层。
  <br>
  留住已经跑通的路径，拒绝薄弱经验，让下一次线程从证据开始。
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Codex-Native-1f6feb" alt="Codex Native">
  <img src="https://img.shields.io/badge/Plugin-Installable-7c3aed" alt="Installable plugin">
  <img src="https://img.shields.io/badge/Memory-ACTIVE%20%2B%20LEARNINGS-2563eb" alt="ACTIVE plus LEARNINGS">
  <img src="https://img.shields.io/badge/Runtime-Zero%20Server-0f766e" alt="Zero runtime server">
</p>

<p align="center">
  <a href="#安装">安装</a> ·
  <a href="#为什么需要它">为什么</a> ·
  <a href="#工作方式">工作方式</a> ·
  <a href="#命令">命令</a> ·
  <a href="README.md">English</a>
</p>

```bash
codex plugin marketplace add .
codex plugin add codex-native-dream-loop@codex-native-dream-loop
```

Dream Loop 面向高频 Codex 用户：你会跨线程、跨仓库、跨日期反复处理相似任务。它给 Codex 一套很小的运行记忆：`ACTIVE.md` 放当前应该生效的规则，`LEARNINGS.md` 放已经证明有效的复用路线，长期经验进入前必须经过晋升验证。

它不是通用记忆数据库，不是 agent 运行时，也不是模型训练框架。它解决的是一个更窄的问题：Codex 已经跑通过一次的路线，下一次不要再从零发现。

## 你会得到什么

| 表面 | 用途 |
| --- | --- |
| `ACTIVE.md` | 热规则和当前路线，影响下一次任务。 |
| `LEARNINGS.md` | 长期路线记忆，带证据、范围、拒绝条件和回滚线索。 |
| `inbox/` | 暂存薄弱信号或推断信号，避免直接污染长期记忆。 |
| `staged/` | 需要审阅的记忆改动提案。 |
| `reports/` | 汇总过期热层、拒绝路线、回放样例和覆盖情况。 |

公开模型刻意保持小。多数任务只需要读取 `ACTIVE.md` 和 `LEARNINGS.md` 的相关片段。

## 安装

### Codex Plugin

在本地仓库运行：

```bash
git clone https://github.com/JY0xLU/codex-native-dream-loop.git
cd codex-native-dream-loop

codex plugin marketplace add .
codex plugin add codex-native-dream-loop@codex-native-dream-loop
codex plugin list
```

预期状态：

```text
codex-native-dream-loop@codex-native-dream-loop  installed, enabled
```

仓库已经包含可被 marketplace 识别的 plugin 包：`plugins/codex-native-dream-loop/`，入口由 `.agents/plugins/marketplace.json` 提供。安装后建议新开一个 Codex 线程，让 skills 干净加载。

### 手动文件复制

当 plugin 支持不可用，或者你想先检查复制计划时，用这个方式：

```bash
python scripts/install.py --codex-home ~/.codex
python scripts/install.py --codex-home ~/.codex --apply
```

Windows PowerShell：

```powershell
python scripts/install.py --codex-home "$env:USERPROFILE\.codex"
python scripts/install.py --codex-home "$env:USERPROFILE\.codex" --apply
```

## 为什么需要它

长期使用 Codex 时，常见失败不是模型不会做，而是路线漂移：

- 相同的安装、调试、发布路线被反复从零发现
- 有用纠正埋在旧对话里
- 临时规则过期后仍然影响新任务
- plugin 和 skill 发现得太晚
- 记忆增长速度超过了人能审计的速度

Dream Loop 的目标是让下一次运行比上一次更便宜。它让已知有效路线保持可见，让薄弱经验先等待，并保留足够审计线索，方便撤回错误晋升。

## 工作方式

```text
召回 -> 选择路线 -> 执行 -> 捕捉信号 -> 整理巩固
```

1. 只读取 `ACTIVE.md` 和 `LEARNINGS.md` 的相关片段。
2. 已知路线明确适用时，优先复用。
3. 置信度不够时，再扩大搜索。
4. 明确强信号直接进入合适层级。
5. 推断信号或互相竞争的信号先留在 `inbox/`。
6. 长期记忆必须通过晋升验证。
7. 定期整理，归档过期路线，保持公开模型很小。

日常召回因此保持简单，后台维护仍然可审计。

## 晋升验证

一条长期经验进入 `LEARNINGS.md` 前，至少要回答五个问题：

| 关口 | 问题 |
| --- | --- |
| 证据 | 哪个任务、纠正或重复失败支持它？ |
| 影响 | 哪件事变得更快、更稳或更可靠？ |
| 范围 | 它适用于哪个仓库、流程、工具或任务类型？ |
| 停用条件 | 什么情况下 Codex 应该停止使用这条路线？ |
| 回滚线索 | 如果未来失效，维护过程应该移除或替换什么？ |

这就是路线记忆和泛泛建议的区别。好的条目应该足够具体，能被复用；也应该有边界，能被拒绝。

## 命令

```bash
# 仓库结构体检
python scripts/doctor.py

# 生成维护报告
python scripts/nightly_report.py --memory-root examples/minimal-global/.codex/memory

# 回放轻量样例
python scripts/nightly_report.py replay --fixtures-root examples/minimal-global/.codex/memory/fixtures

# 移除召回条目，同时保留 tombstone 审计
python scripts/memoryctl.py forget LRN-YYYYMMDD-001 --memory-root ~/.codex/memory --reason "no longer valid"
```

## Skills

| Skill | 职责 |
| --- | --- |
| `capture-memory` | 落地明确强信号，或隔离未解决的推断信号。 |
| `capability-evolution` | 按受控顺序发现并验证更好的工具。 |
| `dream-consolidate` | 审阅热记忆、暂存提案、报告、漂移、归档和下一步动作。 |

## 仓库结构

```text
.
|-- .agents/plugins/marketplace.json
|-- .codex-plugin/plugin.json
|-- plugins/codex-native-dream-loop/
|   |-- .codex-plugin/plugin.json
|   |-- assets/
|   `-- skills/
|-- skills/
|   |-- capture-memory/
|   |-- capability-evolution/
|   `-- dream-consolidate/
|-- scripts/
|   |-- doctor.py
|   |-- install.py
|   |-- memoryctl.py
|   `-- nightly_report.py
|-- references/
|-- templates/global/
|-- tests/
|-- README.md
`-- README.zh-CN.md
```

根目录的 `.codex-plugin/plugin.json` 是仓库校验用的源 manifest；`plugins/codex-native-dream-loop/` 下的副本是 marketplace 暴露给 Codex 的可安装包。

## 设计原则

- **公开模型要小**：日常召回只围绕 `ACTIVE.md` 和 `LEARNINGS.md`。
- **优先记录路线**：写可复用路径，不写泛泛总结。
- **证据先于长期化**：强信号可以落地，弱信号先等待。
- **本地优先**：不需要服务、数据库或看板。
- **维护可审计**：晋升、拒绝、归档、回滚都留下轨迹。

## 状态

Dream Loop 的核心闭环已经完成：plugin 安装、手动安装、仓库体检、维护报告、样例回放、遗忘和审计流程都已经在位。后续工作属于增强项：补更多回放覆盖、提升报告可读性，并补清 `ACTIVE.md`、`LEARNINGS.md`、`inbox/` 的判断示例。

## License

MIT. See [LICENSE](LICENSE).
