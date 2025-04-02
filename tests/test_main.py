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