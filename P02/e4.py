from Client0 import Client
from Seq1 import Seq
from pprint import pprint


PRACTICE = 2
EXERCISE = 4
genes = ["U5", "ADA", "FRAT1"]
sequence = "../sequences/"

# -- Parameters of the server to talk to
IP = "212.128.255.90" # your IP address
PORT = 1234
def get_sequence():
    for i in genes:
        file = sequence + str(i) + ".txt"
        s = Seq()
        complete_file = s.read_fasta(file)
    return complete_file

sequences = get_sequence()
c = Client(IP, PORT)
print(c)
# -- Send a message to the server
for a in genes:
    print(f"To server: Sending {a} Gene to the server...")
    response = c.talk(f"Sending {a} Gene to the server...")
    print(f"From Server: {response}")
    for j in sequences:
        print(f"To server:  {j} ")
        response = c.talk(f"Sending {a} Gene to the server...")
        print(f"From Server: {response}")





