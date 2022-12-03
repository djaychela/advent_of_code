import sys
from pathlib import Path

day = int(sys.argv[1])
filenames = [f"{day:02d}_01.py", f"{day:02d}_02.py", f"data/{day:02d}_test.txt", f"data/{day:02d}.txt"]

for file in filenames:
    print(f"Creating {file}...")
    Path(file).touch()
