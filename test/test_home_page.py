import allure
import pytest

from pages.home_page import HomePage
from data.accordion_data import accordions_data

class TestHomePage:
    @allure.step('Проверка функционала аккордионов')
    @pytest.mark.parametrize("index, title, expected_text", accordions_data)
    def test_check_question_about_necessary(self, browser, index, title, expected_text):
        home_page = HomePage(browser)
        home_page.open()
        home_page._scroll(y=3500)
        home_page.open_accordion(title)
        assert home_page.get_accordion_text(index=index) == expected_text
