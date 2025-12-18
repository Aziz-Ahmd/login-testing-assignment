from src.login import login

def test_valid_login():
    assert login("admin", "1234") == "Login Successful"

def test_invalid_password():
    assert login("admin", "wrong") == "Login Failed"
