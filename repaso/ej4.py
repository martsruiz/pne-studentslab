from Seq1 import Seq
from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.255.30" # your IP address
PORT = 1234



genes = ["U5", "FRAT1", "ADA"]
sequence = "../sequences/"
def get_sequence(gene):
    a = str(sequence) + str(gene) + ".txt"
    s = Seq()
    return s.read_fasta(a)

# -- Create a client object
c = Client(IP, PORT)
print(c)
for gene in genes:
    sequences = get_sequence(gene)
    print(f"To server: Sending {gene} Gene to the server...")
    response = c.talk(f"Sending {gene} Gene to the server...")
    print(f"From Server: {response}")
    print(f"To server: {sequences} ")
    response = c.talk(f" {sequences} ")
    print(f"From Server: {response}")


