# 《Failure》English Edition — Writer's Brief (v1.0)

## What this is

An English edition of a Chinese practitioner's handbook on structural failure. The Chinese
edition is finished and is the **source of facts**. The English edition is not a translation:
it is the same book written again for an English reader.

Rule of thumb: if a sentence could be pasted back into Chinese word-for-word, it is too close.
Rewrite for the English ear, keep every fact, number, date, page citation and case ID.

## Hard rules

1. **Facts are not negotiable.** Every number, date, time, page reference, report number and
   case ID in the Chinese text appears in the English text, unchanged. If the Chinese says
   "p.153–154", the English says "pp. 153–154". If a figure was marked "报告未载", write
   "not stated in the report".
2. **Do not add facts.** No invented colour, no reconstructed dialogue, no "likely felt".
   No outside knowledge, however well known.
3. **Case IDs stay as-is**: `mi-001`, `av-007`, `ch-006`, `po-004`. Do not renumber, do not
   translate, do not expand to names.
4. **The stop point stays a stop point.** The 停点 block must not reveal the outcome. Keep the
   three questions in this fixed English form:

   > **Stop here. Decide before you turn the page.**
   >
   > 1. What would you do? Write the action, not "pay more attention".
   > 2. Which item here are you most likely to miss, and why does it look unimportant?
   > 3. If you may set one checkpoint, when is it and what does it check?

5. **Section order and headings mirror the Chinese.** Same chapter numbering, same section
   sequence, same 12 card fields:

   | Chinese | English |
   |---|---|
   | 编号 | Case ID |
   | 时间与地点 | When and where |
   | 主体 | What and who |
   | 事发前在做什么 | What they were doing |
   | 决策点 | The decision point |
   | 当时可见 | What was visible then |
   | 〔停点〕 | Stop point (see above) |
   | 结局 | What happened |
   | 被排除的选项 | Options ruled out |
   | 早期信号 | Early signals |
   | 加码点 | The point of escalation |
   | 失效链 | Failure chain |
   | 最小反事实 | Minimum counterfactual |
   | 结局与来源 | Outcome and sources |

6. **No AI tells.** Banned: "it is not X, but Y" more than once per chapter; paragraph-opening
   "First/Second/Finally"; em-dashes; "experts say"; exclamation marks; "delve", "crucial",
   "landscape", "tapestry", "unlock", "navigate the complexities"; closing each paragraph with
   a moral.
7. **Tone.** A working manual, not an essay. Short declaratives. The reader is a practitioner
   deciding what to check on Monday. Never scold, never inspire.

## Fixed terminology

Mechanism chapter titles (use exactly):

1. 偏差的正常化 — **Normalization of Deviance** (Vaughan, 1996)
2. 指标替代目标 — **Goal Displacement; Goodhart's Law**
3. 叙事先于证据 — **Narrative before Evidence**
4. 专家直觉的失效区 — **Where Intuitive Expertise Breaks Down**
5. 程序漂移 — **Practical Drift** (Snook)
6. 信息在层级中衰减 — **Information Attenuation up the Hierarchy**
7. 激励错位 — **Misaligned Incentives**
8. 责任稀释 — **Diffusion of Responsibility**
9. 说真话的人先被淘汰 — **Why the Truth-Teller Goes First**
10. 成功的松弛 — **The Slack of Success** (Sitkin)
11. 隐蔽耦合 — **Hidden Coupling** (Perrow)
12. 冗余的假象 — **The Illusion of Redundancy**
13. 边界条件外推 — **Extrapolating Past the Validated Domain**
14. 规模跨越阈值 — **Crossing a Scale Threshold**
15. 安全边际被吃掉 — **Margin Erosion** (Dekker)
16. 自动化与技能退化 — **Automation and Skill Decay**
17. 沉没成本与加码 — **Sunk Cost and Escalation** (Staw)
18. 期限错配 — **Horizon Mismatch**
19. 维护的不可见 — **The Invisibility of Maintenance**
20. 交接断层 — **Handover Rupture**
21. 监管滞后与俘获 — **Regulatory Lag and Capture** (Stigler)
22. 合规但不安全 — **Compliant and Unsafe**
23. 连带失效 — **Cascading Failure**
24. 路径锁定 — **Path Lock-in**

Other fixed renderings:

- 机制章 / 领域页 — *mechanism chapter* / *domain page*
- 案例卡 — *case card*; 压缩版 — *condensed*; 展开版 — *full card*
- 停点 — *stop point*
- 失效链 — *failure chain*; 三层 — *technical / informational / organizational layers*
- 最小反事实 — *minimum counterfactual*
- 加码点 — *escalation point*
- 装置一/二/三/四 — *Device 1–4* (the book's recurring instruments)
- 三态制 — *three-state register*
- 档案学 — *the archival view*
- 台阶（七级） — *the seven-step ladder*
- 读者契约 — *the reader's contract*
- 自检五问 — *five self-checks*
- 领域 — *domain*; 航空 aviation, 化工与流程工业 chemical & process, 核电与能源 nuclear & energy,
  医疗 healthcare, 药品与器械 drugs & devices, 建筑与基础设施 construction & infrastructure,
  海事与运输 maritime & transport, 软件与互联网服务 software & internet services, 金融 finance,
  创业与产品 startups & products, 公共政策与行政 public policy & administration, 军事 military,
  制造业与供应链 manufacturing & supply chain, 农业与食品 agriculture & food

## Output

Write to `/home/ubuntu/failure-book/build/en/<same-number>-<slug>.md`, UTF-8, one file per
Chinese file. Heading levels identical to the Chinese file. No YAML front matter. No
translation notes, no "translator's preface", no bracketed glosses of Chinese terms.

Report back: word count per file, and a list of anything in the Chinese you could not render
without adding a fact.
