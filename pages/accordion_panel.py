from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class AccordionPanel:
    def __init__ (self, driver, locator):
        self.driver = driver
        self.locator = locator

    def is_visible(self):
        elem = self.driver.find_element(*self.locator)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of(elem))
        return True



