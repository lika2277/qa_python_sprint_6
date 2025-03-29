from pages.element import Element

class Link(Element):
    def click(self):
        self.driver.find_element(*self.locator).click()