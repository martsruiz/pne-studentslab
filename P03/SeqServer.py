import socket
from Seq1 import Seq
import termcolor
class SeqServer():
    def __init__(self, msg = None):

        # Configure the Server's IP and PORT
        PORT = 12345
        IP = "127.0.0.1"  # "192.168.1.39" "212.128.255.90" # it depends on the machine the server is running
        MAX_OPEN_REQUESTS = 5



        # create an INET, STREAMing socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print("SEQ Server configured!")

        try:
            serversocket.bind((IP, PORT))
            # become a server socket
            # MAX_OPEN_REQUESTS connect requests before refusing outside connections
            serversocket.listen(MAX_OPEN_REQUESTS)

            while True:
                # accept connections from outside
                print("Waiting for connections at {}, {} ".format(IP, PORT))
                (clientsocket, address) = serversocket.accept()


                # Read the message from the client, if any
                msg = clientsocket.recv(2048).decode("utf-8")

                message = self.return_response(str(msg))

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

    def return_response (self, msg):
        if str("PING") in msg:
            return self.ping_response()
        if str("GET") in msg:
            return self.get_response(msg)
        if str("INFO") in msg:
            return self.info_response(msg)
        if str("COMP") in msg:
            return self.comp_response(msg)
        if str("REV") in msg:
            return self.rev_response(msg)
        if str("GENE") in msg:
            return self.gene_response(msg)

    def ping_response(self):
        termcolor.cprint("PING command!", "green")
        print("OK!")
        return "OK!\n"

    def get_response(self, msg):
        list_seq = ["AATCGGGGA", "GGGTTACG","TAGATACAGT","GGATAGATC", "AGTGATCCC"]
        for i in msg:
            if i.isdigit():
                n = list_seq[int(i)]
            else:
                pass
        print(termcolor.colored("GET", "green"))
        print(n)

        return n





    def info_response(self, msg):
        seq = msg.replace("INFO", "").strip()
        print(termcolor.colored("INFO", "green"))
        s1 = Seq(str(seq))
        length = s1.len()
        base_counts = s1.count()

        answer = (f"Sequence: {s1}\nTotal length: {length}\n")


        for base, count in base_counts.items():
            percentage = round((count / length) * 100,1)
            answer +=  (f"{base}: {count} ({percentage} %)\n")
        print (answer)

        return answer




    def comp_response(self, msg):
        seq = msg.replace("COMP", "").strip()
        print(termcolor.colored("COMP", "green"))
        s = Seq(str(seq))
        complement = s.complement()
        print(complement)
        c = complement + "\n"

        return c

    def rev_response(selfsel, msg):
        new_seq = msg.replace("REV", "").strip()
        print(termcolor.colored("REV", "green"))
        s = Seq(str(new_seq))
        reverse = s.reverse()
        print(reverse)
        r = reverse + "\n"
        return r

    def gene_response(self, msg):
        new_msg = msg.replace("GENE", "").strip()
        sequence = "../sequences/"
        file = sequence + str(new_msg) + ".txt"
        print(termcolor.colored("GENE", "green"))
        s = Seq()
        print(s.read_fasta(file))
        with_space = s.read_fasta(file) + "\n"
        return with_space










c = SeqServer()