import pytest


@pytest.fixture()
def create_store_id(client):
    store_list = []
    store_1 = client.post(
        "/store",
        json={"location": "fanling",
              "name": "store_1"},
    )
    store_2 = client.post(
        "/store",
        json={"location": "Kowloon",
              "name": "store_2"},
    )

    store_list.append(store_1.json["id"])
    store_list.append(store_2.json["id"])

    return store_list




@pytest.fixture()
def created_product_id(client, create_store_id):
    response = client.post(
        "/product",
        json={"name": "coffee",
              "price": 15.5,
              "store_id": create_store_id[0]}
    )

    return response.json["id"]


@pytest.fixture()
def registered_user_info(client):
    username = "sherry"
    password = "1234"

    client.post("/register", json={
        "username": "sherry",
        "password": "1234"
    })
    return username, password


@pytest.fixture()
def created_user_jwt(client, registered_user_info):

    response = client.post("/login", json={
        "username": "sherry",
        "password": "1234"
    })
    return response.json["access_token"], response.json["refresh_token"]
