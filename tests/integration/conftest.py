import pytest

@pytest.fixture()
def created_store_id(client):
    store_1 = client.post(
        "/store",
        json={"location": "fanling",
              "name": "store_1"},
    )


@pytest.fixture()
def created_store_id_2(client):

    store_2 = client.post(
        "/store",
        json={"location": "Kowloon",
              "name": "store_2"},
    )


@pytest.fixture()
def created_product_id(client, created_store_id):
    response = client.post(
        "/product",
        json={"name": "coffee",
              "price": 15.5,
              "store_id": created_store_id}
    )

    return response.json["id"]

