from urllib.parse import parse_qs, urlparse
url_path = urlparse(self.path)
path = url_path.path # we get it from here
print(path)
arguments = parse_qs(url_path.query)
print(arguments)