import allure
from tests.conftest import browser
from pages.main import PageMain

class TestMain:
    @allure.title('Проверка работы аккардиона')
    @staticmethod
    def test_accordion(browser):
        count = 7
        main = PageMain(browser)
        main.open()
        main.accept_cookies()

        accordion = main.get_accordion(count, count)
        for i in range(count):
            accordion.click_heading(i)
            assert accordion.is_panel_visible(i)