from Seq1 import Seq


# Create a Null sequence
s = Seq()
FILENAME = "../sequences/U5.txt"
n = s.read_fasta(FILENAME)

print("Sequence 1:", "(Length:", s.len(), ")", n , "\n Bases:", s.count(),"\n Rev:", s.reverse(),"\n Com:", s.complement())


