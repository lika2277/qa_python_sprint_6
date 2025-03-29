from pages.accordion import Accordion
from pages.accordion_item import AccordionItem
from tests.conftest import browser
import locators.accordion_locators as locators
from pages.accordion_panel import AccordionPanel

class TestAccordion:
    @staticmethod
    def test_accordion_item(browser):
        accordion = Accordion([
            AccordionItem(browser, locators.accordion_heading_0),
            AccordionItem(browser, locators.accordion_heading_1),
            AccordionItem(browser, locators.accordion_heading_2),
            AccordionItem(browser, locators.accordion_heading_3),
            AccordionItem(browser, locators.accordion_heading_4),
            AccordionItem(browser, locators.accordion_heading_5),
            AccordionItem(browser, locators.accordion_heading_6),
            AccordionItem(browser, locators.accordion_heading_7)
        ], [
            AccordionPanel(browser, locators.accordion_panel_0),
            AccordionPanel(browser, locators.accordion_panel_1),
            AccordionPanel(browser, locators.accordion_panel_2),
            AccordionPanel(browser, locators.accordion_panel_3),
            AccordionPanel(browser, locators.accordion_panel_4),
            AccordionPanel(browser, locators.accordion_panel_5),
            AccordionPanel(browser, locators.accordion_panel_6),
            AccordionPanel(browser, locators.accordion_panel_7)
        ])

        for i in range(7):
            accordion.click(i)
            assert accordion.is_panel_visible(i)