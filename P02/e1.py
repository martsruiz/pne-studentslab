from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "192.168.1.40" #"192.168.1.45" # your IP address
PORT = 1234 #8080

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.ping()
