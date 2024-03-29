from application.user_service import UserService
from domain.repository.user_repository import UserRepository
from infraestructure.repository.user_repositoryImpl import UserRepositoryImpl

class UserServiceImpl(UserService):
    def __init__(self):
        self.user_repository = UserRepositoryImpl()

    def get_users(self):
        return self.user_repository.get_all()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def create_user(self, user_data):
        return self.user_repository.create(user_data)

    def update_user(self, user_id, user_data):
        return self.user_repository.update(user_id, user_data)

    def delete_user(self, user_id):
        return self.user_repository.delete(user_id)
    
    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)



