from src.core.managers.user_manager import UserManager


class UserService:

    @staticmethod
    def create_user(user: dict, session):
        return UserManager.create_user(input_data=user, session=session)

