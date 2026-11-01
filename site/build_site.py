#!/usr/bin/env python3
"""把 build/ 下的成书 Markdown 生成为 mkdocs-material 静态站。

文件名统一换成 ASCII slug（ch01、domain-01、appendix-a），页面标题取 Markdown 的一级标题。
中文交叉引用（「第 11 章」）在正文里是纯文本，不做自动链接，导航与内链由本脚本生成。
"""
import os, re, shutil, sys

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SITE_DIR)
SRC = os.path.join(ROOT, 'book')
SITE = SITE_DIR
DOCS = os.path.join(SITE, 'docs')

PARTS = [
    ('01-元问题', '第一部　元问题', 'ch'),
    ('02-解剖学', '第二部　解剖学', 'ch'),
    ('03-机制', '第三部　二十四个机制', 'ch'),
    ('04-领域特征', '第四部　十四个领域', 'domain'),
    ('05-用法', '第五部　怎么用', 'ch'),
    ('06-边界', '第六部　边界', 'ch'),
]
APPX = {'A': 'appendix-a.md', 'B': 'appendix-b.md', 'C': 'appendix-c.md', 'D': 'appendix-d.md'}


def h1_of(path):
    for line in open(path, encoding='utf-8'):
        if line.startswith('# '):
            return line[2:].strip()
    return os.path.basename(path)[:-3]


def label(title):
    """导航标签：去掉中英并列的英文部分，机制章只留中文名。"""
    t = title.replace('｜', '|').split('|')[0].strip()
    return re.sub(r'\s+', ' ', t)


def slug_for(dirname, fname):
    n = re.match(r'(\d+)', fname)
    if dirname == '04-领域特征':
        return f'domain-{n.group(1)}.md'
    return f'ch{int(n.group(1)):02d}.md'


def build():
    if os.path.exists(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(DOCS)
    manifest = {}          # slug -> 标题
    nav = [{'首页': 'index.md'}, {'前言：读者契约': 'preface.md'}]
    shutil.copy2(os.path.join(SRC, '00-前言.md'), os.path.join(DOCS, 'preface.md'))
    manifest['preface.md'] = label(h1_of(os.path.join(SRC, '00-前言.md')))

    for dirname, part_label, _ in PARTS:
        src = os.path.join(SRC, dirname)
        items = []
        for f in sorted(os.listdir(src)):
            if not f.endswith('.md'):
                continue
            slug = slug_for(dirname, f)
            shutil.copy2(os.path.join(src, f), os.path.join(DOCS, slug))
            t = label(h1_of(os.path.join(src, f)))
            manifest[slug] = t
            items.append({t: slug})
        nav.append({part_label: items})

    # 附录
    appx_items = []
    for f in sorted(os.listdir(os.path.join(SRC, '07-附录'))):
        if not f.endswith('.md'):
            continue
        letter = f[0]
        slug = APPX[letter]
        shutil.copy2(os.path.join(SRC, '07-附录', f), os.path.join(DOCS, slug))
        t = label(h1_of(os.path.join(SRC, '07-附录', f)))
        manifest[slug] = t
        appx_items.append({t: slug})
    nav.append({'附录': appx_items})

    shutil.copy2(os.path.join(SRC, '术语表.md'), os.path.join(DOCS, 'glossary.md'))
    manifest['glossary.md'] = label(h1_of(os.path.join(SRC, '术语表.md')))
    nav.append({'术语表': 'glossary.md'})

    # 静态资源
    files_dir = os.path.join(DOCS, 'files')
    os.makedirs(files_dir)
    for name, out in [('失败的知识.pdf', 'failure-knowledge-zh.pdf'),
                      ('failure-knowledge.pdf', 'failure-knowledge-en.pdf'),
                      ('失败的知识-双语定稿-20261102.tar.gz', 'failure-knowledge-src.tar.gz')]:
        src = os.path.join(ROOT, 'dist', name)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(files_dir, out))
    os.makedirs(os.path.join(DOCS, 'assets'), exist_ok=True)
    shutil.copy2(os.path.join(SITE, 'extra.css'), os.path.join(DOCS, 'assets', 'extra.css'))
    shutil.copy2(os.path.join(SITE, 'index.md'), os.path.join(DOCS, 'index.md'))
    shutil.copy2(os.path.join(SITE, 'shelf-counter.js'), os.path.join(DOCS, 'assets', 'shelf-counter.js'))

    cfg = {
        'site_name': '失败的知识',
        'site_description': '跨领域失效结构手册：二十四个机制、十四个领域、一百五十九个案例',
        'repo_url': 'https://github.com/Jweokk/failure-knowledge-book',
        'repo_name': 'GitHub',
        'site_url': 'https://tkf.fly2ai.top/',
        'docs_dir': 'docs',
        'site_dir': 'build',
        'use_directory_urls': True,
        'theme': {
            'name': 'material',
            'language': 'zh',
            'features': ['navigation.sections', 'navigation.top', 'navigation.footer',
                         'navigation.tracking', 'toc.follow', 'search.suggest',
                         'search.highlight', 'content.code.copy'],
            'palette': [{'scheme': 'default', 'primary': 'custom', 'accent': 'custom',
                         'toggle': {'icon': 'material/weather-night', 'name': '深色'}},
                        {'scheme': 'slate', 'primary': 'custom', 'accent': 'custom',
                         'toggle': {'icon': 'material/weather-sunny', 'name': '浅色'}}],
            'font': {'text': 'Noto Serif SC', 'code': 'Noto Sans Mono'},
        },
        'extra_css': ['assets/extra.css'],
        'extra_javascript': ['assets/shelf-counter.js'],
        'markdown_extensions': ['tables', 'attr_list', 'md_in_html', 'footnotes',
                                'admonition', 'pymdownx.details', 'pymdownx.superfences',
                                'pymdownx.tabbed', 'toc'],
        'plugins': [{'search': {'lang': ['zh', 'en']}}],
        'nav': nav,
        'extra': {'alternate': [{'name':'中文','link':'/','lang':'zh'},{'name':'English','link':'/en/','lang':'en'}]},
        'copyright': '免费公开 · 持续校订',
    }
    import yaml
    with open(os.path.join(SITE, 'mkdocs.yml'), 'w', encoding='utf-8') as f:
        yaml.safe_dump(cfg, f, allow_unicode=True, sort_keys=False)
    import json
    with open(os.path.join(SITE, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print('页面', len(manifest), '导航块', len(nav))


if __name__ == '__main__':
    build()
