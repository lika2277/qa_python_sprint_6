from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class AccordionItem:
    def __init__ (self, driver, locator):
        self.driver = driver
        self.locator = locator

    def click(self):
        elem = self.driver.find_element(*self.locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(elem))
        elem.click()




