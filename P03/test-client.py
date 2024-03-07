import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 12345
IP = "127.0.0.1"  # it depends on the machine the server is running

# First, create the socket
# We will always use these parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be sent, only bytes
# It's necessary to encode the string into bytes
user_input = input("Please enter your message: ")
s.send(str.encode(user_input))

# Receive response from the server
response = s.recv(2048).decode("utf-8")

# Print the response received from the server
print("Response from server:", response)

# Close the socket
s.close()


