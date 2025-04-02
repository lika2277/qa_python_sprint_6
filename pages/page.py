import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base import PageBase

class Page(PageBase):
    # Cookies Button
    locator_cookie = [By.ID, 'rcc-confirm-button']
    # Логотип «Самоката»
    locator_link_logo_scooter = [By.CSS_SELECTOR, 'div[class^="Header_Logo"] > a[class^="Header_LogoScooter"]']
    # Логотип "Яндекса"
    locator_link_logo_yandex = [By.CSS_SELECTOR, 'div[class^="Header_Logo"] > a[class^="Header_LogoYandex"]']

    @allure.step('Открыть страницу')
    def open(self, url = 'https://qa-scooter.praktikum-services.ru/'):
        self.driver.get(url)

    @allure.step('Принять cookie')
    def accept_cookies(self):
        self.is_visible(self.locator_cookie)
        self.click(self.locator_cookie)

    @allure.step('Клик по логотипа "Самокат"')
    def click_logo_scooter(self):
        self.is_visible(self.locator_link_logo_scooter)
        self.click(self.locator_link_logo_scooter)

    @allure.step('Клик по логотипа "Яндекс"')
    def click_logo_yandex(self):
        self.is_visible(self.locator_link_logo_yandex)
        self.click(self.locator_link_logo_yandex)

    def check_redirect(self, url):
        original_window = self.get_current_window()
        self.is_number_of_windows(2)

        for window in self.get_windows():
            if window != original_window:
                self.switch_to_window(window)
                break

        self.is_url(url)