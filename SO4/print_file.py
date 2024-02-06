
from pathlib import Path
def print_filename(filename):
    FILENAME = str(filename)
    file_contents = Path(FILENAME).read_text()
    return file_contents

print(print_filename("sequences/ADA.txt"))
print(print_filename("sequences/FRAT1.txt"))
print(print_filename("sequences/FXN.txt"))
print(print_filename("sequences/RNU6_269P.txt"))
print(print_filename("sequences/U5.txt"))

