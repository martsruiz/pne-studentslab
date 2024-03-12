import socket
import random
class Number_Guesser():
    def __init__(self):

        # Configure the Server's IP and PORT
        PORT = 12345
        IP = "127.0.0.1"  # "192.168.1.39" "212.128.255.90" # it depends on the machine the server is running
        MAX_OPEN_REQUESTS = 5



        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print("GUESSER NUMBER configured!")

        try:
            serversocket.bind((IP, PORT))
            # become a server socket
            # MAX_OPEN_REQUESTS connect requests before refusing outside connections
            serversocket.listen(MAX_OPEN_REQUESTS)
            n = random.randint(1, 100)
            print(n)
            self.n = n
            while True:
                # accept connections from outside
                print("Waiting for connections at {}, {} ".format(IP, PORT))
                (clientsocket, address) = serversocket.accept()


                # Read the message from the client, if any
                msg = clientsocket.recv(2048).decode("utf-8")

                message = self.guess(int(msg))

                # Send the message
                send_bytes = str(message).encode("utf-8")

                # We must write bytes, not a string
                clientsocket.send(send_bytes)
                clientsocket.close()

        except socket.error:
            print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

        except KeyboardInterrupt:
            print("Server stopped by the user")
            serversocket.close()


    def guess(self, number):

        rounds = 0
        number_attempts = []

        if self.n == number:
            answer = f" You won after {rounds} attempts"
        elif self.n > number:
            answer = "Higher"

            number_attempts.append(number)
        elif self.n < number:
            answer = "Lower"
            number_attempts.append(number)
        rounds += 1

        print(number_attempts)

        return answer

c = Number_Guesser()