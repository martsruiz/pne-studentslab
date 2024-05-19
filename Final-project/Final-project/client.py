import http.client
import json

SERVER = "localhost"
PORT = 8080

conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
user_request = input("Please enter the service you want to request (1,2,3,4,5,6,7), press 0 to exit")


if user_request == "1":
    user_request1 = input("Enter the number of species you want to know")
    request = f"/listSpecies?limit={int(user_request1)}&json=1"

elif user_request == "2":
    user_request1 = input("Select the specie ")
    request = f"/karyotype?species={user_request1}&json=1"

elif user_request == "3":
    user_request1 = input("Select the specie")
    user_request2 = input("Select the chromosome")
    request = f"/chromosomeLength?species={user_request1}&chromo={user_request2}&json=1"

elif user_request == "4":
    user_request1 = input("Select the gene")
    request = f"/geneSeq?gene={user_request1}&json=1"


elif user_request == "5":
    user_request1 = input("Select the gene")
    request = f"/geneInfo?gene={user_request1}&json=1"

elif user_request == "6":
    user_request1 = input("Select the gene")
    request = f"/geneCalc?gene={user_request1}&json=1"

elif user_request == "7":
    user_request1 = input("Select the chromosome")
    user_request2 = input("Select the start position")
    user_request3 = input("Select the end position")

    request = f"/geneList?chromo={int(user_request1)}&start={user_request2}&end={user_request3}&json=1"

else:
    print("Sorry, we have an error")

try:
    conn.request("GET", request)
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
try:
    person = json.loads(data1)  # Convert the string to JSON
    # Print the JSON response
    print(person)
except json.JSONDecodeError:
    print("ERROR! Response is not valid JSON")


