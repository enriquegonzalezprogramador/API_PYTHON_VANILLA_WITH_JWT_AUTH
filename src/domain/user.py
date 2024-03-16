class User:
    def __init__(self, id, username, edad, sexo, pais, password):
        self._id = id
        self._username = username
        self._edad = edad
        self._sexo = sexo
        self._pais = pais
        self._password = password

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        self._sexo = value

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, value):
        self._pais = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'edad': self.edad,
            'sexo': self.sexo,
            'pais': self.pais,
            'password': self.password
        }
