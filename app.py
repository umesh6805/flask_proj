from app import app

def test_index_redirect():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 302

def test_signup_page():
    client = app.test_client()
    response = client.get("/signup")
    assert response.status_code == 200

def test_signup_success():
    client = app.test_client()
    response = client.post(
        "/signup",
        data={
            "name": "Umesh",
            "email": "umesh@test.com",
            "password": "1234",
            "confirm": "1234",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200

def test_signup_password_mismatch():
    client = app.test_client()
    response = client.post(
        "/signup",
        data={
            "name": "Umesh",
            "email": "umesh@test.com",
            "password": "1234",
            "confirm": "5678",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200