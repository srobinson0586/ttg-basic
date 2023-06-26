import os
from pathlib import Path

os.chdir(Path(__file__).parent)

file_path = Path('dev_python_files.txt')
folder_paths = [Path(x.split()[0]) for x in file_path.read_text().splitlines()]

for folder in folder_paths:
    folder.mkdir()