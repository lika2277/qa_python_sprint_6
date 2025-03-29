from pages.element import Element

class Button(Element):
    def click(self):
        self.driver.find_element(*self.locator).click()