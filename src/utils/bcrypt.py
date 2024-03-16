import bcrypt

# Función para encriptar una contraseña
def hash_password(password):
    salt = bcrypt.gensalt()
    # Encriptar la contraseña utilizando la sal
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Función para verificar una contraseña encriptada
def verify_password(password, hashed_password):
    # Verificar la contraseña utilizando el hash almacenado
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))