from abc import ABC, abstractmethod
from domain.user import User

class UserRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, user_id):
        pass

    @abstractmethod
    def create(self, user_data):
        pass

    @abstractmethod
    def update(self, user_id, user_data):
        pass

    @abstractmethod
    def delete(self, user_id):
        pass

    @abstractmethod
    def get_user_by_username(self, username):
        pass
