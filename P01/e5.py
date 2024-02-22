from Seq1 import Seq
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("IATTA")

def count2 (base):
    bases_list = ["A", "C", "T", "G"]
    for i in bases_list:
        n = base.count_base(i)
        print(f"{i}:{n}")


print(f"Sequence 0: (Length: {s1.len()}) {s1}")
count2(s1)
print(f"Sequence 1: (Length: {s2.len()}) {s2}")
count2(s2)
print(f"Sequence 2: (Length: {s3.len()}) {s3}")
count2(s3)
