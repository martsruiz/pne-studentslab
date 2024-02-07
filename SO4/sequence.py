from pathlib import Path

FILENAME = "sequences/FXN.txt"
file_contents = Path(FILENAME).read_text()
lines = file_contents.split("\n")
lines.pop(0)

print(len("".join(lines)))