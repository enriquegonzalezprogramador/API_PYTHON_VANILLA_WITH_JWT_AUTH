from domain.user import User
from domain.repository.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_users(self):
        users_json = self.user_repository.get_all()
        users = [User.from_json(user_json) for user_json in users_json]
        return users

    def get_user_by_id(self, user_id):
        user_json = self.user_repository.get_by_id(user_id)
        if user_json:
            return User.from_json(user_json)
        else:
            return None

    def create_user(self, user_data):
        user_id = self.user_repository.create(user_data)
        return user_id

    def update_user(self, user_id, user_data):
        success = self.user_repository.update(user_id, user_data)
        return success

    def delete_user(self, user_id):
        success = self.user_repository.delete(user_id)
        return success


