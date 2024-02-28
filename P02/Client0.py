import socket
class Client:


    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        a = f"Connection to SERVER at {self.ip}, PORT: {self.port}"
        return a


    def ping(self):
        print("OK")


    def talk (self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data. No strings can be sent, only bytes
        # It necesary to encode the string into bytes
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response





