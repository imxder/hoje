import pytest
from unittest.mock import Mock, patch
from user_dao import UserDao
from user import User

@pytest.fixture
def mock_connection():
    connection = Mock()
    cursor = Mock()
    connection.cursor.return_value = cursor
    return connection

def test_save_user(mock_connection):
  
    user = User("1", "John Doe", "john.doe@example.com")
  
    user_dao = UserDao(mock_connection)
    user_dao.save_user(user)
    
    mock_connection.cursor.return_value.execute.assert_called_once_with(
        "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
        (user.get_id(), user.get_name(), user.get_email())
    )
   
    mock_connection.commit.assert_called_once()

def test_get_user_by_id(mock_connection):
   
    mock_cursor = Mock()
    mock_execute = Mock()
    mock_fetchone = Mock()
    mock_cursor.execute = mock_execute
    mock_cursor.fetchone = mock_fetchone
    mock_connection.cursor.return_value = mock_cursor
    
    user_dao = UserDao(mock_connection)
    user = user_dao.get_user_by_id("1")
    
    mock_execute.assert_called_once_with(
        "SELECT id, name, email FROM users WHERE id = ?",
        ("1",)
    )
   
    mock_fetchone.assert_called_once()
    assert isinstance(user, User)

def test_get_all_users(mock_connection):
  
    mock_cursor = Mock()
    mock_execute = Mock()
    mock_fetchall = Mock()
    mock_cursor.execute = mock_execute
    mock_cursor.fetchall = mock_fetchall
    mock_connection.cursor.return_value = mock_cursor
 
    user_dao = UserDao(mock_connection)
    users = user_dao.get_all_users()
    
    mock_execute.assert_called_once_with("SELECT id, name, email FROM users")
   
    mock_fetchall.assert_called_once()
 
    assert len(users) == len(mock_fetchall.return_value)
    for user in users:
        assert isinstance(user, User)
