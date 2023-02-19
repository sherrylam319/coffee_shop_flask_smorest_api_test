import json

def test_get_product(client, created_product_id):
    response = client.get(f"/product/{created_product_id}")

    assert response.json == {
        "id": 1,
        "name": "coffee",
        "price": 15.5,
        "store":
            {"id": 1, "location": "fanling", "name": "store_1"}
    }
    assert response.status_code == 200


def test_create_product(client, create_store_id):

    response = client.post("/product", json={
        "name": "coffee",
        "price": 15.5,
        "store_id": create_store_id[0]}
    )

    assert response.status_code == 201
    assert response.json["id"] == 1
    assert response.json["name"] == "coffee"
    assert response.json["price"] == 15.5
    assert response.json["store"] == {'id': 1, 'location': 'fanling', 'name': 'store_1'}


def test_delete_product(client, created_product_id, fresh_jwt):
    response = client.delete(
        f"/product/{created_product_id}",
        headers={"Authorization": f"Bearer {fresh_jwt}"})

    assert response.json["message"] == "Product deleted"


def test_invalid_token_callback(client):
    response = client.delete(
        f"/product/1",
        headers={"Authorization": "Bearer 9i5-39ieplkjfdl45dlkf"}
    )

    assert response.json == {"message": "Signature verification failed.", "error": "invalid_token"}
    assert response.status_code == 401


def test_token_not_fresh(client, jwt_access_token):
    response = client.delete(
        f"/product/1",
        headers={"Authorization": f"Bearer {jwt_access_token}"}
    )
    assert response.json == {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
    assert response.status_code == 401


def test_missing_token(client):
    response = client.delete(
        f"/product/1")

    assert response.json == {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
    assert response.status_code == 401



def test_put_product(client, create_store_id,  created_product_id, jwt_access_token):

    response = client.put(f"/product/{created_product_id}",
                          json={"name": "latte",
                                "price": 13.3,
                                "store_id": create_store_id[1]
                                },
                          headers={"Authorization": f"Bearer {jwt_access_token}"})

    assert response.status_code == 200
    assert response.json["name"] == "latte"
    assert response.json["price"] == 13.3
    assert response.json['store']['id'] == 2






