from src.login import login

def test_login_flow():
    result = login("Aziz", "12345")
    assert result == "Login Successful"
