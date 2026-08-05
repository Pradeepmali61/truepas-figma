import re
from pathlib import Path

root = Path('c:/Users/Administrator/OneDrive/Desktop/Facepe3/Truepas-figma')

pairs = [
    ('#cc0000', '#2727d6'),
    ('#CC0000', '#2727d6'),
    ('#ff3333', '#4e9af1'),
    ('#FF3333', '#4e9af1'),
    ('#990000', '#1b1b9e'),
    ('#660000', '#1b1b9e'),
    ('#fff5f5', '#e8f0fe'),
    ('#FFF5F5', '#e8f0fe'),
    ('#ffe5e5', '#d6e3f8'),
    ('#FFE5E5', '#d6e3f8'),
    ('rgba(204,0,0,0.75)', 'rgba(39,39,214,0.75)'),
]

files = list(root.glob('*.html')) + [root / 'styles.css']

for f in files:
    text = f.read_text(encoding='utf-8')
    new = text
    for old, newc in pairs:
        new = new.replace(old, newc)
    if new != text:
        f.write_text(new, encoding='utf-8')
        print('updated', f.name)
