#!/usr/bin/env python3

import http.server
import mimetypes
from urllib.parse import urlparse, unquote
from pathlib import Path

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path[1:])
        root = Path("out")
        path = root / Path(unquote(url.path))
        if path.is_dir():
            path = path.joinpath("index.html")
        if path.suffix == "":
            path = path.with_suffix(".html")
        if not path.exists():
            self.send_response(400)
            self.wfile.write("Not Found")
            return
        with path.open("rb") as f:
            self.send_response(200)
            self.send_header("Content-type", mimetypes.guess_type(path)[0])
            self.end_headers()
            self.wfile.write(f.read())

def main(args: list[str]) -> int:
    server_address = ('', 9060)
    httpd = http.server.HTTPServer(server_address, RequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        pass
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
