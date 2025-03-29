import locators.order_locators as locators
from selenium.webdriver.common.keys import Keys

form_inputs = [[
        [
            {'type': 'input', 'locator': locators.order_field_name, 'data': 'Петя'},
            {'type': 'input', 'locator': locators.order_field_second_name, 'data': 'Петров'},
            {'type': 'input', 'locator': locators.order_field_address, 'data': 'ул. Первомаяскаяб д.5'},
            {'type': 'input', 'locator': locators.order_field_phone, 'data': '+79992223344'},
            {'type': 'select', 'locator': locators.order_field_metro, 'locator_item': locators.order_field_metro_select_item, 'index': 3}
        ],
        [
            {'type': 'input', 'locator': locators.order_field_date, 'data': '12.09.2025' + Keys.ENTER},
            {'type': 'input', 'locator': locators.order_field_comment, 'data': 'Оставить у подъезда'},
            {'type': 'select', 'locator': locators.order_field_period, 'locator_item': locators.order_field_period_select_option, 'index': 3},
            {'type': 'select', 'locator_item': locators.order_field_color, 'index': 0}
        ]
    ],[
        [
            {'type': 'input', 'locator': locators.order_field_name, 'data': 'Иван'},
            {'type': 'input', 'locator': locators.order_field_second_name, 'data': 'Иванов'},
            {'type': 'input', 'locator': locators.order_field_address, 'data': 'ул. Бакунинская, д51'},
            {'type': 'input', 'locator': locators.order_field_phone, 'data': '+79992225566'},
            {'type': 'select', 'locator': locators.order_field_metro,
             'locator_item': locators.order_field_metro_select_item, 'index': 3}
        ],
        [
            {'type': 'input', 'locator': locators.order_field_date, 'data': '12.09.2025' + Keys.ENTER},
            {'type': 'input', 'locator': locators.order_field_comment, 'data': 'Прелупредить за час до выезда'},
            {'type': 'select', 'locator': locators.order_field_period,
             'locator_item': locators.order_field_period_select_option, 'index': 3},
            {'type': 'select', 'locator_item': locators.order_field_color, 'index': 0}
        ]
]]