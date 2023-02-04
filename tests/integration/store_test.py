
def test_get_store(client, created_store_id):
    response = client.get(
        f"/store/{created_store_id}"
    )
    assert response.json == {"id": 1, "location": "fanling", "name": "store_1", "product": {}}
    assert response.status_code == 200


def test_delete_store(client, created_store_id):

    response = client.delete(
        f"/store/{created_store_id}"
    )
    assert response.status_code == 200
    assert response.json == {"message": "Store deleted"}


def test_post_store(client):

    response = client.post(
        "/store",
        json={"location": "fanling"
            , "name": "store_1"}
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









