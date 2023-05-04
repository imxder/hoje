import sqlite3

from user.user_dao import UserDao

class Database:
    def __init__(self):
        self.__connection = sqlite3.connect('users.db')
        self.__user_dao = UserDao(self.__connection)

    def get_user_dao(self):
        return self.__user_dao

    def close(self):
        self.__connection.close()