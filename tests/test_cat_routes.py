def test_get_all_cats_with_no_records(client):

    #Act
    response = client.get("/cats")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_cat_succeds(client, one_cat):
    # Act
    response = client.get("/cats/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Morty",
        "color": "orange",
        "personality": "rechargeble"
    }

def test_create_one_cat(client):
    # Act
    response = client.post("/cats", json={
        "name": "Chester",
        "color": "black",
        "personality": "evel"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Chester",
        "color": "black",
        "personality": "evel"
    }
