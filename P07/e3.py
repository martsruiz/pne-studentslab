import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id/ENSG00000207552"
PARAMETERS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMETERS
print(URL)

conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMETERS)
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

print("Gene:", "MIR633")
print("Description:", person["desc"])
print("Bases:", person["seq"])
