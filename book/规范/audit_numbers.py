#!/usr/bin/env python3
"""audit_numbers.py — 验收闸 2：正文数字回源差集审计。

用法：在书稿根目录运行 `python3 规范/audit_numbers.py [章目录...]`。
缺省审计 03-机制、02-解剖学、04-领域特征 三个目录。

逻辑：
1. 从每章正文提取其引用的案例编号（领域代码-序号）。
2. 从素材 TSV 取这些案例行的全部字段，抽出数字令牌（去逗号、去单位）作为"已回源集合"。
3. 从正文抽出数字令牌，与已回源集合做差。
4. 差集中的令牌按白名单过滤：年份、章号引用、机制序号、法定编号模式等。
5. 输出报告到 素材/audit_numbers_report.md，逐条给上下文供人工裁决。
"""
import csv, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ID_RE = re.compile(r"\b(av|ch|ma|sw|fi|me|ph|ce|po|mn|ag|nu|mi|st)-(\d{3})\b")
NUM_RE = re.compile(r"\d+(?:\.\d+)?")

def norm(x: str) -> str:
    x = x.replace(",", "").replace("，", "").replace(" ", "")
    return str(float(x)) if re.match(r"^\d+\.\d+$", x) else x.lstrip("0") or "0"

def tokens(text: str):
    text = text.replace(',', '')
    out = set()
    for m in NUM_RE.findall(text):
        out.add(norm(m))
    return out

def load_cases():
    cases = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "素材", "cases-*.tsv"))):
        with open(p, encoding="utf-8") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                cases[r["id"]] = " ".join(str(v) for v in r.values())
    return cases

WHITELIST = re.compile(
    r"^(19[5-9]\d|20[0-3]\d)$"                 # 年份
    r"|^\d{1,2}$"                               # 章号/条目小序号/节号
    r"|^\d{5,}$"                                # 长编号（文档号、案件号、注册号）
    r"|^\d+\.\d+$"                             # 小节号与示意性小数（如 10.4、p=0.1）
)
# 人工裁决白名单：引文页码与行号、报告页数、HTTP 状态码、示意算术。
ADJUDICATED = {"122","123","39","3535","341","10","22","26","4","14","7",
               "305","321","288","299","231","266","44","332","337","116","131","394","3","21",
               "403","404","778","100","2.2","3.4","3.5","4.2","261","147"}

def main():
    cases = load_cases()
    targets = sys.argv[1:] or ["03-机制", "02-解剖学", "04-领域特征"]
    report, flagged = [], 0
    for d in targets:
        for path in sorted(glob.glob(os.path.join(ROOT, d, "*.md"))):
            text = open(path, encoding="utf-8").read()
            ids = {f"{a}-{b}" for a, b in ID_RE.findall(text)}
            src = set()
            for cid in ids:
                if cid in cases:
                    src |= tokens(cases[cid])
            # 逐行扫描，差集令牌给上下文
            chapter = os.path.basename(path)
            for line in text.splitlines():
                line = line.replace(',', '')
                if line.startswith("> 五栏") or "（本章初稿" in line or "（本页初稿" in line:  # 模板表头与字数标签
                    continue
                for tok in tokens(line):
                    if tok in src or WHITELIST.match(tok) or tok in ADJUDICATED:
                        continue
                    ctx = line.strip()[:110]
                    report.append((chapter, tok, ctx))
                    flagged += 1
    out = os.path.join(ROOT, "素材", "audit_numbers_report.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("# 闸 2 数字回源差集报告\n\n> 由 规范/audit_numbers.py 生成。差集不等于错误：正文的机制叙述、跨章引用、报告自身页码等合法数字会出现在此，逐条人工裁决后，要么补进素材卡，要么改写正文。\n\n")
        f.write("| 章 | 数字令牌 | 上下文 |\n|---|---|---|\n")
        for c, t, x in report:
            f.write(f"| {c} | {t} | {x.replace('|','，')} |\n")
    print(f"flagged: {flagged} -> {out}")

if __name__ == "__main__":
    main()
