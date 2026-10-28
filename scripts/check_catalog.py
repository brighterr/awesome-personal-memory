"""Validate local catalog structure and Markdown links; does not fetch external URLs."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import datetime
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
data = json.loads((ROOT / 'data/catalog.json').read_text(encoding='utf-8'))
datetime.date.fromisoformat(data['as_of'])
required = {
    'benchmarks': ['name', 'year', 'group', 'priority', 'task', 'scale', 'metric', 'limit', 'url'],
    'methods': ['name', 'type', 'idea', 'result', 'setting', 'caveat', 'url'],
}
for kind, fields in required.items():
    names = set()
    for entry in data[kind]:
        for field in fields:
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                errors.append(f'{kind}: missing/empty {field} in {entry.get("name")}')
        name = entry.get('name', '').casefold()
        if name in names:
            errors.append(f'Duplicate name: {name}')
        names.add(name)
        for resource in entry.get('resources', []):
            url = urlsplit(resource['url'])
            if url.scheme != 'https' or not url.netloc or not resource.get('note') or not resource.get('check_scope'):
                errors.append(f'Invalid resource metadata: {resource}')
            datetime.date.fromisoformat(resource['link_checked_on'])
        for field in ['url', 'url2', 'evidence']:
            if field in entry:
                url = urlsplit(entry[field])
                if url.scheme != 'https' or not url.netloc:
                    errors.append(f'Invalid source URL: {entry[field]}')

def anchors(path):
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    found = set(re.findall(r'<a\s+(?:id|name)=[\"\']([^\"\']+)', text))
    counts = {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        title = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', title)
        slug = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')
        n = counts.get(slug, 0)
        found.add(slug if n == 0 else f'{slug}-{n}')
        counts[slug] = n + 1
    return found

checked = 0
for path in ROOT.rglob('*.md'):
    text = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8'), flags=re.S)
    for link in re.findall(r'\]\(([^\s)]+)\)', text):
        parts = urlsplit(link)
        if parts.scheme or parts.netloc:
            continue
        target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
        checked += 1
        if not target.is_relative_to(ROOT):
            errors.append(f'{path.relative_to(ROOT)}: non-portable path {link}')
        elif not target.exists():
            errors.append(f'{path.relative_to(ROOT)}: missing {link}')
        elif parts.fragment and target.suffix == '.md' and unquote(parts.fragment) not in anchors(target):
            errors.append(f'{path.relative_to(ROOT)}: missing anchor {link}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'OK: {len(data["benchmarks"])} benchmark-family records, {len(data["methods"])} method/configuration records, {checked} local links and anchors.')
print('External URLs and research claims were not validated by this check.')
