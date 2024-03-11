import socket
import termcolor

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.97"  # the IP address depends on the machine running the server
clients_list = []
# Initialize connection counter
connection_counter = 0

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect...")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")
        connection_counter += 1
        clients_list.append(client_ip_port)

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-readable string
        msg = msg_raw.decode()

        # -- Print the received message

        print(f"CONNECTION {connection_counter}: CLIENT IP, PORT: {client_ip_port}\n Message received: " + termcolor.colored (msg, "green"))

        # -- Send a response message to the client
        response = f" ECHO: {msg}"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()
        if connection_counter == 5:
            for a, i in enumerate(clients_list, start=0):
                print(f"Client {a}: {i} ")
# -- Close the server socket
ls.close()
