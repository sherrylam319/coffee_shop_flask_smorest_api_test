import json

def test_get_store(client, create_store_id):
    response = client.get(
        f"/store/{create_store_id[0]}"
    )
    assert response.json == {"id": 1, "location": "fanling", "name": "store_1", "product": {}}
    assert response.status_code == 200


def test_delete_store(client, create_store_id):

    response = client.delete(
        f"/store/{create_store_id[0]}"
    )
    assert response.status_code == 200
    assert response.json == {"message": "Store deleted"}


def test_post_store(client):

    response = client.post(
        "/store",
        json={"location": "fanling",
               "name": "store_1"}
    )
    assert response.status_code == 200
    assert response.json["id"] == 1
    assert response.json["location"] == "fanling"
    assert response.json["name"] == "store_1"
    assert response.json["product"] == {}


def test_integrity_error(client):

    client.post(
        "/store",
        json={"location": "fanling", "name": "store_1"}
    )
    response = client.post(
        "/store",
        json={"location": "fanling", "name": "store_1"}
    )

    assert response.status_code == 400
    assert response.json["message"] == "A store with that name already exists."


def test_get_all_store(client):
    client.post(
        "/store",
        json={"location": "fanling", "name": "store_1"}
    )
    client.post(
        "/store",
        json={"location": "kowloon", "name": "store_2"}
    )

    response = client.get(
        "/store"
    )
    assert response.json == [{"id": 1, "location": "fanling", "name": "store_1", "product": {}},
                             {"id": 2, "location": "kowloon", "name": "store_2", "product": {}}]















