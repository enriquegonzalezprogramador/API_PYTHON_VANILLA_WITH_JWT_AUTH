import jwt
from datetime import datetime, timedelta

def generate_token(payload, expiration_time='1h'):
    secret_key = 'miclavesecreta'
    # Calcula el tiempo de expiración basado en el tiempo actual y el tiempo de expiración proporcionado
    expiration_delta = timedelta(seconds=3600)  # Por defecto, 1 hora de expiración
    if expiration_time.endswith('h'):
        hours = int(expiration_time[:-1])
        expiration_delta = timedelta(hours=hours)
    elif expiration_time.endswith('m'):
        minutes = int(expiration_time[:-1])
        expiration_delta = timedelta(minutes=minutes)
    expiration_time = datetime.utcnow() + expiration_delta

    # Agrega el tiempo de expiración al payload
    payload['exp'] = expiration_time

    # Codifica el token con el payload y la clave secreta
    token = jwt.encode(payload, secret_key, algorithm='HS256')

    return token

# Función para verificar y decodificar un token JWT
def verify_token(token):
    secret_key = 'miclavesecreta'
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        # El token ha expirado
        return None
    except jwt.InvalidTokenError:
        # El token es inválido
        return None
