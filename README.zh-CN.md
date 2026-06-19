<p align="center">
  <img src="assets/hero-logo.png" width="156" alt="CoDream Loop logo">
</p>

<h1 align="center">CoDream Loop</h1>

<p align="center">
  给 Codex 用的路线记忆：留下已经赢过的路径，拒绝薄弱经验，保持召回很小。
</p>

<p align="center">
  <a href="https://github.com/JY0xLU/codream-loop/stargazers"><img src="https://img.shields.io/github/stars/JY0xLU/codream-loop?style=flat&logo=github&label=Stars" alt="GitHub stars"></a>
  <a href="https://github.com/JY0xLU/codream-loop/forks"><img src="https://img.shields.io/github/forks/JY0xLU/codream-loop?style=flat&logo=github&label=Forks" alt="GitHub forks"></a>
  <img src="https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/deps-zero-0f766e" alt="Zero runtime dependencies">
  <img src="https://img.shields.io/badge/privacy-local--only-14b8a6" alt="Local-only privacy">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2563eb" alt="MIT license"></a>
  <img src="https://img.shields.io/github/last-commit/JY0xLU/codream-loop?label=last%20commit" alt="Last commit">
</p>

<p align="center">
  <a href="#安装">安装</a> ·
  <a href="#为什么需要它">为什么</a> ·
  <a href="#公开模型">公开模型</a> ·
  <a href="#闭环怎么工作">闭环</a> ·
  <a href="#命令">命令</a> ·
  <a href="README.md">English</a>
</p>

```bash
git clone https://github.com/JY0xLU/codream-loop.git
cd codream-loop

codex plugin marketplace add .
codex plugin add codream-loop@codream-loop
```

Codex 经常会忘记哪条路线已经跑通。Dream Loop 给它一套很小的运行记忆：`ACTIVE.md` 放当前热规则，`LEARNINGS.md` 放可复用路线，任何长期记忆都先过验证门。

它适合高频 Codex 用户：跨线程、跨 repo、跨日期反复做相似工作。它不是通用记忆平台，不是 agent 运行时，也不是训练框架。目标是让 Codex 下一次直接从赢过的路线开始，而不是让记忆越来越难审计。

## 亮点

- **公开模型很小**：日常召回只看 `ACTIVE.md` 和 `LEARNINGS.md`。
- **复用路线**：强经验沉淀成可执行路径，而不是泛泛心得。
- **验证门**：长期记忆需要来源证据、拒绝条件和回滚线索。
- **插件优先安装**：仓库自带 Codex marketplace 入口和可安装 plugin 包。
- **本地优先**：安装、doctor、report、fixture replay、forget 都是零依赖脚本。

## 环境要求

- 推荐路径需要支持 plugin 的 Codex CLI
- 本地脚本需要 Python 3.10+
- 使用本地文件系统中的 Codex home
- 不需要服务、数据库、看板或云同步

## 快速开始

```bash
git clone https://github.com/JY0xLU/codream-loop.git
cd codream-loop

codex plugin marketplace add .
codex plugin add codream-loop@codream-loop
python scripts/doctor.py
python scripts/nightly_report.py --memory-root examples/minimal-global/.codex/memory
```

安装后建议新开一个 Codex 线程，让 Dream Loop skills 干净加载。最直接的收益是：Codex 选择路线前，会先读取 `ACTIVE.md` 和 `LEARNINGS.md` 的最小相关片段。

## 安装

### Codex Plugin

在本地仓库运行：

```bash
git clone https://github.com/JY0xLU/codream-loop.git
cd codream-loop

codex plugin marketplace add .
codex plugin add codream-loop@codream-loop
codex plugin list
```

预期状态：

```text
codream-loop@codream-loop  installed, enabled
```

仓库已经包含可被 marketplace 识别的 plugin 包：`plugins/codream-loop/`，入口由 `.agents/plugins/marketplace.json` 提供。安装后建议新开一个 Codex 线程，让 skills 干净加载。

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

手动安装会复制三个 Dream Loop skills、全局起步模板和 `AGENTS.md` 片段。plugin 不可用时保留这条路径作为回退。

## 使用场景

- **重复仓库工作**：安装、测试、发布、PR 路线不用每次重新发现。
- **README 和发布卫生**：保留已经证明有效的发布偏好，不让它们埋在旧线程里。
- **长期 agent 偏好**：把重复出现的明确纠正变成有范围、有证据的行为。

## 不适合做什么

Dream Loop 刻意保持窄边界。它不是：

- 通用向量记忆或图记忆产品
- 自主 agent 运行时
- benchmark 优化器或模型训练循环
- 云端记忆同步层

## 为什么需要它

很多 agent 不是不会做事，而是路线会漂移：

- 有效路径被反复从零发现
- 旧经验散在长对话里
- 临时规则留得太久
- plugin 和 skill 找得太晚
- 记忆层越加越多，却没有更清楚

Dream Loop 的目标是让下一次行动比上一次更省、更快、更稳。

它只把两个文件放到日常心智模型里：

- `ACTIVE.md`
  - 现在就应该影响行为的热规则
- `LEARNINGS.md`
  - 已验证、可跨任务复用的路线记忆

其他内容都留在后台，用于审阅、追踪和回滚。

## 公开模型

Dream Loop 对日常使用只暴露两层。

### `ACTIVE.md`

`ACTIVE.md` 是热层。

适合放：

- 临时但重要的规则
- 当前热路线
- 阶段性、应该立刻影响下一次任务的行为
- 必须改变下一次运行的明确纠正

如果一条内容不再影响近期决策，就不应该继续留在这里。

### `LEARNINGS.md`

`LEARNINGS.md` 是路线记忆层。

它应该像一套路由表，而不是心得堆。使用时先从索引进入相关章节，再读取当前任务真正需要的条目。

好的 entry 至少回答：

- 适合哪类任务
- 应该先走哪条路
- 为什么这条路赢
- 最近何时验证过
- 有什么证据
- 什么情况下应该回退或避免

这样系统更像路线复用，而不是单纯存储记忆。

```text
日常召回：
  ACTIVE.md       -> 当前指令和热路线
  LEARNINGS.md    -> 已验证的复用路线

审阅支撑：
  inbox/          -> 未解决或推断信号
  staged/         -> 等待判断的记忆改动
  rejected/       -> 不应该落地的候选
  AUDIT_LOG.md    -> 晋升、拒绝、归档、回滚轨迹
```

## 闭环怎么工作

工作循环是：

```text
recall -> choose -> search if needed -> execute -> land or quarantine -> consolidate
```

落到实际步骤：

1. 先从 `ACTIVE.md` 和 `LEARNINGS.md` 里只取最小相关片段。
2. 如果已有路线明显适用，就先复用。
3. 如果把握还不够高，再让 `capability-evolution` 按顺序搜索：已启用官方插件 -> 可安装官方插件 -> 本地 skills -> 可信 GitHub 项目。
4. 让搜索过程可观察：记录查过哪些层、哪些层被跳过或阻塞、哪个候选获胜、哪些候选失败，以及是否真的触达外部搜索。
5. 当前任务只选一条获胜路线执行，不把多条竞争路线同时固化。
6. 用 `capture-memory` 直接把明确强信号落到 `ACTIVE.md` 或 `LEARNINGS.md`。
7. 只有推断型、未验证或互相竞争的信号才进 `inbox/`。
8. 用 `dream-consolidate` 在维护时刷新热层、强化路线记忆、清空未决信号，并把淘汰路线归档。

公开模型保持小，后台机制仍然可审计。

## 最小工作流示例

1. 用户纠正 Codex：“这个仓库发布前先跑 `python scripts/doctor.py`。”
2. `capture-memory` 把它识别为明确强信号，落成一条短的 `ACTIVE.md` 规则。
3. 下一次相关任务开始前，Codex 先读取这条热规则，再选择路线。
4. 如果这条路线在多轮发布里都证明有效，`dream-consolidate` 会带着证据和拒绝条件生成 `LEARNINGS.md` 候选。
5. 如果路线未来过期，`memoryctl.py forget` 或维护 pass 会把它移出默认召回，并留下审计痕迹。

弱推断信号走另一条路：先进入 `inbox/`，不能直接变成长期记忆。

## 验证门

Dream Loop 会验证长期记忆改动，但不把自己变成重型优化框架。

在一条路线、偏好或流程进入长期记忆之前，维护 pass 至少要回答：

- 它来自哪一次真实任务、明确纠正、repo 审计或重复失败
- 它是否真的能让上一次结果变好
- 它应该成为 `LEARNINGS.md` 的长期路线，还是只该暂时放进 `ACTIVE.md`
- 什么证据会让它被拒绝、退回隔离或归档
- 如果以后证明它错了，怎么回滚

对于判断较重的改动，`dream-consolidate` 应先生成 staged proposal：接受哪些编辑、拒绝哪些候选、证据是什么、reviewer 或 subagent 怎么看、目标层是哪一个。staging 只是审计产物，不是第三个公开记忆层。日常心智模型仍然只有 `ACTIVE.md` 和 `LEARNINGS.md`。

这让 Dream Loop 成为 Codex-native 的记忆维护闭环：轻到能读，严到能挡住自我强化的坏经验。

## 不臃肿的质量控制

Dream Loop 的改进重点不是增加更多公开层，而是让路线选择更准。

- 能复用已知路线就先复用。
- 把握不足时才扩大搜索。
- 验证证据保持短小。
- 凡是需要大框架才能证明的小记忆改动，都应该被拒绝或暂缓。
- 失败或淘汰路线要归档，不要静默消失。

系统应该变快，但不应该变得更难理解。

## 核心 Skills

这套系统主要由三个 skill 组成：

| Skill | 何时触发 | 改变什么 | 拒绝什么 |
| --- | --- |
| `capture-memory` | 出现纠正、已验证路线或稳定偏好时。 | 落明确强信号，或隔离弱信号。 | 把每个观察都变成长期记忆。 |
| `capability-evolution` | 已知路线不够用时。 | 按顺序检查官方插件、本地 skills、可信外部选项，并保留证据。 | 没展示查过/跳过哪些层就声称完成 discovery。 |
| `dream-consolidate` | 需要维护 pass 时。 | 刷新热记忆、审阅提案、归档过期路线、报告漂移。 | 没有人类要求时静默修改 repo tracked files。 |

它们共同服务一个目标：

**先复用已经赢过的路线，不够时再扩大搜索。**

## 自动化

这套系统默认只需要一个 recurring automation，而不是越拆越多的定时 agent。

这个 automation 每次运行要同时完成六件事：

- 维护 Dream Loop 双层 memory
- 审计当前 repo 或 PR 轮次
- 检查已安装 custom skills 是否仍然匹配 automation prompt
- 报告真实 reviewer 或 subagent 证据，或说明为什么走低风险单代理快路
- 检查 automation 自己的 prompt 有没有落后
- 给出下一轮最小可执行改进建议

它在 repo 层只做审计和建议，不静默修改跟踪文件。

## 后台机制

系统仍然保留一些后台机制，但它们不应该成为主要心智模型。

| 区域 | 用途 |
| --- | --- |
| `inbox/` | 只用于推断型、未验证、仍有冲突的短期隔离信号。 |
| `staged/` | 等待判断的记忆改动提案。 |
| `rejected/` | 被拒绝的候选和理由。 |
| `AUDIT_LOG.md` | 最小化的晋升、拒绝、归档、回滚痕迹。 |
| `ARCHIVE/` | 退役或被替代的内容，用于保留可追溯性。 |

这些机制服务于回滚和审阅，不是日常必须理解的额外公开层。

## 命令

```bash
# 仓库结构体检
python scripts/doctor.py

# 生成维护报告
python scripts/nightly_report.py --memory-root examples/minimal-global/.codex/memory

# 生成静态 HTML 报告
python scripts/nightly_report.py --memory-root examples/minimal-global/.codex/memory --format html --output report.html

# 回放轻量样例
python scripts/nightly_report.py replay --fixtures-root examples/minimal-global/.codex/memory/fixtures

# 移除召回条目，同时保留 tombstone 审计
python scripts/memoryctl.py forget LRN-YYYYMMDD-001 --memory-root ~/.codex/memory --reason "no longer valid"
```

## 仓库结构

```text
.
|-- .agents/plugins/marketplace.json
|-- .codex-plugin/plugin.json
|-- plugins/codream-loop/
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

根目录的 `.codex-plugin/plugin.json` 是仓库校验用的源 manifest；`plugins/codream-loop/` 下的副本是 marketplace 暴露给 Codex 的可安装包。

## 文档地图

- [CHANGELOG.md](CHANGELOG.md) - 版本记录和重要变更
- [references/](references/) - scope、验证、自动化、能力演进等设计说明
- [templates/global/](templates/global/) - 起步记忆结构和 AGENTS 片段
- [plugins/codream-loop/](plugins/codream-loop/) - 可被 marketplace 安装的 plugin 包

## 贡献

改动应继续遵守小公开模型：

- 不要轻易增加新的公开记忆层
- 示例要具体，并带来源或验证依据
- 发布前运行 `python scripts/doctor.py` 和 fixture replay
- plugin 安装说明和手动 fallback 要保持同步

## 什么叫效果变好了

这套系统真正跑顺之后，会有这些变化：

- 新任务不再频繁从零开始
- `ACTIVE.md` 会一直很短，而且一眼能看出现在哪些规则重要
- `LEARNINGS.md` 更像路线库，不像心得堆
- 明确纠正和稳定偏好会很快落层，而不是在 `inbox/` 里拖着
- plugin 和 skill 会在需要时被主动找出来
- 失败或淘汰路线会被归档，而不是静默消失
- 系统更快了，但没有变得更乱

## 状态

Dream Loop 的核心闭环已经完成：plugin 安装、手动安装、仓库体检、维护报告、样例回放、遗忘和审计流程都已经在位。后续工作属于增强项：补更多回放覆盖、提升报告可读性，并补清 `ACTIVE.md`、`LEARNINGS.md`、`inbox/` 的判断示例。

## License

MIT. See [LICENSE](LICENSE).
