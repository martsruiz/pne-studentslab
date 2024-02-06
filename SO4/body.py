from pathlib import Path

FILENAME = "sequences/U5.txt"
file_contents = Path(FILENAME).read_text()
lines = file_contents.split("\n")
for i in range (1, len (lines)):
    print(lines[i])



