from pathlib import Path

FILENAME = "sequences/FXN.txt"
file_contents = Path(FILENAME).read_text()
lines = file_contents.split("\n")
lines.pop(0)

print(len("".join(lines)))

def count_length(filename):
    FILENAME = str(filename)
    filename_file = Path(FILENAME).read_text()
    first_line = filename_file.find("\n")
    body = filename_file[first_line:]
    bodys = body.replace("\n", "")
    length = len(bodys)
    return length

print(count_length("sequences/FXN.txt"))