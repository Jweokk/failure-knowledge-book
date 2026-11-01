#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《Failure》English edition PDF: normalize headings → merge → HTML → PDF."""
import os, re, subprocess, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # book/
PROJECT = os.path.dirname(ROOT)
EN = os.path.join(ROOT, 'en')
OUT = os.path.join(PROJECT, 'dist')

PARTS = ['01-meta', '02-anatomy', '03-mechanisms', '04-domains', '05-usage', '06-boundaries', '07-appendices']

def natural(fs):
    def key(f):
        m = re.match(r'(\d+)', os.path.basename(f))
        return (int(m.group(1)) if m else 999, f)
    return sorted(fs, key=key)

def normalize(text, chapnum):
    """## 1 What It Is → ## 11.1 What It Is ; unify heading case."""
    def repl(m):
        n = m.group(1)
        title = m.group(2).strip()
        title = re.sub(r'\bwhat it is\b', 'What It Is', title, flags=re.I)
        title = re.sub(r'\bhow it grows\b', 'How It Grows', title, flags=re.I)
        return f'## {chapnum}.{n} {title}'
    return re.sub(r'(?m)^## (\d{1,2}) (?!\d)(.+)$', repl, text)

def collect():
    out = []
    p = os.path.join(EN, '00-preface.md')
    if os.path.exists(p):
        out.append((None, p))
    for part in PARTS:
        d = os.path.join(EN, part)
        if not os.path.isdir(d):
            continue
        for f in natural([x for x in glob.glob(os.path.join(d, '*.md'))]):
            m = re.match(r'(\d+)-ch(\d+)', os.path.basename(f))
            out.append((int(m.group(2)) if m else None, f))
    return out

COVER = """<div class="cover">
<h1 class="covertitle">The Knowledge of Failure</h1>
<p class="coversub">A Cross-Domain Manual of Structural Failure</p>
<p class="coverline">24 mechanisms &middot; 14 domains &middot; 53 case cards</p>
<p class="covermeta">November 2026 &middot; English edition v1.0</p>
</div>

"""

def main():
    files = collect()
    words_all = sum(len(re.findall(r"[A-Za-z][A-Za-z'-]*", open(f, encoding='utf-8').read())) for _, f in files)
    colophon = """<div class="colophon">
<p class="ct">METHOD</p>
<p>Mechanisms first, cases second. Every case is told only from what the people in it could see at the time, and stops at the decision, so the reader judges before turning the page.</p>
<p class="ct">SCOPE</p>
<p>%s words &middot; 24 mechanism chapters &middot; 14 domain pages &middot; 53 full case cards &middot; 159 indexed cases</p>
<p class="ct">EDITION</p>
<p>v1.0 &middot; November 2026</p>
</div>
<!--TOC-HERE-->

""" % f"{words_all:,}"
    chunks = [COVER, colophon]
    for idx, (chap, f) in enumerate(files):
        t = open(f, encoding='utf-8').read()
        t = re.sub(r'\n*\(?Chapter (length|draft)[^\n]*\)?\s*$', '', t)
        if chap:
            t = normalize(t, chap)
        if idx > 1:
            t = '<div class="pagebreak"></div>\n\n' + t
        chunks.append(t)
    md = '\n\n'.join(chunks)
    mdpath = os.path.join(OUT, 'failure-knowledge.md')
    open(mdpath, 'w', encoding='utf-8').write(md)

    csspath = os.path.join(ROOT, '_spec', 'book-en.css')
    htmlpath = os.path.join(OUT, 'failure-knowledge.html')
    subprocess.run(['pandoc', mdpath, '-f', 'markdown+pipe_tables+footnotes', '-t', 'html5',
                    '--standalone', '--toc', '--toc-depth=2', '--css', csspath,
                    '--metadata', 'title=The Knowledge of Failure', '--metadata', 'lang=en',
                    '-o', htmlpath], check=True)
    h = open(htmlpath, encoding='utf-8').read()
    m = re.search(r'<nav id="TOC".*?</nav>', h, re.S)
    if m and '<!--TOC-HERE-->' in h:
        h = h.replace(m.group(0), '').replace('<!--TOC-HERE-->', m.group(0))
        open(htmlpath, 'w', encoding='utf-8').write(h)

    pdfpath = os.path.join(OUT, 'failure-knowledge.pdf')
    subprocess.run(['weasyprint', htmlpath, pdfpath], check=True)
    words = len(re.findall(r"[A-Za-z][A-Za-z'-]*", md))
    print('files', len(files), 'words', words, 'PDF', pdfpath,
          os.path.getsize(pdfpath) // 1024, 'KB')

if __name__ == '__main__':
    main()
