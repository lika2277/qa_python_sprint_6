from selenium.webdriver.common.by import By
from pages.base import PageBase

class PageAccordion(PageBase):
    def __init__(self, driver, headings = 0, panels = 0):
        super().__init__(driver)
        self.headings = headings
        self.panels = panels

    def click_heading(self, index):
        if index < 0 or index >= self.headings:
            raise IndexError
        locator = [By.ID, 'accordion__heading-' + str(index)]
        self.is_visible(locator)
        self.click(locator)

    def is_panel_visible(self, index):
        if index < 0 or index >= self.panels:
            raise IndexError
        return self.is_visible([By.ID, 'accordion__panel-' + str(index)])