from http.server import BaseHTTPRequestHandler
import json
from application.user_serviceImpl import UserServiceImpl

class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _parse_post_data(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        return json.loads(post_data.decode())

    def do_GET(self):
        if self.path == '/users':
            self._set_headers()
            users = UserServiceImpl().get_users()
            self.wfile.write(json.dumps(users).encode())

        elif self.path.startswith('/users/'):
            user_id = self.path.split('/')[-1]
            user = UserServiceImpl().get_user_by_id(user_id)
            if user:
                self._set_headers()
                self.wfile.write(json.dumps(user).encode())
            else:
                self._set_headers(status_code=404)
                self.wfile.write(b'User not found')

