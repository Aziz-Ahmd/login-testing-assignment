from src.login import login

def test_login_flow():
    result = login("admin", "1234")
    assert result == "Login Successful"
