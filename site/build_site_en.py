#!/usr/bin/env python3
"""英文版站点：与中文版同构，输出到 site/build-en，随后并入主站 /en/ 子路径。"""
import os, re, shutil

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SITE_DIR)
SRC = os.path.join(ROOT, 'book', 'en')
SITE = SITE_DIR
DOCS = os.path.join(SITE, 'docs-en')

PARTS = [
    ('01-meta', 'Part I　Meta-questions', 'ch'),
    ('02-anatomy', 'Part II　Anatomy', 'ch'),
    ('03-mechanisms', 'Part III　Twenty-four mechanisms', 'ch'),
    ('04-domains', 'Part IV　Fourteen domains', 'domain'),
    ('05-usage', 'Part V　How to use it', 'ch'),
    ('06-boundaries', 'Part VI　Boundaries', 'ch'),
]
APPX = {'A': 'appendix-a.md', 'B': 'appendix-b.md', 'C': 'appendix-c.md', 'D': 'appendix-d.md'}


def h1_of(path):
    for line in open(path, encoding='utf-8'):
        if line.startswith('# '):
            return line[2:].strip()
    return os.path.basename(path)[:-3]


def label(title):
    t = title.replace('｜', '|').split('|')[0].strip()
    return re.sub(r'\s+', ' ', t)


def slug_for(dirname, fname):
    n = re.match(r'(\d+)', fname)
    if dirname == '04-domains':
        return f'domain-{n.group(1)}.md'
    return f'ch{int(n.group(1)):02d}.md'


def build():
    if os.path.exists(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(DOCS)
    shutil.copy2(os.path.join(SRC, '00-preface.md'), os.path.join(DOCS, 'preface.md'))
    nav = [{'Home': 'index.md'}, {'Preface': 'preface.md'}]
    for dirname, part_label, _ in PARTS:
        src = os.path.join(SRC, dirname)
        items = []
        for f in sorted(os.listdir(src)):
            if not f.endswith('.md'):
                continue
            slug = slug_for(dirname, f)
            shutil.copy2(os.path.join(src, f), os.path.join(DOCS, slug))
            items.append({label(h1_of(os.path.join(src, f))): slug})
        nav.append({part_label: items})
    appx = []
    for f in sorted(os.listdir(os.path.join(SRC, '07-appendices'))):
        if not f.endswith('.md'):
            continue
        slug = APPX[f[0]]
        shutil.copy2(os.path.join(SRC, '07-appendices', f), os.path.join(DOCS, slug))
        appx.append({label(h1_of(os.path.join(SRC, '07-appendices', f))): slug})
    nav.append({'Appendices': appx})

    os.makedirs(os.path.join(DOCS, 'assets'), exist_ok=True)
    shutil.copy2(os.path.join(SITE, 'extra.css'), os.path.join(DOCS, 'assets', 'extra.css'))
    shutil.copy2(os.path.join(SITE, 'index-en.md'), os.path.join(DOCS, 'index.md'))

    cfg = {
        'site_name': 'The Knowledge of Failure',
        'site_description': 'A cross-domain manual of structural failure: twenty-four mechanisms, fourteen domains, 159 cases',
        'repo_url': 'https://github.com/Jweokk/failure-knowledge-book',
        'repo_name': 'GitHub',
        'site_url': 'https://tkf.fly2ai.top/en/',
        'docs_dir': 'docs-en',
        'site_dir': 'build-en',
        'use_directory_urls': True,
        'theme': {
            'name': 'material',
            'language': 'en',
            'features': ['navigation.sections', 'navigation.top', 'navigation.footer',
                         'navigation.tracking', 'toc.follow', 'search.suggest',
                         'search.highlight'],
            'palette': [{'scheme': 'default', 'primary': 'custom', 'accent': 'custom',
                         'toggle': {'icon': 'material/weather-night', 'name': 'Dark'}},
                        {'scheme': 'slate', 'primary': 'custom', 'accent': 'custom',
                         'toggle': {'icon': 'material/weather-sunny', 'name': 'Light'}}],
            'font': {'text': 'Noto Serif', 'code': 'Noto Sans Mono'},
        },
        'extra_css': ['assets/extra.css'],
        'extra_javascript': ['assets/shelf-counter.js'],
        'markdown_extensions': ['tables', 'attr_list', 'md_in_html', 'footnotes',
                                'admonition', 'pymdownx.details', 'pymdownx.superfences',
                                'pymdownx.tabbed', 'toc'],
        'plugins': [{'search': {'lang': ['en']}}],
        'nav': nav,
        'extra': {'alternate': [{'name':'English','link':'/en/','lang':'en'},{'name':'中文','link':'/','lang':'zh'}]},
        'copyright': 'Free and open · continuously revised',
    }
    import yaml
    with open(os.path.join(SITE, 'mkdocs-en.yml'), 'w', encoding='utf-8') as f:
        yaml.safe_dump(cfg, f, allow_unicode=True, sort_keys=False)
    print('en 导航块', len(nav))


if __name__ == '__main__':
    build()
