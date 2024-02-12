def seq_ping():
    print("OK")


from pathlib import Path
def seq_read_fasta(filename):
    count = 0
    file_contents = Path(filename).read_text()
    first_line = file_contents.find("\n")
    new_sequence = file_contents[first_line:]
    n = new_sequence.replace("\n", "")
    return n

def seq_len(seq):
    return len(seq)

def seq_count(seq, base):
    count = 0
    for i in seq:
        if i == base:
            count += 1
    return count

def seq_count(seq):
    bases_dic = {"A": 0,
                 "C": 0,
                 "T": 0,
                 "G": 0}

    for base in seq:
        if base in bases_dic:
            bases_dic[base] += 1

    return bases_dic


def seq_reverse(seq, n):
    short_sequence = seq[:n]

    return short_sequence

def seq_complement(seq) :
    short_sequence = seq_reverse(seq, 20)
    dic = {"A": "T",
           "T": "A",
           "C": "G",
           "G": "C"}
    for i in short_sequence:
        if i in dic:
            print(dic[i], end="")















