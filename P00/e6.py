
from Seq0 import *
U5_file = seq_read_fasta("../sequences/U5.txt")
short_seq = seq_reverse(U5_file, 20)
print("U5_file")
print("Fragment:", short_seq)
print("Reverse:" , short_seq[::-1])
