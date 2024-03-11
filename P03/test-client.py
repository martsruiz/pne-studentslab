from Client0 import Client

IP = "127.0.0.1"
PORT = 12345

c = Client(IP, PORT)
print(c)
def ping_response():
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

n = info_response(responses[0])
def comp_response(response):
    print("Testing COMP...")
    comp_msg = "COMP " + str(response)
    response = c.talk((comp_msg))
    print("COMP " + str(response))
    return response
comp = comp_response(responses[0])
def rev_response(response):
    print("Testing REV...")
    rev_msg = "REV " + str(response)
    response = c.talk((rev_msg))
    print("REV " + str(response))
    return response
rev = rev_response(responses[0])

def gene_response():
    genes = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
    print("Testing GENE...")

    for gene in genes:
        gene_msg = "GENE " + str(gene)
        response = c.talk((gene_msg))
        print("GENE " + str(gene)+ " " + str(response))

    return response

gene = gene_response()

