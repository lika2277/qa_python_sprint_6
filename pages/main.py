import allure
from selenium.webdriver.common.by import By
from pages.accordion import PageAccordion
from pages.page import Page

class PageMain(Page):
    # Кнопка заказать (вверху страницы)
    locator_button_order_top = [By.CSS_SELECTOR, 'div[class^="Header_Nav"] > button[class^="Button_Button"]']
    # Кнопка заказать (внизу страницы)
    locator_button_order_bottom = [By.CSS_SELECTOR, 'div[class^="Home_FinishButton"] > button[class^="Button_Button"]']

    @allure.step('Клик по кнопке "Заказать" в шапке проекта')
    def click_order_button_top(self):
        self.is_visible(self.locator_button_order_top)
        self.click(self.locator_button_order_top)

    @allure.step('Клик по кнопке "Заказать" в нижней части проекта')
    def click_order_button_bottom(self):
        self.is_visible(self.locator_button_order_bottom)
        self.click(self.locator_button_order_bottom)

    def get_accordion(self, headings_count = 0, panels_count = 0):
        return PageAccordion(self.driver, headings_count, panels_count)