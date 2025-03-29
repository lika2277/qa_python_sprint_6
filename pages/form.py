from pages.element import Element
from pages.button import Button
from pages.order_form_field import OrderFormField
from pages.order_form_select import OrderFormSelect

class Form(Element):
    def fill(self, data):
        for field in data:
            if field.get('type') == 'input':
                element = OrderFormField(self.driver, field.get('locator'))
                element.is_visible()
                element.send_keys(field.get('data'))
            else:
                if field.get('locator'):
                    element = OrderFormField(self.driver, field.get('locator'))
                    element.is_visible()
                    element.click()

                element_item = OrderFormSelect(self.driver, field.get('locator_item'))
                element_item.is_visible()
                element_item.select(field.get('index'))

    def submit(self, locator):
        button = Button(self.driver, locator)
        button.is_visible()
        button.click()
        
        
