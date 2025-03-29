import locators.order_locators as locators
from selenium.webdriver.common.keys import Keys
from pages.button import Button
from pages.form import Form
from pages.link import Link
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOrderForm:

    @staticmethod
    def test_order_button_top(browser):
        button = Button(browser, locators.order_button_top)
        button.is_visible()
        button.click()
        
        form = Form(browser, locators.order_form)
        assert form.is_visible()

    @staticmethod
    def test_order_button_bottom(browser):
        button = Button(browser, locators.order_button_bottom)
        button.is_visible()
        button.click()

        form = Form(browser, locators.order_form)
        assert form.is_visible()

    @staticmethod
    def test_order(browser, input_data):
        button = Button(browser, locators.order_button_bottom)
        button.is_visible()
        button.click()

        order_form = Form(browser, locators.order_form)
        order_form.is_visible()
        order_form.fill(input_data[0])
        order_form.submit(locators.order_button_next)

        rent_form = Form(browser, locators.order_form)
        rent_form.is_visible()
        rent_form.fill(input_data[1])
        rent_form.submit(locators.order_button_order)

        confirm_form = Form(browser, locators.order_confirm)
        confirm_form.is_visible()
        confirm_form.submit(locators.order_confirm_confirm)

        result_form = Form(browser, locators.order_confirm)
        assert result_form.is_visible()

    @staticmethod
    def test_logo_scooter(browser):
        button = Button(browser, locators.order_button_top)
        button.is_visible()
        button.click()

        form = Form(browser, locators.order_form)
        form.is_visible()

        link = Link(browser, locators.order_link_logo_scooter)
        link.is_visible()
        link.click()

        assert browser.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @staticmethod
    def test_logo_yandex(browser):
        original_window = browser.current_window_handle

        link = Link(browser, locators.order_link_logo_yandex)
        link.is_visible()
        link.click()

        WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(2))

        for window_handle in browser.window_handles:
            if window_handle != original_window:
                browser.switch_to.window(window_handle)
                break

        WebDriverWait(browser, 10).until(EC.url_to_be('https://dzen.ru/?yredirect=true'))

        assert browser.current_url == 'https://dzen.ru/?yredirect=true'