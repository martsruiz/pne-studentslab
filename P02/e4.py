from Client0 import Client
from Seq1 import Seq
from pprint import pprint


PRACTICE = 2
EXERCISE = 4
genes = ["U5", "ADA", "FRAT1"]
sequence = "../sequences/"

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.90" # your IP address
PORT = 1234
def get_sequence(gene):
    file_path = sequence + gene + ".txt"
    s = Seq()
    return s.read_fasta(file_path)

c = Client(IP, PORT)
print(c)


# -- Send a message to the server
for gene in genes:
    sequences = get_sequence(gene)
    print(f"To server: Sending {gene} Gene to the server...")
    response = c.talk(f"Sending {gene} Gene to the server...")
    print(f"From Server: {response}")
    print(f"To server: {sequences} ")
    response = c.talk(f" {sequences} ")
    print(f"From Server: {response}")




