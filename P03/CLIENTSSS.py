
from Client0 import Client

IP = "127.0.0.1"
PORT = 12345

c = Client(IP, PORT)
print(c)



def ping_response():
    print("Testing Ping...")
    print(c.talk("PING"))

def get_response(user_input):
    responses = []
    print("Testing Get...")
    response = c.talk(user_input)
    responses.append(response)
    return ( str(user_input) + ": " + str(response))


def info_response(response):
    print("Testing Info...")
    info_msg = str(response)
    response = c.talk(info_msg)
    print(response)
    return response


def comp_response(response):
    print("Testing COMP...")
    comp_msg = str(response)
    response = c.talk((comp_msg))
    print(comp_msg)
    return response

def rev_response(response):
    print("Testing REV...")
    rev_msg = str(response)
    response = c.talk((rev_msg))
    print(rev_msg)
    return response

def gene_response(response):
    print("Testing GENE...")
    gene_msg = response
    response = c.talk((gene_msg))
    return (str(gene_msg) + ": " + str(response))
def return_response():
    user_input = input("Please enter a input")
    if str("PING") in user_input:
        return ping_response()
    if str("GET") in user_input:
        return get_response(user_input)
    if str("INFO") in user_input:
        return info_response(user_input)
    if str("COMP") in user_input:
        return comp_response(user_input)
    if str("REV") in user_input:
        return rev_response(user_input)
    if str("GENE") in user_input:
        return gene_response(user_input)

print(return_response())
