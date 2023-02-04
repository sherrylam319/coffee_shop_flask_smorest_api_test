
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


def test_create_product(client, created_store_id):
    response = client.post("/product", json={
        "name": "coffee",
        "price": 15.5,
        "store_id": created_store_id}
    )

    assert response.status_code == 200
    assert response.json["id"] == 1
    assert response.json["name"] == "coffee"
    assert response.json["price"] == 15.5
    assert response.json["store"] == {'id': 1, 'location': 'fanling', 'name': 'store_1'}


def test_delete_product(client, created_product_id):

    response = client.delete(f"/product/{created_product_id}")
    assert response.json["message"] == "Product deleted"


def test_put_product(client, created_product_id, created_store_id_2):

    response = client.put(f"/product/{created_product_id}",
                          json={"name": "latte",
                                "price": 13.3,
                                "store_id": created_store_id_2
                                })

    assert response.status_code == 200
    assert response.json["name"] == "latte"
    assert response.json["price"] == "13.3"
    assert response.json["store_id"] == "2"




