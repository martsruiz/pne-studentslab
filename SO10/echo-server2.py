import socket
import termcolor

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.150"  # the IP address depends on the machine running the server

# Initialize connection counter
connection_counter = 0

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
print("Waiting for Clients to connect...")

while True:
    # Accept a new connection
    (rs, address) = ls.accept()

    # Increment connection counter
    connection_counter += 1

    print("A client has connected to the server!")

    # Print client's IP and port
    print(f"Connection {connection_counter}. Client IP, PORT {address}")

    # Receive message from client
    msg = rs.recv(2048).decode("utf-8")
    print("Message received: " + termcolor.colored(msg, "yellow"))

    # Send the received message back to the client
    rs.send(msg.encode())

    # Close the client socket
    rs.close()

# -- Close the server socket
ls.close()
