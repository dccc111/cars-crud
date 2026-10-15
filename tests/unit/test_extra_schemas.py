"""Additional unit tests written to practise the workload's 'write your own test' step."""

import pytest
from pydantic import ValidationError

from app.schemas import CarInput

pytestmark = pytest.mark.unit


def test_make_model_and_color_are_trimmed_individually():
    car = CarInput(make="  Audi ", model=" A4 ", year=2020, color="  Black ")
    assert (car.make, car.model, car.color) == ("Audi", "A4", "Black")


def test_color_defaults_to_empty_string_when_omitted():
    assert CarInput(make="Audi", model="A4", year=2020).color == ""


def test_boolean_year_is_rejected():
    with pytest.raises(ValidationError):
        CarInput(make="Audi", model="A4", year=True)


@pytest.mark.parametrize("year", [1886, 2100])
def test_year_lower_and_upper_boundaries_are_allowed(year):
    assert CarInput(make="Audi", model="A4", year=year).year == year
