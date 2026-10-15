"""Additional end-to-end test written to practise the 'write your own test' step."""

import re

import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.e2e


def test_create_then_list_shows_the_new_car(page, live_server):
    page.goto(f"{live_server}/cars/new")
    page.get_by_label("Make", exact=True).fill("Mazda")
    page.get_by_label("Model", exact=True).fill("MX-5")
    page.get_by_label("Year", exact=True).fill("2022")
    page.get_by_label("Color", exact=False).fill("Red")
    page.get_by_role("button", name="Create car", exact=True).click()

    expect(page).to_have_url(re.compile(r"/cars/\d+$"))

    page.get_by_role("link", name="Back to cars").click()
    row = page.get_by_role("row").filter(has_text="Mazda")
    expect(row).to_contain_text("MX-5")
