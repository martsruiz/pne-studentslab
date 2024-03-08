from Client0 import Client
IP = "127.0.0.1"
PORT = 12345
c = Client(IP, PORT)
print(c)
print("Testing Ping...")
print(c.talk("PING"))
print("Testing GET...")
print(c.talk("GET"))
print("Testing Info...")
print(c.talk("INFO"))
print("Testing COMP...")
print(c.talk("COMP"))
print("Testing REV...")
print(c.talk("REV"))
