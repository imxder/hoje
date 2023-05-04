class User:
    def __init__(self, user_id, name, email):
        self.__id = user_id
        self.__name = name
        self.__email = email

    def get_id(self):
        return self.__id

    def set_id(self, user_id):
        self.__id = user_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email