"""Additional API tests written to practise the workload's 'write your own test' step."""

import pytest

pytestmark = pytest.mark.api


def test_created_car_can_be_retrieved_by_location(client, car_payload):
    created = client.post("/api/cars", json=car_payload).json()
    response = client.get(f"/api/cars/{created['id']}")
    assert response.status_code == 200
    assert response.json() == created


def test_list_returns_newest_first(client, car_payload):
    first = client.post("/api/cars", json=car_payload).json()
    second = client.post(
        "/api/cars",
        json={**car_payload, "make": "Honda", "model": "Civic"},
    ).json()
    ids = [car["id"] for car in client.get("/api/cars").json()]
    assert ids == [second["id"], first["id"]]
