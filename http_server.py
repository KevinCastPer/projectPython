from http.server import  BaseHTTPRequestHandler, HTTPServer

# Los nombre de clase van en mayuscula. Seria asi
class HttpServer:
    def __init__(self):
        # Asi, estás creado un objeto, pero no lo estas guardando en la instancia de la clase, tiene que poner self
        # aunque estaba bien desde el punto de vista de programa, pero bueno, es mejor tener el objeto asociado por si quieres luego terminar la ejecución del servidor web, etc
        self.server = HTTPServer(('', 8888), myHandler)
        self.server.serve_forever()

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(201)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"hola mundo")
        return

print("Servidor en el puerto 8888")

server = HttpServer()
