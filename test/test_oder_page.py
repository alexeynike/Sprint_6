import allure
import pytest

from pages.home_page import HomePage
from pages.order_page import OrderPage

@allure.suite("Страница заказа")
class TestOderPage:
    @allure.title('Создание заказа через кнопку "Заказать" в хеддере')
    def test_make_order_from_header_btn(self, browser, create_user_data):
        user = create_user_data('Имя', 'Фамилия','Ул.Тестовая', '88005553535')
        home_page = HomePage(browser)
        home_page.open()
        home_page.open_order_page_by_header_btn()
        order_page = OrderPage(browser)
        order_page.fill_user_data_form(user)
        order_page.fill_order_data_form()
        order_page.click_order_confirm_btn()
        order_page.assert_order_message('Заказ оформлен')

    @allure.title('Переход на главную страницу для проверки лого "Самокат"')
    def test_move_to_homepage_click_to_scooter_logo(self, browser):
        order_page = OrderPage(browser)
        order_page.open()
        home_page = order_page.click_to_logo_scooter()
        home_page.assert_home_page_is_opened()

    @allure.title('Переход на dzen для проверки лого "Яндекс"')
    def test_move_to_dzen_click_to_yandex_logo(self, browser):
        order_page = OrderPage(browser)
        order_page.open()
        order_page.click_to_logo_yandex()
        order_page.switch_tab()
        order_page.assert_url_have('dzen.ru')
