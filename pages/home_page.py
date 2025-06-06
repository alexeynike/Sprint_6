import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.order_page import OrderPage


class HomePageLocators:
    MAIN_TEXT = (By.XPATH, "//div[contains(@class, 'Home_Header')]")
    ACCORDION_ITEM = (By.XPATH, "//div[@class = 'accordion__button']")
    ACCORDION_TEXT = (By.XPATH, "//div[@class = 'accordion__panel']/p")
    HEADER_ORDER_BTN = (By.XPATH, "//div[contains (@class, 'Header_Nav')]/button[contains (@class, 'Button_Button')]")
    PAGE_ORDER_BTN = (By.XPATH, "//div[contains (@class, 'Home_FinishButton')]/button")

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators()

    def open(self):
        self._open_url()

    @allure.step('Открыть аккордион {name}')
    def open_accordion(self, name):
        accordions = self.driver.find_elements(*HomePageLocators.ACCORDION_ITEM)
        for accordion in accordions:
            if accordion.text == name:
                accordion.click()
                break

        else:
            ValueError(f"Аккордион с именем: {name} не найден")

    @allure.step('Получить текст аккордиона {index}')
    def get_accordion_text(self, index):
        return self._find_elements(*self.locator.ACCORDION_TEXT)[index].text

    @allure.step('Клик по кнопке "Заказать" в хеддере')
    def open_order_page_by_header_btn(self):
        self._click_element(*self.locator.HEADER_ORDER_BTN)
        return OrderPage(self.driver)

    @allure.step('Проверка нахождения пользователя на главной странице')
    def assert_home_page_is_opened(self):
        assert 'Самокат' in self._find_element(*self.locator.MAIN_TEXT).text
