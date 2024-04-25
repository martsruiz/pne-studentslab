import http.client
import json
from Seq1 import Seq

def info_response(msg):
    s1 = Seq(str(msg))
    length = s1.len()
    base_counts = s1.count()

    total_bases = sum(base_counts.values())

    result_str = f"Length: {length}\n"
    maximum_key = max(base_counts, key=base_counts.get)

    for base, count in base_counts.items():
        percentage = round(count / total_bases * 100, 1)
        result_str += f"{base}: {count} ({percentage}%)\n"



    result_str += f"Most frequent Base: {maximum_key}"

    return result_str

genes = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSDARG00000009026"
}
user_input= input("Please enter a gene").upper()
USER_ENS = genes[str(user_input)]

SERVER = "rest.ensembl.org"
ENDPOINT_1 = "/sequence/id/"
ENDPOINT_COMP = ENDPOINT_1 + USER_ENS
PARAMETERS = "?content-type=application/json"
URL = SERVER + ENDPOINT_COMP+ PARAMETERS
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT_COMP + PARAMETERS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()


# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1) # aqui convertimos el string en json

print("Gene:", str(user_input))
print("Description:", person["desc"])
sequence = person["seq"]

print(info_response(sequence))



