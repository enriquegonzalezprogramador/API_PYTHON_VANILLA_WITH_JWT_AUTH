from application.user_serviceImpl import UserServiceImpl
from utils.jwt import generate_token, verify_token
from utils.bcrypt import verify_password, hash_password
import json
import cgi
from http.server import BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _parse_request_data(self):
        # Verificar el método de la solicitud para determinar cómo analizar los datos
        if self.command == 'POST' or self.command == 'PUT':
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': self.command}
            )
            request_data = {}
            for field in form.keys():
                request_data[field] = form[field].value
            return request_data
        else:
            # Manejar otros métodos de solicitud aquí si es necesario
            return {} 
    def _authenticate_token(self):
        auth_header = self.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(' ')[1]
            try:
                decoded_token = verify_token(token)
                return decoded_token
            except Exception as e:
                return None
        else:
            return None

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
    
    def do_POST(self):
        if self.path == '/users':
            # Verificar el token JWT antes de permitir el acceso
            decoded_token = self._authenticate_token()
            if decoded_token:
                self._set_headers()
                user_data = self._parse_request_data()
                password = user_data['password'];
                user_data['password'] = hash_password(password)
                print(user_data)
                user = UserServiceImpl().create_user(user_data)
                if user:
                    self._set_headers(status_code=201)
                    self.wfile.write(json.dumps(user).encode())
                else:
                    self._set_headers(status_code=400)
                    self.wfile.write(b'Failed to create user')
            else:
                self._set_headers(status_code=401)
                self.wfile.write(b'Unauthorized')

        elif self.path == '/login':
            data = self._parse_request_data()
            username = data.get('username')
            password = data.get('password')

            userResp = UserServiceImpl().get_user_by_username(username)
            user = json.loads(userResp)

            print(userResp)
            print(user)

            if user:
                if verify_password(password, user['password']):
                    token = generate_token({'username': username})
                    self._set_headers()
                    self.wfile.write(json.dumps({'token': token}).encode())
                else:
                    self._set_headers(status_code=401)
                    self.wfile.write(json.dumps({'message': 'Invalid username or password'}).encode())
            else:
                self._set_headers(status_code=401)
                self.wfile.write(json.dumps({'message': 'Invalid username or password'}).encode())

    def do_PUT(self):
        if self.path.startswith('/users/'):
            user_id = self.path.split('/')[-1]
            user_data = self._parse_request_data()
            success = UserServiceImpl().update_user(user_id, user_data)
            if success:
                self._set_headers(status_code=204)
            else:
                self._set_headers(status_code=404)
                self.wfile.write(b'User not found')

    def do_DELETE(self):
        if self.path.startswith('/users/'):
            user_id = self.path.split('/')[-1]
            success = UserServiceImpl().delete_user(user_id)
            if success:
                self._set_headers(status_code=204)
            else:
                self._set_headers(status_code=404)
                self.wfile.write(b'User not found')

   # def do_POST(self):
        #if self.path == '/users':
            #self._set_headers()
            #user_data = self._parse_request_data()
            #user = UserServiceImpl().create_user(user_data)
            #if user:
             #   self._set_headers(status_code=201)
             #   self.wfile.write(json.dumps(user).encode())
            #else:
              #  self._set_headers(status_code=400)
              #  self.wfile.write(b'Failed to create user')


