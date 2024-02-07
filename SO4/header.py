
from pathlib import Path
def print_filename(filename):
    FILENAME = str(filename)
    file_contents = Path(FILENAME).read_text()
    first_line = file_contents.find("\n")
    new_sequence = file_contents[:first_line]
    return new_sequence

f = print_filename("sequences/RNU6_269P.txt")
print("First line of the RNU6_269P.txt file: ", str(f))

def print_filename1(filename):
    FILENAME = str(filename)
    file_contents = Path(FILENAME).read_text()
    lines = file_contents.split("\n")
    first_line = lines[0]
    return first_line
f = print_filename1("sequences/RNU6_269P.txt")
print("First line of the RNU6_269P.txt file: ", str(f))


