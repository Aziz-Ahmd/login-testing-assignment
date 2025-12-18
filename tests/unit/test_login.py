from src.login import login

def test_valid_login():
    assert login("Aziz", "12345") == "Login Successful"

def test_invalid_password():
    assert login("Aziz", "wrong") == "Login Failed"
