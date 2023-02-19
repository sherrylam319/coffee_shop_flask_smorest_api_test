

def test_user_registration(client):
    response = client.post("/register", json={
        "username": "sherry",
        "password": "1234"
    })

    assert response.status_code == 201
    assert response.json == {"message": "User created successfully."}



def test_user_login_valid(client, registered_user_info):

    response = client.post("/login", json={
        "username": "sherry",
        "password": "1234"
    })
    assert response.json["access_token"]
    assert response.json["refresh_token"]


def test_user_login_invalid(client, registered_user_info):

    response = client.post("/login", json={
        "username": "sherry",
        "password": "0000"
    })

    assert response.json["message"] == "Invalid credentials."
    assert response.status_code == 401


def test_token_refresh(client, created_user_jwt):
    client.post("/login", json={
        "username": "sherry",
        "password": "1234"
    })

    response = client.post(
        "/refresh",
        headers={"Authorization": f"Bearer {created_user_jwt[1]}"})

    assert response.json["access_token"]



def test_user_logout(client, created_user_jwt):
    client.post("/login", json={
        "username": "sherry",
        "password": "1234"
    })
    response = client.post(
        "/logout",
        headers={"Authorization": f"Bearer {created_user_jwt[0]}"})

    assert response.json["message"] == "Successfully logged out."
    assert response.status_code == 200


def test_get_user_info(client):
    client.post("/register", json={
        "username": "sherry",
        "password": "1234"
    })

    response = client.get("/user/1")
    assert response.json == {"id": 1, "username": "sherry"}

def test_delete_user(client, registered_user_info):
    response = client.delete(f"/user/1")

    assert response.json == {"message": "User deleted."}
    assert response.status_code == 200








