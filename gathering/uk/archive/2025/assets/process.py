from pathlib import Path
import subprocess

dirname = Path().resolve().name

Path('smaller').mkdir(exist_ok=True)

for f in Path().iterdir():
    if f.is_file() and f.suffix == '.jpg':
        spath = (Path('smaller') / f.name).with_suffix('.webp')
        if not spath.exists():
            subprocess.run(['convert','-resize','200',str(f),str(spath)])

        print(f'<a href="assets/{dirname}/{f}"><img src="assets/{dirname}/{spath}"></a>')
