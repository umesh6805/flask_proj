from app import app

def test_signup_page():
    client = app.test_client()
    response = client.get("/signup")
    assert response.status_code == 200