from Client0 import Client
from Seq1 import Seq
from pprint import pprint


PRACTICE = 2
EXERCISE = 5
genes = "FRAT1"
sequence = "../sequences/"

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.33"  #"212.128.255.90" # your IP address
PORT = 1234
def get_sequence(gene):
    file_path = sequence + gene + ".txt"
    s = Seq()
    return s.read_fasta(file_path)

c = Client(IP, PORT)
print(c)


# -- Send a message to the server
sequences = get_sequence(genes) #sequencia completa del gen

def get_fragments(sequences):
    fragments = ""
    rounds = 0
    list = []
    for i in sequences:
        fragments += i
        if len(fragments) == 10:
            list.append(fragments)
            rounds += 1
            fragments = ""
        if rounds == 5:
            break
    return list






print(f"Gene {genes}: {sequences}")
response = c.talk(f"Sending {genes} Gene to the server, in fragments of 10 bases...")

fragments = get_fragments(sequences)
for i, fragment in enumerate(fragments, start=1):
    print(f"Fragment {i}: {fragment}")
    response = c.talk(f"Fragment {i}: {fragment}")
