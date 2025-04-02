import allure
from selenium.webdriver.common.by import By
from pages.page import Page

class PageMain(Page):
    # Кнопка заказать (вверху страницы)
    locator_button_order_top = [By.CSS_SELECTOR, 'div[class^="Header_Nav"] > button[class^="Button_Button"]']
    # Кнопка заказать (внизу страницы)
    locator_button_order_bottom = [By.CSS_SELECTOR, 'div[class^="Home_FinishButton"] > button[class^="Button_Button"]']
    # Количество элементов аккордиона
    accordion_items_count = 7

    @allure.step('Клик по кнопке "Заказать" в шапке проекта')
    def click_order_button_top(self):
        self.is_visible(self.locator_button_order_top)
        self.click(self.locator_button_order_top)

    @allure.step('Клик по кнопке "Заказать" в нижней части проекта')
    def click_order_button_bottom(self):
        self.is_visible(self.locator_button_order_bottom)
        self.click(self.locator_button_order_bottom)

    def get_accordion_items_count(self):
        return self.accordion_items_count

    @allure.step('Клик по разделу аккордиона')
    def click_accordion_heading(self, index):
        if index < 0 or index >= self.accordion_items_count:
            raise IndexError
        locator = [By.ID, 'accordion__heading-' + str(index)]
        self.scroll(locator)
        self.is_visible(locator)
        self.click(locator)

    @allure.step('Проверка отображения скрытого под аккордионом элемента')
    def is_accordion_panel_visible(self, index):
        if index < 0 or index >= self.accordion_items_count:
            raise IndexError
        return self.is_visible([By.ID, 'accordion__panel-' + str(index)])
