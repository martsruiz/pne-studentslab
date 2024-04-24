import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMETERS = "?content-type=application/json"
url = ENDPOINT + PARAMETERS


print()
print(f"Server: {SERVER}")
print(f"URL: {url}")

conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", url)
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

print("CONTENT:", person["ping"])
if person["ping"] == 1:
    print("PING OK! The database is running!")