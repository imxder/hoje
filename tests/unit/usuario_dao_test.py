import unittest
from unittest.mock import Mock, patch
from ...src.user import UserDao
from ...src.user import User

class TestUserDao(unittest.TestCase):

    def setUp(self):
        
        self.connection = Mock()
        self.user_dao = UserDao(self.connection)

    def test_save_user(self):
        
        user = User("1", "John Doe", "john.doe@example.com")
       
        mock_cursor = Mock()
        mock_execute = Mock()
        mock_cursor.execute = mock_execute
        self.connection.cursor.return_value = mock_cursor
        # Call the save_user method
        self.user_dao.save_user(user)
        # Assert that the execute method was called with the correct SQL and parameters
        mock_execute.assert_called_once_with(
            "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
            (user.get_id(), user.get_name(), user.get_email())
        )
        # Assert that the connection.commit method was called
        self.connection.commit.assert_called_once()

    def test_get_user_by_id(self):
        # Set up a mock cursor object and execute method
        mock_cursor = Mock()
        mock_execute = Mock()
        mock_fetchone = Mock()
        mock_cursor.execute = mock_execute
        mock_cursor.fetchone = mock_fetchone
        self.connection.cursor.return_value = mock_cursor
        # Call the get_user_by_id method
        user = self.user_dao.get_user_by_id("1")
        # Assert that the execute method was called with the correct SQL and parameters
        mock_execute.assert_called_once_with(
            "SELECT id, name, email FROM users WHERE id = ?",
            ("1",)
        )
        # Assert that the fetchone method was called
        mock_fetchone.assert_called_once()
        # Assert that the User object was returned
        self.assertIsInstance(user, User)

    def test_get_all_users(self):
        # Set up a mock cursor object and execute method
        mock_cursor = Mock()
        mock_execute = Mock()
        mock_fetchall = Mock()
        mock_cursor.execute = mock_execute
        mock_cursor.fetchall = mock_fetchall
        self.connection.cursor.return_value = mock_cursor
        # Call the get_all_users method
        users = self.user_dao.get_all_users()
        # Assert that the execute method was called with the correct SQL
        mock_execute.assert_called_once_with("SELECT id, name, email FROM users")
        # Assert that the fetchall method was called
        mock_fetchall.assert_called_once()
        # Assert that the correct number of User objects were returned
        self.assertEqual(len(users), len(mock_fetchall.return_value))
        for user in users:
            self.assertIsInstance(user, User)
