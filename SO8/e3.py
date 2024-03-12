import socket

# SERVER IP, PORT
PORT = 1234
IP = "212.128.255.30"#  depends on the computer the server is running tiene que ser el ID del ordenador al que queremos mandar
ok = True
while ok:
  # -- Ask the user for the message
    user_input = input("Please enter your message")

  # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # -- Establish the connection to the Server
    s.connect((IP, PORT))

  # -- Send the user message
    s.send(str.encode(user_input))

  # -- Close the socket
    s.close()
    ok = False


