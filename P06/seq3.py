import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from Seq1 import Seq


# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
def get_response( msg):
    list_seq = ["AATCGGGGA", "GGGTTACG","TAGATACAGT","GGATAGATC", "AGTGATCCC"]
    for i in msg:
        if i.isdigit():
            n = list_seq[int(i)]
        else:
            pass
    return n
def gene_response( msg):
    new_msg = msg.replace("GENE", "").strip()
    sequence = "../sequences/"
    file = sequence + str(new_msg) + ".txt"
    s = Seq()
    with_space = s.read_fasta(file) + "\n"
    return with_space
def comp_response(self, msg):
    seq = msg.replace("COMP", "").strip()
    s = Seq(str(seq))
    complement = s.complement()
    c = complement + "\n"

    return c

def info_response(msg):
    seq = msg.replace("INFO", "").strip()
    s1 = Seq(str(seq))
    length = s1.len()
    base_counts = s1.count()

    for base, count in base_counts.items():
        percentage = round((count / length) * 100,1)
        answer =  (f"{base}: {count} ({percentage} %)\n")

    return answer

def rev_response( msg):
    new_seq = msg.replace("REV", "").strip()
    s = Seq(str(new_seq))
    reverse = s.reverse()
    r = reverse + "\n"
    return r



# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):




    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        print(path)
        print(arguments)
        if path == "/" or path == "/echo":
            contents = Path("html/index.html").read_text()




        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))



# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
