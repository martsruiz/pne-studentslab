import socket


class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

    def talk(self, command):
        # Create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Connect to the server
            s.connect((self.server_ip, self.server_port))

            # Send command to the server
            s.send(command.encode())

            # Receive response from the server
            response = s.recv(2048).decode("utf-8")

            # Print the response received from the server
            print(response)

        except ConnectionRefusedError:
            print("Error: Connection refused. Make sure the server is running.")

        finally:
            # Close the socket
            s.close()


# Create a Client instance
client = Client("127.0.0.1", 12345)

# Define commands to test server functionalities
commands = [
    "PING",
    "GET 0",
    "INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "GENE U5",
    "GENE ADA",
    "GENE FRAT1",
    "GENE FXN",
    "GENE RNU6_269P"
]

# Test each command
for command in commands:
    print("* Testing", command)
    client.talk(command)
