class User:
    def __init__(self, user_id: str):
        self.__user_id = user_id

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id
