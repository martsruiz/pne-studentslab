from Seq1 import Seq
print("-----| Practice 1, Exercise 10 |------")
genes = ["U5", "ADA", "FXN", "FRAT1", "RNU6_269P"]
sequence = "../sequences/"
for i in genes:
    file = sequence + str(i) + ".txt"
    s = Seq()
    s.read_fasta(file)
    dic_count = s.count()
    maximum_key  = max(dic_count, key = dic_count.get)
    print(f"Gene {i} : Most frequent Base: {maximum_key}")



















































