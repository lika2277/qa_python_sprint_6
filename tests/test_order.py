import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
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

        order.is_visible_form()
        order.submit('customer', input_data[0])

        order.is_visible_form()
        order.submit('scooter', input_data[1])

        order.is_visible_form()
        order.submit('confirm')

        assert order.is_visible_result()

    @allure.title('Проверка работы ссылки в шапке проекта')
    @staticmethod
    def test_logo_scooter(browser):
        order = PageOrder(browser)
        order.open()
        order.accept_cookies()
        order.click_logo_scooter()
        assert browser.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка работы ссылки в шапке проекта')
    @staticmethod
    def test_logo_yandex(browser):
        main = PageMain(browser)
        main.open()

        original_window = browser.current_window_handle

        main.click_logo_yandex()

        WebDriverWait(browser, 10).until(expected_conditions.number_of_windows_to_be(2))

        for window_handle in browser.window_handles:
            if window_handle != original_window:
                browser.switch_to.window(window_handle)
                break

        WebDriverWait(browser, 10).until(expected_conditions.url_to_be('https://dzen.ru/?yredirect=true'))

        assert browser.current_url == 'https://dzen.ru/?yredirect=true'