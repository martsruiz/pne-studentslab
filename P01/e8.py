from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("IATTA")

print("Sequence 1:", "(Length:", s1.len(), ")", s1 , "\n Bases:", s1.count(),"\n Rev:", s1.reverse(),"\n Com:", s1.complement(),
      "\nSequence 2:", "(Length:", s2.len(), ")", s2, "\n Bases:", s2.count(),"\n Rev:",s2.reverse(),"\n Com:", s2.complement(),
      "\nSequence 3:", "(Length:", s3.len(), ")", s3, "\n Bases:", s3.count(),"\n Rev:", s3.reverse(),"\n Com:",s3.complement())

