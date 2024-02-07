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


