class User:
    def __init__(self, id, name, edad, sexo, pais):
        self._id = id
        self._name = name
        self._edad = edad
        self._sexo = sexo
        self._pais = pais

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

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

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'edad': self.edad,
            'sexo': self.sexo,
            'pais': self.pais
        }
