from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        c_len = int(self.headers.get("Content-Length"))
        body = self.rfile.read(c_len)
        print(body.decode())
        self.send_response(200)
        self.send_header("Content_type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        get_answer = 'Hello, World wide web!'
        self.send_response(200)
        self.send_header("Content_type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(get_answer, "utf-8"))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
