from Seq0 import *
U5_file = seq_read_fasta("../sequences/U5.txt")
ADA_file = seq_read_fasta("../sequences/ADA.txt")
FRAT1 = seq_read_fasta("../sequences/FRAT1.txt")
FXN_file = seq_read_fasta("../sequences/FXN.txt")

sequences1 = ["Gene U5", "Gene ADA", "Gene FXN", "Gene FRAT1"]
sequences = [U5_file, ADA_file, FXN_file, FRAT1]

for sequence_name, sequence in zip(sequences1,sequences):

    n = seq_count(sequence)
    print(sequence_name, n)
