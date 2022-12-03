import sys
import pathlib

day = sys.argv[1]
filenames = []
current_dir = pathlib.Path(__file__).parent.absolute()

filenames.append(pathlib.Path(current_dir / f"{day}_1.py"))
filenames.append(pathlib.Path(current_dir / f"{day}_2.py"))
filenames.append(pathlib.Path(current_dir / "data" / f"{day}.txt"))
filenames.append(pathlib.Path(current_dir / "data" / f"{day}_test.txt"))

for file in filenames:
    with open(file, "w") as f:
        pass
