from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("IATTC")

print("Sequence 1:", "(Length:", s1.len(), ")", s1 , "\n BASES:", s1.count(),"\nSequence 2:", "(Length:", s2.len(), ")", s2, "\n BASES:", s2.count(), "\nSequence 3:", "(Length:", s3.len(), ")", s3, "\n BASES:", s3.count())