from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Element:
    def __init__(self, driver: WebDriver, locator):
        self.driver = driver
        self.locator = locator

    def is_visible(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locator))
        return True