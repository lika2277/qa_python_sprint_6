import allure
from selenium.webdriver.common.by import By
from pages.forms import PageFormCustomer, PageFormScooter, PageFormConfirm
from pages.page import Page

class PageOrder(Page):
    # Cookies Button
    locator_cookie = [By.ID, 'rcc-confirm-button']
    # Форма заказа
    locator_form = [By.CSS_SELECTOR, 'div[class^="Order_Form"]']
    # Форма подтверждения заказа
    locator_result = [By.CSS_SELECTOR, 'div[class^="Order_Modal"]']

    def __init__(self, driver):
        super().__init__(driver)
        self.forms = {
            'customer': PageFormCustomer(driver),
            'scooter': PageFormScooter(driver),
            'confirm': PageFormConfirm(driver)
        }

    @allure.step('Открыть страницу')
    def open(self, url = 'https://qa-scooter.praktikum-services.ru/order'):
        self.driver.get(url)

    @allure.step('Принять cookie')
    def accept_cookies(self):
        self.is_visible(self.locator_cookie)
        self.click(self.locator_cookie)

    def is_visible_form(self):
        return self.is_visible(self.locator_form)

    def submit(self, name, data = None):
        form = self.forms.get(name)
        if form and data:
            form.submit(data)
        elif form:
            form.submit()

    def is_visible_result(self):
        return self.is_visible(self.locator_result)