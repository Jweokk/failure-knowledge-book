# 失败的知识

**跨领域失效结构手册**

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![中文 + English](https://img.shields.io/badge/language-%E4%B8%AD%E6%96%87%20%2B%20English-7c6cff.svg)](#)
[![Edition](https://img.shields.io/badge/edition-v1.0-f59e0b.svg)](CHANGELOG.md)

[English](./README.md) · [在线阅读](https://tkf.fly2ai.top/) · [English edition](https://tkf.fly2ai.top/en/)

24 个机制 · 14 个领域 · 159 个案例 · 53 张完整案例卡 · 55.4 万汉字 · 中英双语

---

## 这是一本什么书

多数写失败的书收集故事，然后给出教训。这本把失败当作一类知识来处理：它由有限的一组机制构成，这些机制在不同领域反复出现，每一个都有它怎么长出来的过程、最早在什么时候能被看出来、以及在什么条件下不成立。

每个机制章取四到六个不同领域的案例——航空、化工、建筑、软件、医疗、核电、铁路、海运、采矿、金融、公共工程、产品、食品、能源。重点不是案例彼此相似，而是同样的结构参数反复出现：耦合度、冗余程度、激励在奖励什么、剩余时间、监管强度、规模量级。

案例卡只写当事人当时能看到的信息。结局段的内容不进左栏，不推测内心动机，每一个加码点都落到具体的日期、会议或签字人。每张卡停在决策点，读者先判断，翻页才是结局。

## 里面有什么

| 部 | 章 | 主线 |
|---|---|---|
| 元问题 | 1–4 | 失败的知识为什么最贵、记录会怎样失真、五个认真记录失败的领域、这套方法为什么没有扩散出去 |
| 解剖学 | 5–10 | 一次失效的解剖、当时可见、案例的形状、证据等级、怎么读一张卡 |
| 机制 | 11–34 | 二十四个机制，从偏差的正常化到跨越规模阈值 |
| 领域 | 1–14 | 航空、化工、建筑、软件、医疗、核电、铁路、海运、采矿、金融、公共工程、产品、食品与农业、能源 |
| 用法 | 35–39 | 查、用、练、共，以及九十分钟预演会 |
| 边界 | 40–42 | 这套方法做不到什么、仍在争议中的案例、机制清单的边界 |
| 附录 | A–D | 机制 × 领域矩阵、案例总表、证据等级与重建方法、机制家系 |

每个机制章的末尾是自检五问，不是总结。附录 A 是 24 × 14 的矩阵，138 格；附录 B 把 159 个案例按编号、领域、所在章列全。

## 构建

需要 Python 3.11+、`mkdocs-material`（站点）、`weasyprint`（PDF）、Noto Serif SC 与 Noto Serif 字体。

```bash
python3 book/_spec/build_pdf.py          # 中文 PDF -> dist/失败的知识.pdf
python3 book/_spec/build_pdf_en.py       # 英文 PDF -> dist/failure-knowledge.pdf
python3 site/build_site.py               # 汇集页面 + 生成 mkdocs.yml
mkdocs build -f site/mkdocs.yml          # 中文站 -> site/build
python3 site/build_site_en.py
mkdocs build -f site/mkdocs-en.yml       # 英文站 -> site/build-en
rm -rf site/build/en && cp -r site/build-en site/build/en
```

## 目录结构

```
book/            中文稿（Markdown，一章一个文件）
book/en/         英文稿，独立成文，不是翻译
book/_spec/      PDF 流水线：build_pdf.py、build_pdf_en.py、CSS
site/            站点汇集、导航、主题覆盖、计数脚本
dist/            构建产物（PDF，不入库）
```

## 勘误与方法

`book/勘误.md` 记录审校中改正的每一处，附核对所依据的原始文书。`book/交付说明.md` 记录从初稿到定稿改了什么、为什么。方法本身见附录 C；书里的数字都能追到可以打开的出处。

## 许可

正文与图表：CC BY-NC-SA 4.0；脚本：MIT。见 [LICENSE](./LICENSE)。
