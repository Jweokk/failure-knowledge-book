#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《失效》PDF 构建：合并 Markdown → HTML(CSS) → PDF。"""
import os, re, subprocess, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # book/
PROJECT = os.path.dirname(ROOT)
OUT = os.path.join(PROJECT, 'dist')

ORDER = [
    ('00-前言.md', None),
    ('01-元问题', None), ('02-解剖学', None), ('03-机制', None),
    ('04-领域特征', None), ('05-用法', None), ('06-边界', None),
    ('07-附录', None), ('术语表.md', None),
]

def natural(files):
    def key(f):
        m = re.match(r'(\d+)', os.path.basename(f))
        return (int(m.group(1)) if m else 999, f)
    return sorted(files, key=key)

def collect():
    parts = []
    for name, _ in ORDER:
        p = os.path.join(ROOT, name)
        if os.path.isfile(p):
            parts.append(p)
        elif os.path.isdir(p):
            fs = [os.path.join(p, f) for f in os.listdir(p) if f.endswith('.md') and not f.startswith('._')]
            parts.extend(natural(fs))
    return parts

def strip_selfreports(t):
    # 去掉章末「（本章 N 字）」这类给自己看的标记
    t = re.sub(r'\n*（本章[\d,]+ 字）\s*$', '', t)
    return t

def main():
    files = collect()
    cover = '''<div class="cover">
<h1 class="covertitle">失败的知识</h1>
<p class="coversub">跨领域失效结构手册</p>
<p class="coverline">24 个机制 · 14 个领域 · 53 张案例卡</p>
<p class="covermeta">2026 年 11 月 · 中文版 v2.0</p>
</div>

'''
    def hz(x):
        return len(re.findall(r'[\u4e00-\u9fff]', x))
    body_hz = sum(hz(open(f, encoding='utf-8').read()) for f in files)
    colophon = ("""<div class="colophon">
<p class="ct">体例</p>
<p>机制为主，案例为辅。每个案例只写当事人在当时可见的信息，停在决策点，读者先判断再看结局。</p>
<p class="ct">规模</p>
<p>%s 汉字 · 24 章机制 · 14 个领域页 · 53 张完整案例卡 · 159 条案例索引</p>
<p class="ct">版本</p>
<p>v2.0 · 2026 年 11 月</p>
</div>
<!--TOC-HERE-->

""") % f"{body_hz:,}"
    chunks = [cover, colophon]
    for i, f in enumerate(files):
        t = open(f, encoding='utf-8').read()
        t = strip_selfreports(t)
        # 章首分页（首篇不分页）
        if i:
            t = '<div class="pagebreak"></div>\n\n' + t
        chunks.append(t)
    md = '\n\n'.join(chunks)
    mdpath = os.path.join(OUT, '失败的知识-合并.md')
    open(mdpath, 'w', encoding='utf-8').write(md)

    css = open(os.path.join(ROOT, '_spec', 'book.css'), encoding='utf-8').read()
    csspath = os.path.join(OUT, 'book.css')
    open(csspath, 'w', encoding='utf-8').write(css)

    htmlpath = os.path.join(OUT, '失败的知识.html')
    subprocess.run([
        'pandoc', mdpath, '-f', 'markdown+pipe_tables+footnotes', '-t', 'html5',
        '--standalone', '--toc', '--toc-depth=2', '--css', csspath,
        '--metadata', 'title=失败的知识', '--metadata', 'lang=zh-CN',
        '-o', htmlpath,
    ], check=True)

    # 把 pandoc 生成的目录挪到封面与版本页之后
    h = open(htmlpath, encoding='utf-8').read()
    m = re.search(r'<nav id="TOC".*?</nav>', h, re.S)
    if m and '<!--TOC-HERE-->' in h:
        nav = m.group(0)
        h = h.replace(nav, '').replace('<!--TOC-HERE-->', nav)
        open(htmlpath, 'w', encoding='utf-8').write(h)

    pdfpath = os.path.join(OUT, '失败的知识.pdf')
    subprocess.run(['weasyprint', htmlpath, pdfpath], check=True)
    print('PDF:', pdfpath, os.path.getsize(pdfpath) // 1024, 'KB')
    print('篇目:', len(files))

if __name__ == '__main__':
    main()
