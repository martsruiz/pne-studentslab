import socket
import termcolor


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

    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # This new contents are written in HTML language
    body = """
    <!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Bases information</title>
  </head>
  <body style="background-color: white;">
    <h1>Bases information</h1>
    <p>Click on the following links to have more information</p>
    <a href="http://localhost:63342/pne-studentslab/P04/html/info/A.html?_ijt=fhf3gtd9vcs2oc9oeuitn62kk&_ij_reload=RELOAD_ON_SAVE">[A]</a>
    <a href="http://localhost:63342/pne-studentslab/P04/html/info/C.html?_ijt=fhf3gtd9vcs2oc9oeuitn62kk&_ij_reload=RELOAD_ON_SAVE">[C]</a>
    <a href="http://localhost:63342/pne-studentslab/P04/html/info/G.html?_ijt=fhf3gtd9vcs2oc9oeuitn62kk&_ij_reload=RELOAD_ON_SAVE">[G]</a>
    <a href="http://localhost:63342/pne-studentslab/P04/html/info/T.html?_ijt=fhf3gtd9vcs2oc9oeuitn62kk&_ij_reload=RELOAD_ON_SAVE">[T]</a>

  </body>
</html>
    """

    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

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