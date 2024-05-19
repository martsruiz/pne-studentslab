
import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import http.client
import json

import jinja2 as j
from Seq1 import Seq
import urllib.parse


# Define the Server's port
PORT = 8080


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


def connect_server(ENDPOINT):
    server = "rest.ensembl.org"

    parameters = "?content-type=application/json"

    url = ENDPOINT + parameters
    url1 = server + url
    print(url1)
    print()
    print(f"Server: {server}")
    print(f"URL: {url}")

    conn = http.client.HTTPConnection(server)

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


def info_response(msg):
    s1 = Seq(str(msg))
    length = s1.len()
    base_counts = s1.count()

    total_bases = sum(base_counts.values())

    info_list = [f"The length of the gene is: {length}"]
    for base, count in base_counts.items():
        percentage = round(count / total_bases * 100, 1)
        info_list.append(f"The percentage of {base} is: {count} ({percentage}%)")

    return info_list


def check_specie(specie):
    endpoint = "/info/species"
    total_list = connect_server(endpoint)

    specie = specie.lower()

    for i in total_list["species"]:
        if specie in i["common_name"].lower():
            return True

    return False


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
        try:
            json_arguments = int(arguments["json"][0])
        except KeyError:
            json_arguments = 0



        contents = ""
        if path == "/":
            contents = Path("index.html").read_text()

        elif path == "/listSpecies":
            ENDPOINT = "/info/species"
            total_list = connect_server(ENDPOINT)
            total_species = len(total_list["species"])

            limit = total_species
            if "limit" in arguments:
                try:
                    limit = int(arguments["limit"][0])
                except (ValueError, IndexError):
                    pass

            if int(limit) <= total_species:
                list_species = []
                for specie in total_list["species"][:int(limit)]:
                    n = (specie["common_name"]).capitalize()
                    list_species.append(n)

                info = {"limit_number": limit, "total_number": total_species, "list_species": list_species}

                if json_arguments == 0:
                    contents = read_html_file("list-species.html").render(
                        context=info)
                elif json_arguments == 1:
                    contents = json.dumps(info)

            else:
                contents = Path("error.html").read_text()




        elif path == "/karyotype":

            specie = arguments["species"][0].replace("+", "").strip()
            specie1 = urllib.parse.quote(specie)

            specie_found = check_specie(specie)

            if not specie_found:
                contents = Path("error.html").read_text()
            else:
                endpoint1 = "/info/assembly/" + specie1

                specie_list = connect_server(endpoint1)

                karyotype_list = (specie_list["karyotype"])

                info ={"names_karyotype": karyotype_list}

                if json_arguments == 0:
                    contents = read_html_file("karyotype.html").render(
                    context=info)
                elif json_arguments == 1:
                    contents = json.dumps(info)

        elif path == "/chromosomeLength":

            if "species" not in arguments or "chromo" not in arguments:
                contents = Path("error.html").read_text()

            else:
                specie = arguments["species"][0].replace("+", "").lower().strip()
                number_chromosome = arguments["chromo"][0]
                endpoint1 = "/info/assembly/"
                endpoint_complete = endpoint1 + urllib.parse.quote(specie)
                total_list = connect_server(endpoint_complete)
                specie_found = check_specie(specie)
                if not specie_found:
                    contents = Path("error.html").read_text()
                else:
                    chromosome_length = None
                    for j in total_list["top_level_region"]:
                        if j["name"] == number_chromosome and j["coord_system"] == "chromosome":
                            chromosome_length = j["length"]
                            break

                    if chromosome_length is not None:
                        contents = read_html_file("chromosome_length.html").render(
                            context={"chromosome_length": chromosome_length})

                    else:
                        contents = Path("error.html").read_text()  # Error si el número de cromosoma no es válido

        elif path == "/geneSeq":
            name_gene = arguments["gene"][0].upper()
            print(name_gene)
            try:
                endpoint = "/lookup/symbol/human/" + str(name_gene)
                gene_info = connect_server(endpoint)
                id_number = gene_info["id"]
                endpoint1 = "/sequence/id/" + str(id_number)
                gene_sequence = connect_server(endpoint1)
                sequence = gene_sequence["seq"]
                contents = read_html_file("gene_sequence.html").render(
                    context={"user_gene": name_gene, "sequence": sequence})

            except Exception:
                contents = Path("error.html").read_text()

        elif path == "/geneInfo":
            try:
                name_gene = arguments["gene"][0]
                endpoint = "/lookup/symbol/human/" + str(name_gene)
                gene_info = connect_server(endpoint)
                start = gene_info["start"]
                end = gene_info["end"]
                id_number = gene_info["id"]
                endpoint1 = "/sequence/id/" + str(id_number)
                gene_sequence = connect_server(endpoint1)
                sequence = gene_sequence["seq"]
                length = len(str(sequence))
                chromo_info = gene_sequence["desc"]
                chromo_info= str(chromo_info).split(":")
                chromo_number = chromo_info[2]
                contents = read_html_file("gene_info.html").render(
                    context={"user_gene": name_gene, "start": start, "end": end, "id": id_number, "chromosome" : chromo_number, "length": length})

            except Exception:
                contents = Path("error.html").read_text()

        elif path == "/geneCalc":
            try:
                name_gene = arguments["gene"][0]
                endpoint = "/lookup/symbol/human/" + str(name_gene)
                gene_info = connect_server(endpoint)
                id_number = gene_info["id"]
                endpoint1 = "/sequence/id/" + str(id_number)
                gene_sequence = connect_server(endpoint1)
                sequence = gene_sequence["seq"]
                calc_gene = info_response(str(sequence))
                print(calc_gene)
                length = len(str(sequence))
                contents = read_html_file("calculation_gene.html").render(
                    context={"user_gene": name_gene, "bases": calc_gene, "length": length})

            except Exception:
                contents = Path("error.html").read_text()

        elif path == "/geneList":
            if "chromo" not in arguments or "start" not in arguments or "end" not in arguments:
                contents = Path("error.html").read_text()
            else:
                chromosome = arguments["chromo"][0]
                start = arguments["start"][0]
                end = arguments ["end"][0]
                try:
                    endpoint = f"/phenotype/region/homo_sapiens/{chromosome}:{start}-{end}"
                    gene_info = connect_server(endpoint)
                    list_of_genes = []
                    for gene in gene_info:
                        gene_name = gene["id"]
                        list_of_genes.append(gene_name)

                    dic_info = {"user_chromo": chromosome, "start_position": start, "end_position": end, "list_of_genes": list_of_genes}

                    contents = read_html_file("gene_list.html").render(
                        context=dic_info)
                except Exception:
                    contents = Path("error.html").read_text()



        else:
            contents = Path("error.html").read_text()







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
