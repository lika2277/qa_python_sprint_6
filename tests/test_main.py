import allure
from tests.conftest import browser
from pages.main import PageMain

class TestMain:
    @allure.title('Проверка работы аккардиона')
    @staticmethod
    def test_accordion(browser):
        main = PageMain(browser)
        main.open()
        main.accept_cookies()

        for i in range(main.get_accordion_items_count()):
            main.click_accordion_heading(i)
            assert main.is_accordion_panel_visible(i)

    @allure.title('Проверка работы ссылки в шапке проекта')
    @staticmethod
    def test_logo_yandex(browser):
        url = 'https://dzen.ru/?yredirect=true'
        main = PageMain(browser)
        main.open()
        main.click_logo_yandex()
        main.check_redirect(url)
        assert main.get_current_url() == url
