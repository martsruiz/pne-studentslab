
import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import http.client
import json


import jinja2 as j
from Seq1 import Seq


# Define the Server's port
PORT = 8080
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
def connect_server(ENDPOINT):
    SERVER = "rest.ensembl.org"

    PARAMETERS = "?content-type=application/json"

    url = ENDPOINT + PARAMETERS
    print()
    print(f"Server: {SERVER}")
    print(f"URL: {url}")

    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", url)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")

    # -- Create a variable with the data,
    # -- form the JSON received
    person = json.loads(data1) # aqui convertimos el string en json

    return person


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
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
        contents = ""
        if path == "/":
            contents = Path("index.html").read_text()

        elif path == "/listSpecies":
            ENDPOINT = "/info/species"
            total_list = connect_server(ENDPOINT)
            total_species = len(total_list["species"])

            if arguments == {}:
                limit = int(total_species)
            else:
                limit = arguments["limit"][0]

            list_species = []
            for specie in total_list["species"][:int(limit)]:
                n = (specie["common_name"]).capitalize()
                list_species.append(n)
            contents = read_html_file("list-species.html").render(
                context={"limit_number": limit, "total_number": total_species, "list_species": list_species})

        elif path == "/karyotype":
            specie = arguments["species"][0].replace("+","").lower().strip()
            print(specie)

            ENDPOINT = "/info/assembly/" + str(specie)
            karyotype = connect_server(ENDPOINT)
            karyotype_list = (karyotype["karyotype"])
            contents = read_html_file("karyotype.html").render(
                context={"names_karyotype": karyotype_list})

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

