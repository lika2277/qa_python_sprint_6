from selenium.webdriver.common.by import By
from pages.base import PageBase

class PageHeader(PageBase):
    # Логотип «Самоката»
    locator_link_logo_scooter = [By.CSS_SELECTOR, 'div[class^="Header_Logo"] > a[class^="Header_LogoScooter"]']
    # Логотип "Яндекса"
    locator_link_logo_yandex = [By.CSS_SELECTOR, 'div[class^="Header_Logo"] > a[class^="Header_LogoYandex"]']

    def click_logo_scooter(self):
        self.is_visible(self.locator_link_logo_scooter)
        self.click(self.locator_link_logo_scooter)

    def click_logo_yandex(self):
        self.is_visible(self.locator_link_logo_yandex)
        self.click(self.locator_link_logo_yandex)
