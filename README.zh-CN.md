<div align="center" id="readme-top">

<img src="assets/hero-logo.png" width="220" alt="Codex Native Dream Loop logo">

# Codex Native Dream Loop

**给 Codex 用的本地优先路线记忆层。**

双文件召回面、可审计晋升流程、可直接安装的 Codex plugin，让跨线程复用不再靠临场回忆。

<p align="center">
  <img src="https://img.shields.io/badge/Codex-Native-1f6feb?style=for-the-badge" alt="Codex Native">
  <img src="https://img.shields.io/badge/Public_Model-ACTIVE_%2B_LEARNINGS-2563eb?style=for-the-badge" alt="ACTIVE plus LEARNINGS">
  <img src="https://img.shields.io/badge/Local_First-Zero_Runtime_Server-0f766e?style=for-the-badge" alt="Local first">
  <img src="https://img.shields.io/badge/Plugin-Installable-7c3aed?style=for-the-badge" alt="Installable plugin">
  <img src="https://img.shields.io/badge/License-MIT-111827?style=for-the-badge" alt="MIT license">
</p>

[快速开始](#快速开始) · [插件安装](#插件安装) · [架构概览](#架构概览) · [English](README.md)

</div>

<br>

<details>
  <summary><kbd>目录</kbd></summary>

<br>

- [Codex Native Dream Loop 0.1](#codex-native-dream-loop-01)
- [项目定位](#项目定位)
- [为什么需要它](#为什么需要它)
- [设计取舍](#设计取舍)
- [快速开始](#快速开始)
- [插件安装](#插件安装)
- [手动文件复制安装](#手动文件复制安装)
- [架构概览](#架构概览)
- [记忆布局](#记忆布局)
- [核心 Skills](#核心-skills)
- [晋升验证](#晋升验证)
- [维护命令](#维护命令)
- [项目结构](#项目结构)
- [路线图](#路线图)

<br>

</details>

## Codex Native Dream Loop 0.1

> [!IMPORTANT]
>
> Dream Loop 面向高频 Codex 用户：你会跨线程、跨仓库、跨日期反复处理相似任务。
> 它把记忆控制在能读懂的规模，把长期经验的晋升控制在可审计的流程里，并且可以作为 Codex plugin 安装。
>
> 公开模型刻意保持很小：`ACTIVE.md` 是热层，`LEARNINGS.md` 是可复用路线库。
> 其他目录只服务于审阅、暂存、拒绝、回放、报告和回滚。

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 项目定位

Codex 往往能记住一段对话，却不一定保留真正跑通问题的路线。Dream Loop 给 Codex 一套有纪律的运行记忆：

<table>
<tr>
<td width="33%" valign="top">
<strong>ACTIVE.md</strong><br><br>
热层。短期指令、当前仓库路线、正在生效的纠正，以及任何应该立刻影响下一次任务的内容。
</td>
<td width="33%" valign="top">
<strong>LEARNINGS.md</strong><br><br>
路线库。长期复用路线必须有证据、适用范围、失败条件，以及为什么应该优先尝试。
</td>
<td width="33%" valign="top">
<strong>晋升验证</strong><br><br>
经验进入长期记忆前的控制点。检查来源证据、结果影响、影响范围、拒绝条件和回滚线索。
</td>
</tr>
<tr>
<td width="33%" valign="top">
<strong>暂存区</strong><br><br>
需要判断的提案可以先进入 <code>staged/</code>，记录接受的改动、拒绝的候选、审阅备注和目标层级。
</td>
<td width="33%" valign="top">
<strong>回放样例</strong><br><br>
用小型 YAML 样例保持闭环诚实，但不把仓库变成沉重的评测框架。
</td>
<td width="33%" valign="top">
<strong>维护报告</strong><br><br>
报告未解决的收件箱、暂存提案、拒绝路线、过期热层条目、样例结果和来源追踪覆盖情况。
</td>
</tr>
</table>

它不是通用记忆数据库，不是 agent 运行时，也不是模型训练框架。它是 Codex 路线记忆的轻量治理层。

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 为什么需要它

长期使用 Codex 时，最常见的问题不是模型不会做，而是路线漂移：

- 相同的安装、调试、发布路线被反复从零发现
- 有用纠正埋在很长的对话里
- 临时规则过期后还留在热层
- plugin 和 skill 发现得太晚
- 记忆增长速度超过了人能审计的速度

Dream Loop 把召回面控制得很小，同时让后台治理可审计。目标很直接：下一次运行应该从最佳已知路线开始，而不是再来一次空白推理。

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 设计取舍

<table>
<tr>
<th width="30%">取舍</th>
<th width="35%">Dream Loop</th>
<th width="35%">避免的问题</th>
</tr>
<tr>
<td><strong>公开记忆模型</strong></td>
<td>只有两个日常可读文件：<code>ACTIVE.md</code> 和 <code>LEARNINGS.md</code></td>
<td>日常召回散落在很多不透明层里</td>
</tr>
<tr>
<td><strong>长期经验</strong></td>
<td>必须带证据、范围、拒绝条件和回滚线索才能晋升</td>
<td>泛泛建议悄悄改变不相关的未来行为</td>
</tr>
<tr>
<td><strong>弱信号处理</strong></td>
<td>未解决或推断信号短期留在 <code>inbox/</code></td>
<td>每个观察都变成长期记忆</td>
</tr>
<tr>
<td><strong>自动维护</strong></td>
<td>单一维护过程同时处理记忆、仓库审计、漂移检查和下一步建议</td>
<td>越来越多互相重叠的定时 agent</td>
</tr>
<tr>
<td><strong>工具形态</strong></td>
<td>安装、体检、报告、回放、遗忘都是零依赖脚本</td>
<td>强制用户先部署服务、数据库、看板或云端组件</td>
</tr>
<tr>
<td><strong>插件路径</strong></td>
<td>仓库自带 Codex plugin 包和本地 marketplace 文件</td>
<td>用户必须先手动复制 skill 目录才能试用</td>
</tr>
</table>

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 快速开始

安装 plugin，验证仓库，再生成一份本地维护报告。

### 0. 前置条件

- 支持 plugin 的 Codex CLI
- Python 3.10+
- 本仓库的本地副本

### 1. 作为 Codex plugin 安装

在仓库根目录运行：

```bash
codex plugin marketplace add .
codex plugin add codex-native-dream-loop@codex-native-dream-loop
codex plugin list
```

你应该能看到 `codex-native-dream-loop` 处于已安装、已启用状态。安装后建议新开一个 Codex 线程，让 plugin skills 干净加载。

### 2. 验证仓库

```bash
python scripts/doctor.py
```

预期输出：

```text
Dream Loop doctor: OK
Severity: must checks passed
```

### 3. 生成报告

```bash
python scripts/nightly_report.py --memory-root examples/minimal-global/.codex/memory
```

### 4. 运行回放

```bash
python scripts/nightly_report.py replay --fixtures-root examples/minimal-global/.codex/memory/fixtures
```

预期输出：

```text
Replay fixtures: 5/5
```

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 插件安装

仓库包含可被 marketplace 识别的 plugin 包：

- `.agents/plugins/marketplace.json` - 仓库本地 marketplace 入口
- `plugins/codex-native-dream-loop/.codex-plugin/plugin.json` - 可安装的 plugin manifest
- `plugins/codex-native-dream-loop/skills/` - 随 plugin 分发的 Dream Loop skills
- `plugins/codex-native-dream-loop/assets/` - plugin logo 和 composer icon

克隆并安装：

```bash
git clone https://github.com/JY0xLU/codex-native-dream-loop.git
cd codex-native-dream-loop
codex plugin marketplace add .
codex plugin add codex-native-dream-loop@codex-native-dream-loop
```

确认安装：

```bash
codex plugin list
```

拉取新版本后的更新方式：

```bash
git pull
codex plugin remove codex-native-dream-loop
codex plugin add codex-native-dream-loop@codex-native-dream-loop
```

根目录的 `.codex-plugin/plugin.json` 保留为仓库校验使用的源 manifest；`plugins/codex-native-dream-loop/` 下的副本是 marketplace 暴露给 Codex 的可安装包。

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 手动文件复制安装

当 Codex plugin 不可用，或者你想先检查每个复制动作时，用手动安装。

先看 dry-run：

```bash
python scripts/install.py --codex-home ~/.codex
```

Windows PowerShell：

```powershell
python scripts/install.py --codex-home "$env:USERPROFILE\.codex"
```

确认后执行复制：

```bash
python scripts/install.py --codex-home ~/.codex --apply
```

手动安装会复制：

- `skills/capture-memory/`
- `skills/capability-evolution/`
- `skills/dream-consolidate/`
- `templates/global/`
- 全局 `AGENTS.md` 起步片段

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 架构概览

```text
Codex 任务线程
  召回 -> 选择路线 -> 执行 -> 捕捉信号
        |
        v
公开路线记忆
  ACTIVE.md + LEARNINGS.md
        |
        v
治理产物
  inbox / staged / rejected / archive / audit
        |
        v
维护工具
  doctor / report / replay / forget / install
```

即使后台治理产物变多，公开模型仍然很小。普通任务只需要读取 `ACTIVE.md` 和 `LEARNINGS.md` 的相关片段；维护命令再检查支撑目录。

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 记忆布局

```text
.codex/memory/
|-- ACTIVE.md                 # 当前热行为和路线
|-- LEARNINGS.md              # 长期可复用路线记忆
|-- AUDIT_LOG.md              # 晋升、拒绝、归档、回滚轨迹
|-- inbox/                    # 未解决的推断信号
|-- staged/                   # 等待判断的提案
|-- rejected/                 # 被拒绝的候选和理由
|-- fixtures/                 # 轻量回放预期
|-- reports/                  # 维护报告
`-- ARCHIVE/                  # 退役或被替代的材料
```

只有 `ACTIVE.md` 和 `LEARNINGS.md` 是日常召回面。其他目录用于审阅、追踪和维护。

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 核心 Skills

<table>
<tr>
<th width="28%">Skill</th>
<th width="36%">职责</th>
<th width="36%">使用时机</th>
</tr>
<tr>
<td><code>capture-memory</code></td>
<td>落地明确强信号，或隔离未解决的推断信号。</td>
<td>出现用户纠正、重复失败、已证明路线或长期偏好之后。</td>
</tr>
<tr>
<td><code>capability-evolution</code></td>
<td>按受控顺序发现并验证更好的能力。</td>
<td>本地路线不足，且 plugin、skill 或可信外部项目可能提升任务质量时。</td>
</tr>
<tr>
<td><code>dream-consolidate</code></td>
<td>审阅热记忆、暂存提案、归档、报告、漂移和下一步动作。</td>
<td>需要定时或手动执行 Dream Loop 维护时。</td>
</tr>
</table>

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 晋升验证

一条长期经验进入 `LEARNINGS.md` 前，应该回答五个问题：

| 关口 | 问题 |
| --- | --- |
| 来源证据 | 这个信号来自哪里？ |
| 结果影响 | 哪件事变得更快、更稳或更可靠？ |
| 适用范围 | 它适用于哪个工作区、仓库、工具或任务类型？ |
| 拒绝条件 | 什么情况下 Codex 应该停止使用这条路线？ |
| 回滚线索 | 如果未来失效，维护过程应该移除或替换什么？ |

长期条目的示例形态：

```md
- README 和 GitHub 展示页要保持视觉明确、可直接安装 plugin，并写清验证证据。
  scope: public repo presentation
  evidence: repeated README polish requests and plugin install validation
  reject_when: repository is no longer distributed through Codex plugins
```

弱信号、推断信号或互相竞争的信号，应该先留在 `inbox/`，直到有足够证据晋升或拒绝。

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 维护命令

| 命令 | 用途 |
| --- | --- |
| `python scripts/doctor.py` | 检查仓库健康、文档、plugin 元数据、回放样例和 UTF-8 安全。 |
| `python scripts/nightly_report.py --memory-root <path>` | 为一个 Dream Loop 记忆根目录生成维护报告。 |
| `python scripts/nightly_report.py replay --fixtures-root <path>` | 回放样例预期，发现报告逻辑漂移。 |
| `python scripts/memoryctl.py forget --memory-root <path> --target <id>` | 把过期或被拒绝的记忆移出热路径。 |
| `python scripts/install.py --codex-home <path> --apply` | 当 plugin 安装不可用时，把 skills 和模板复制进 Codex home。 |

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 项目结构

```text
.
|-- .agents/plugins/marketplace.json
|-- .codex-plugin/plugin.json
|-- assets/
|   |-- 32x32.png
|   `-- hero-logo.png
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

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## 路线图

- **安装路径** - 持续烟测仓库本地 marketplace 和打包后的 plugin。
- **报告质量** - 让维护输出更容易扫描，同时不扩大公开记忆模型。
- **回放覆盖** - 为晋升、拒绝、归档、过期热层和回滚增加样例。
- **操作体验** - 把 Windows、PowerShell 和 Codex Desktop 工作流作为一等路径。
- **治理清晰度** - 补充什么时候写入 `ACTIVE.md`、`LEARNINGS.md`、`inbox/` 的示例。

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## License

MIT. See [LICENSE](LICENSE).
