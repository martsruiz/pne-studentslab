from Seq0 import *
U5_file = seq_read_fasta("../sequences/U5.txt")
print(seq_reverse(U5_file, 20))
print(seq_complement(U5_file))
