from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib3

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        pass
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        #url="https://github.com/Dilduz67/django_homework/blob/develop/contacts.html"
        #http = urllib3.PoolManager()
        #response = http.request('GET', url)
        #w_page = response.data.decode('utf-8')

        with open("contacts.html", "r",encoding="utf-8") as f:
            w_page=f.read()
            self.wfile.write(bytes(w_page, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")