from application.user_serviceImpl import UserServiceImpl
from utils.jwt import generate_token, verify_token
import bcrypt
import json
from http.server import BaseHTTPRequestHandler

class JWTServer(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            username = data.get('username')
            password = data.get('password')

            user = UserServiceImpl.get_user_by_username(username)

            if user:
                if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                    token = generate_token({'username': username})
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'token': token}).encode('utf-8'))
                else:
                    self.send_response(401)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'message': 'Invalid username or password'}).encode('utf-8'))
            else:
                self.send_response(401)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Invalid username or password'}).encode('utf-8'))

    def do_BEFORE_REQUEST(self):
        auth_header = self.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(' ')[1]
            try:
                decoded_token = verify_token(token)
                self.request.user = decoded_token
            except Exception as e:
                self.send_response(403)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Unauthorized'}).encode('utf-8'))
        else:
            self.send_response(401)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Unauthorized'}).encode('utf-8'))
