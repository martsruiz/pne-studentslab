from Client0 import Client
from Seq1 import Seq
from pprint import pprint

PRACTICE = 2
EXERCISE = 4
genes = ["U5", "ADA", "FRAT1"]
sequence_folder = "../sequences/"

# Parámetros del servidor al que se va a hablar
IP = "212.128.255.90"  # Tu dirección IP
PORT = 1234

def get_sequence(gene):
    file_path = sequence_folder + gene + ".txt"
    s = Seq()
    return s.read_fasta(file_path)

# Crear un objeto cliente
c = Client(IP, PORT)
print(c)

# Enviar cada gen y su secuencia al servidor
for gene in genes:
    sequence = get_sequence(gene)
    print(f"Al servidor: Enviando el gen {gene} al servidor...")
    response = c.talk(f"Enviando el gen {gene} al servidor...")
    print(f"Desde el servidor: {response}")

    print(f"Al servidor: Enviando la secuencia del gen {gene} al servidor...")
    response = c.talk(f"Enviando la secuencia del gen {gene} al servidor... {sequence}")
    print(f"Desde el servidor: {response}")

print(f"-----| Práctica {PRACTICE}, Ejercicio {EXERCISE} |------")
