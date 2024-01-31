
with open("dna",  "r") as f:
    dic = {"A": 0,
           "C": 0,
           "T": 0,
           "G": 0}
    for line in f:
        for nucleotide in line:
            if nucleotide in dic:
                dic[nucleotide] += 1

    print(dic)
