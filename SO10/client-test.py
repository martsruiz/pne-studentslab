from Client0 import Client
import termcolor
IP = "192.168.1.40"
PORT = 8081

c = Client(IP, PORT)
for i in range(5):
    msg = "Message " + str(i)
    response = c.talk(msg)

    print(f"To server: " + termcolor.colored(msg, "blue"))
    print (f" From server: "+ termcolor.colored("ECHO: "+ response,  "green"))

