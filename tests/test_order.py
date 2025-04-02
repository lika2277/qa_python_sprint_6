import allure
from pages.main import PageMain
from pages.order import PageOrder

class TestOrder:
    @allure.title('Проверка кнопки "Заказать"')
    @staticmethod
    def test_order_button_top(browser):
        main = PageMain(browser)
        main.open()
        main.accept_cookies()
        main.click_order_button_top()
        assert PageOrder(browser).is_visible_form()

    @allure.title('Проверка кнопки "Заказать"')
    @staticmethod
    def test_order_button_bottom(browser):
        main = PageMain(browser)
        main.open()
        main.accept_cookies()
        main.click_order_button_bottom()
        assert PageOrder(browser).is_visible_form()

    @allure.title('Проверка формы заказа')
    @staticmethod
    def test_order_form(browser, input_data):
        order = PageOrder(browser)
        order.open()
        order.accept_cookies()
        order.submit_form_customer(input_data[0])
        order.submit_form_scooter(input_data[1])
        order.submit_form_confirm()
        assert order.is_visible_result()

    @allure.title('Проверка работы ссылки в шапке проекта')
    @staticmethod
    def test_logo_scooter(browser):
        order = PageOrder(browser)
        order.open()
        order.accept_cookies()
        order.click_logo_scooter()
        assert order.get_current_url() == 'https://qa-scooter.praktikum-services.ru/'