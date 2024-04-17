import socket
import termcolor
from pathlib import Path
import os


# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    slices = req_line.split(" ")
    print(slices)
    method = slices[0]
    resource = slices[1]
    version = slices[2]

    if resource == "/":
        file_name = os.path.join("html", "index.html")
    # This new contents are written in HTML language
        body = Path(file_name).read_text()
    # -- Status line: We respond that everything is ok (200 code)
        status_line = "HTTP/1.1 200 OK\n"

    elif resource == "/info/A":
        file_name = os.path.join("html", "info", "A.html")
    # This new contents are written in HTML language
        body = Path(file_name).read_text()
    # -- Status line: We respond that everything is ok (200 code)
        status_line = "HTTP/1.1 200 OK\n"

    elif resource == "/info/C":
        file_name = os.path.join("html", "info", "C.html")
    # This new contents are written in HTML language
        body = Path(file_name).read_text()
    # -- Status line: We respond that everything is ok (200 code)
        status_line = "HTTP/1.1 200 OK\n"

    elif resource == "/info/T":
        file_name = os.path.join("html", "info", "T.html")
    # This new contents are written in HTML language
        body = Path(file_name).read_text()
    # -- Status line: We respond that everything is ok (200 code)
        status_line = "HTTP/1.1 200 OK\n"

    elif resource == "/info/G":
        file_name = os.path.join ("html", "info", "G.html")
    # This new contents are written in HTML language
        body = Path(file_name).read_text()
    # -- Status line: We respond that everything is ok (200 code)
        status_line = "HTTP/1.1 200 OK\n"

    else:
        file_name = os.path.join ("html", "info", "error.html")
        # This new contents are written in HTML language
        body = Path(file_name).read_text()
        # -- Status line: We respond that everything is ok (200 code)
        status_line = "HTTP/1.1 404 Not found\n"




    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("Green server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()