from http.server import HTTPServer
from routes.user_routes import MyServer
from infraestructure.orm import Database

def run(server_class=HTTPServer, handler_class=MyServer, port=8000):

    db = Database()
    handler_class.db = db

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running at localhost:{port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()