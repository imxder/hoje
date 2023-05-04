from user.user import User
from user.user_dao import UserDao
from infraestructure.database import Database

def main():
    # Cria uma instância do banco de dados e da classe de DAO
    db = Database()
    user_dao = db.get_user_dao()

    # Cria alguns usuários para testar o DAO
    users = [
        User(1, "John Doe", "johndoe@example.com"),
        User(2, "Jane Doe", "janedoe@example.com"),
        User(3, "Bob Smith", "bobsmith@example.com")
    ]

    # Salva os usuários no banco de dados
    for user in users:
        user_dao.save_user(user)

    # Recupera os usuários do banco de dados e imprime suas informações
    retrieved_users = user_dao.get_all_users()
    for user in retrieved_users:
        print(user.get_id(), user.get_name(), user.get_email())

    # Fecha a conexão com o banco de dados
    db.close()

if __name__ == "__main__":
    main()