import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.user_data import UserData


class OrderPageLocators:
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    SUBWAY_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    SUBWAY_STATION = (By.XPATH, "//li[@class = 'select-search__row']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_FORM_BTN = (By.XPATH, "//div[contains(@class, 'Order_NextButton')]/button")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME_INPUT = (By.XPATH, "//div[@class='Dropdown-control']")
    RENT_TIME_SELECT = (By.XPATH, "//div[@class='Dropdown-option']")
    ORDER_BTN = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    ACCEPT_BTN = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = OrderPageLocators()

    def open(self):
        self._open_url('/order')

    @allure.step('Заполнить форму заказа данными пользователя')
    def fill_user_data_form(self, user: UserData):
        self._send_keys(*self.locator.NAME_INPUT, user.name)
        self._send_keys(*self.locator.SURNAME_INPUT, user.last_name)
        self._send_keys(*self.locator.ADDRESS_INPUT, user.address)
        self._click_element(*self.locator.SUBWAY_INPUT)
        self._find_elements(*self.locator.SUBWAY_STATION)[0].click()
        self._send_keys(*self.locator.PHONE_INPUT, user.phone)
        self._click_element(*self.locator.NEXT_FORM_BTN)

    @allure.step('Заполнить форму заказа данными заказа')
    def fill_order_data_form(self):
        self._send_keys(*self.locator.DATE_INPUT, '23.05.2025')
        self._send_keys(*self.locator.DATE_INPUT, Keys.ENTER)
        self._click_element(*self.locator.RENT_TIME_INPUT)
        self._click_element(*self.locator.RENT_TIME_SELECT)
        self._click_element(*self.locator.ORDER_BTN)

    @allure.step('Клик по кнопке "Подтвердить заказ')
    def click_order_confirm_btn(self):
        self._click_element(*self.locator.ACCEPT_BTN)

    @allure.step('Получить подтверждение заказа')
    def assert_order_message(self, text: str):
        assert text in self._find_element(*self.locator.ORDER_SUCCESS_MESSAGE).text

    @allure.step('Клик по лого "Самокат"')
    def click_to_logo_scooter(self):
        from pages.home_page import HomePage
        self._click_element(*self.locator.LOGO_SCOOTER)
        return HomePage(self.driver)

    @allure.step('Клик по лого "Яндекс"')
    def click_to_logo_yandex(self):
       self._click_element(*self.locator.LOGO_YANDEX)
