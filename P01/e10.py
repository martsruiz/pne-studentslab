from Seq1 import Seq
genes = ["U5", "ADA", "FXN", "FRAT1"]
sequence = "../sequences/"
for i in genes:
    file = sequence + str(i) + ".txt"
    s = Seq()
    s.read_fasta(file)

