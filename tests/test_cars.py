# I am using client from flask documentation


def test_all_cars(client):
    response = client.get("/cars")
    assert response.status_code == 200


def test_car_by_id( client, id:int ):
    response = client.get("/cars")
    assert response.status_code == 200
    