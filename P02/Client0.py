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


