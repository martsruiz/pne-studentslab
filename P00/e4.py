from Seq0 import *
U5_file = seq_read_fasta("../sequences/U5.txt")
ADA_file = seq_read_fasta("../sequences/ADA.txt")
FRAT1 = seq_read_fasta("../sequences/FRAT1.txt")
FXN_file = seq_read_fasta("../sequences/FXN.txt")
bases = ["A", "C", "T", "G"]
sequences = [U5_file, ADA_file, FXN_file, FRAT1]
print("Gene U5")
for a in sequences:
    for i in bases:
        print(str(i), seq_count(a, i))


