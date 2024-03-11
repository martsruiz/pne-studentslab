from Client0 import Client

IP = "127.0.0.1"
PORT = 12345

c = Client(IP, PORT)
print(c)
print("Testing Ping...")
print(c.talk("PING"))

def get_response():
    responses = []
    print("Testing Get...")
    for i in range(5):
        response = c.talk("GET" + str(i))
        responses.append(response)
        print("GET " + str(i) + ": " + str(response))
    return responses

responses = get_response()

def info_response(response):
    print("Testing Info...")
    info_msg = "INFO " + str(response)
    response = c.talk(info_msg)
    print(response)
    return response

print(info_response(responses[0]))
