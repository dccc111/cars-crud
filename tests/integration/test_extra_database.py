"""Additional integration tests written to practise the 'write your own test' step."""

import pytest

from app import database
from app.schemas import CarInput

pytestmark = pytest.mark.integration


@pytest.fixture
def db(database_path):
    database.initialize(database_path)
    return database_path


def test_update_changes_only_the_target_car(db, car_payload):
    first = database.create_car(db, CarInput(**car_payload))
    second = database.create_car(db, CarInput(make="Honda", model="Civic", year=2020))

    database.update_car(db, first.id, CarInput(make="Audi", model="A4", year=2021))

    assert database.get_car(db, second.id) == second
    assert database.get_car(db, first.id).make == "Audi"


def test_delete_removes_only_one_car(db, car_payload):
    first = database.create_car(db, CarInput(**car_payload))
    second = database.create_car(db, CarInput(**car_payload))

    assert database.delete_car(db, first.id) is True
    assert database.get_car(db, first.id) is None
    assert database.get_car(db, second.id) == second
