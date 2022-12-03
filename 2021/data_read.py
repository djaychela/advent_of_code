import pathlib

def read_file(file_name):
    current_dir = pathlib.Path(__file__).parent.absolute()
    file_path = pathlib.Path(current_dir / "data" / file_name)

    with open(file_path, "r") as file:
        content = file.readlines()

    return content

