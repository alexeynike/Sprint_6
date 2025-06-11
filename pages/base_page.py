import random
from typing import List

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import ChromiumDriver
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    def __init__(self, driver):
        self.driver = driver
        self._driver: ChromiumDriver = driver
        self.wait = WebDriverWait(self._driver, 10)

    @allure.step('Открыть страницу {endpoint}')
    def _open_url(self, endpoint = ''):
        self._driver.get(self.BASE_URL + endpoint)

    @allure.step('Проскролить страницу {x}, {y}')
    def _scroll(self, x: int = 0, y: int = 0):
        return self._driver.execute_script(f"window.scroll({x}, {y})")

    def _find_element(self, by: str, locator: str) -> WebElement:
        return self._driver.find_element(by, locator)

    def _find_elements(self, by: str, locator: str) -> List[WebElement]:
        return self._driver.find_elements(by, locator)

    @allure.step('Нажать на {locator}')
    def _click_element(self, by, locator):
        self.wait.until(EC.element_to_be_clickable((by, locator)))
        self._driver.find_element(by, locator).click()

    @allure.step('Заполнить поле {locator}')
    def _send_keys(self, by, locator, text):
        self.wait.until(EC.presence_of_element_located((by, locator)))
        self._find_element(by, locator).clear()
        self._find_element(by, locator).send_keys(text)

    @allure.step('Переключить вкладку')
    def switch_tab(self):
        windows = self._driver.window_handles
        self._driver.switch_to.window(windows[-1])

    @allure.step('Проверка что URL содержит {url}')
    def assert_url_have(self, url):
        self.wait.until(EC.url_contains(url))
