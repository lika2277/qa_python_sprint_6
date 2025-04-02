from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class PageBase:
    def __init__(self, driver: WebDriver, timeout = 5):
        self.driver = driver
        self.timeout = timeout

    def find(self, locator):
        return self.driver.find_element(*locator)

    def is_visible(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of_element_located(locator))
        return True

    def send_keys(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    def select(self, locator, index = 0):
       self.driver.find_elements(*locator)[index].click()

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def scroll(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find(locator))
