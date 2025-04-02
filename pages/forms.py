import allure
from selenium.webdriver.common.by import By
from pages.base import PageBase

class PageForm(PageBase):
    # Форма заказа
    locator_form = [By.CSS_SELECTOR, 'div[class^="Order_Form"]']

    @allure.step('Проверка отображения формы')
    def is_visible_form(self, locator = None):
        if locator is None:
            locator = self.locator_form
        self.is_visible(locator)

    @allure.step('Заполнение формы')
    def fill_form(self, data, locators):
        for field in data:
            if field.get('type') == 'input':
                locator_input = locators.get(field.get('name'))
                self.is_visible(locator_input)
                self.send_keys(locator_input, field.get('data'))
            elif field.get('type') == 'select':
                locator_select = locators.get(field.get('name'))
                self.is_visible(locator_select)
                self.click(locator_select)

                locator_select_item = locators.get(field.get('item'))
                self.is_visible(locator_select_item)
                self.select(locator_select_item, field.get('index'))
            elif field.get('type') == 'checkbox':
                locator_checkbox = locators.get(field.get('name'))
                self.is_visible(locator_checkbox)
                self.select(locator_checkbox, field.get('index'))

    @allure.step('Отправка формы')
    def submit_form(self, locator):
        self.is_visible(locator)
        self.click(locator)

class PageFormCustomer(PageForm):
    # Поле "Имя"
    locator_field_name = [By.CSS_SELECTOR, 'input[type="text"][placeholder="* Имя"]']
    # Поле "Фамилия"
    locator_field_second_name = [By.CSS_SELECTOR, 'input[type="text"][placeholder="* Фамилия"]']
    # Поле "Адресс"
    locator_field_address = [By.CSS_SELECTOR, 'input[type="text"][placeholder="* Адрес: куда привезти заказ"]']
    # Поле "Станция метро"
    locator_field_metro = [By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]']
    # Поле "Станция метро" - выдабщий список
    # locator_field_metro_select = [By.CLASS_NAME, 'select-search__select']
    # Поле "Станция метро" - элемент выпадающего списка
    locator_field_metro_select_item = [By.CLASS_NAME, 'select-search__row']
    # Поле "Телефон"
    locator_field_phone = [By.CSS_SELECTOR, 'input[type="text"][placeholder="* Телефон: на него позвонит курьер"]']
    # Кнопка "Далее"
    locator_button_next = [By.CSS_SELECTOR, 'div[class^="Order_NextButton"] > button[class^="Button_Button"]']

    def submit(self, data):
        locators = {
            'name': self.locator_field_name,
            'second_name': self.locator_field_second_name,
            'address': self.locator_field_address,
            'metro': self.locator_field_metro,
            'metro_item': self.locator_field_metro_select_item,
            'phone': self.locator_field_phone
        }

        self.is_visible_form()
        self.fill_form(data, locators)
        self.submit_form(self.locator_button_next)

class PageFormScooter(PageForm):
    # Поде "Дата"
    locator_field_date = [By.CSS_SELECTOR, 'input[type="text"][placeholder="* Когда привезти самокат"]']
    # Поле "Срок аренды"
    locator_field_period = [By.CLASS_NAME, 'Dropdown-control']
    # Поле "Срок аренды" - выпадающий список
    # locator_field_period_select = [By.CLASS_NAME, 'Dropdown-menu']
    # Поле "Срок аренды" - элемент выпадающего списка
    locator_field_period_select_option = [By.CLASS_NAME, 'Dropdown-option']
    # Поле "Выбор цвета"
    locator_field_color = [By.CSS_SELECTOR, 'input[type="checkbox"]']
    # Поле "Комментарии"
    locator_field_comment = [By.CSS_SELECTOR, 'input[type="text"][placeholder="Комментарий для курьера"]']
    # Кнопка "Заказать"
    locator_button_order = [By.CSS_SELECTOR, 'div[class^="Order_Buttons"] > button[class^="Button_Button"]:nth-child(2)']

    def submit(self, data):
        locators = {
            'date': self.locator_field_date,
            'period': self.locator_field_period,
            'period_item': self.locator_field_period_select_option,
            'color': self.locator_field_color,
            'comment': self.locator_field_comment
        }

        self.is_visible_form()
        self.fill_form(data, locators)
        self.submit_form(self.locator_button_order)

class PageFormConfirm(PageForm):
    # Форма подтверждения заказа
    locator_confirm = [By.CSS_SELECTOR, 'div[class^="Order_Modal"]']
    # Кнопка "Да"
    locator_confirm_confirm = [By.CSS_SELECTOR, 'div[class^="Order_Modal"] button[class^="Button_Button"]:nth-child(2)']

    def submit(self):
        self.is_visible(self.locator_confirm)
        self.submit_form(self.locator_confirm_confirm)