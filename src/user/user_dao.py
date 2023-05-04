from user.user import User

class UserDao:
    def __init__(self, connection):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__create_table()

    def save_user(self, user):
        self.__cursor.execute(
            "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
            (user.get_id(), user.get_name(), user.get_email())
        )
        self.__connection.commit()

    def get_user_by_id(self, user_id):
        self.__cursor.execute(
            "SELECT id, name, email FROM users WHERE id = ?",
            (user_id,)
        )
        row = self.__cursor.fetchone()
        return User(*row) if row else None

    def get_all_users(self):
        self.__cursor.execute("SELECT id, name, email FROM users")
        rows = self.__cursor.fetchall()
        return [User(*row) for row in rows]

    def __create_table(self):
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"
        )