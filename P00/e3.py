from Seq0 import *
U5_file = seq_read_fasta("../sequences/U5.txt")
ADA_file = seq_read_fasta("../sequences/ADA.txt")
FRAT1 = seq_read_fasta("../sequences/FRAT1.txt")
FXN_file = seq_read_fasta("../sequences/FXN.txt")

print("Gene U5 -> Length: ", str(seq_len(U5_file)),"\nGene ADA -> Length: ", str(seq_len(ADA_file)),"\nGene FRAT1 -> Length: ", str(seq_len(FRAT1)),"\nGene FXN -> Length:", str(seq_len(FXN_file)))