from Client0 import Client
from Seq1 import Seq
from pprint import pprint
import termcolor

PRACTICE = 2
EXERCISE = 4
genes = ["U5", "ADA", "FRAT1"]
sequence = "../sequences/"

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.33"#"212.128.255.90" # your IP address
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
    print("To server: " + termcolor.colored("Sending " + (gene) + " Gene to the server...", "blue"))
    response = c.talk(termcolor.colored("Sending " + (gene) + " Gene to the server...", "green"))
    print("From Server:" + termcolor.colored(response, "green"))
    print("To server:" + termcolor.colored(sequences, "blue"))
    response = c.talk(termcolor.colored(sequences, "green"))
    print("From Server:" + termcolor.colored(response, "green"))




