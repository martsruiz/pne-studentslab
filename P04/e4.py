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
    method, path, _ = req_line.split(' ')

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)

    # This new contents are written in HTML language
    if path.endswith( "G") :
        body = """
        <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>GUANINE</title>
      </head>
      <body style="background-color: lightblue;">
        <h1>GUANINE</h1>
        <p>Letter:G</p>
        <p>Chemical formula: C5H5N0</p>
        <a href="https://en.wikipedia.org/wiki/Guanine">More info</a>
    
      </body>
    </html>
        """
    elif path.endswith( "T") :
        body = """
        <!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>THYMINE</title>
  </head>
  <body style="background-color: lightgreen;">
    <h1>THYMINE</h1>
    <p>Letter:T</p>
    <p>Chemical formula: C4H6N202</p>
    <a href="https://en.wikipedia.org/wiki/Thymine">More info</a>

  </body>
</html>"""
    elif path.endswith("A"):
        body = """
            <!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>ADENINE</title>
  </head>
  <body style="background-color: lightgreen;">
    <h1>ADENINE</h1>
    <p>Letter:A</p>
    <p>Chemical formula: C5H5N5 </p>
    <a href="https://en.wikipedia.org/wiki/Adenine">More info</a>

  </body>
</html>
    """

    elif path.endswith("C"):
        body = """
        <!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>CYTOSINE</title>
  </head>
  <body style="background-color: yellow;">
    <h1>CYTOSINE</h1>
    <p>Letter:C</p>
    <p>Chemical formula: C4H5N30</p>
    <a href="https://en.wikipedia.org/wiki/Cytosine">More info</a>

  </body>
</html>"""


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