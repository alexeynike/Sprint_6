import pytest
from selenium import webdriver

from data.user_data import UserData


@pytest.fixture
def browser() -> webdriver.Firefox:
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def create_user_data():
    def _create_user_data(name, lastname, address, phone):
        return UserData(name, lastname, address, phone)
    return _create_user_data