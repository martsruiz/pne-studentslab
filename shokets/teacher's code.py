import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8081
IP = "212.128.255.64" # it depends on the machine the server is running


# First, create the socket
# We will always use these parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #this is going to be our shocket

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT)) #es una tupla mismo parametro con dos variables
#si no hay un server, aquí daria error

# Send data. No strings can be sent, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!")) #we are transfroming that into bytes

# Close the socket
s.close()
