from selenium.webdriver.common.by import By
from pages.base import PageBase
from pages.header import PageHeader
from pages.accordion import PageAccordion

class PageMain(PageBase):
    # Cookies Button
    locator_cookie = [By.ID, 'rcc-confirm-button']
    # Кнопка заказать (вверху страницы)
    locator_button_order_top = [By.CSS_SELECTOR, 'div[class^="Header_Nav"] > button[class^="Button_Button"]']
    # Кнопка заказать (внизу страницы)
    locator_button_order_bottom = [By.CSS_SELECTOR, 'div[class^="Home_FinishButton"] > button[class^="Button_Button"]']

    def __init__(self, driver):
        super().__init__(driver)
        self.header = PageHeader(driver)

    def open(self, url = 'https://qa-scooter.praktikum-services.ru/'):
        self.driver.get(url)

    def accept_cookies(self):
        self.is_visible(self.locator_cookie)
        self.click(self.locator_cookie)

    def click_order_button_top(self):
        self.is_visible(self.locator_button_order_top)
        self.click(self.locator_button_order_top)

    def click_order_button_bottom(self):
        self.is_visible(self.locator_button_order_bottom)
        self.click(self.locator_button_order_bottom)

    def get_accordion(self, headings_count = 0, panels_count = 0):
        return PageAccordion(self.driver, headings_count, panels_count)