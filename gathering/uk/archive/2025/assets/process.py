from pathlib import Path
import subprocess

dirname = Path().resolve().name

Path('smaller').mkdir(exist_ok=True)

url = '{{site.url}}/gathering/uk/archive/2025/assets/'+dirname

for f in sorted(Path().iterdir(), key=lambda f: f.name):
    if f.is_file() and f.suffix == '.jpg':
        spath = (Path('smaller') / f.name).with_suffix('.webp')
        if not spath.exists():
            subprocess.run(['convert','-resize','200',str(f),str(spath)])

        print(f'<a href="{url}/{f}"><img src="{url}/{spath}"></a>')
