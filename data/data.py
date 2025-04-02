from selenium.webdriver.common.keys import Keys

form_inputs = [[
        [
            {'type': 'input', 'name': 'name', 'data': 'Петя'},
            {'type': 'input', 'name': 'second_name', 'data': 'Петров'},
            {'type': 'input', 'name': 'address', 'data': 'ул. Первомаяскаяб д.5'},
            {'type': 'input', 'name': 'phone', 'data': '+79992223344'},
            {'type': 'select', 'name': 'metro', 'item': 'metro_item', 'index': 3}
        ],
        [
            {'type': 'input', 'name': 'date', 'data': '12.09.2025' + Keys.ENTER},
            {'type': 'input', 'name': 'comment', 'data': 'Оставить у подъезда'},
            {'type': 'select', 'name': 'period', 'item': 'period_item', 'index': 3},
            {'type': 'checkbox', 'name': 'color', 'index': 0}
        ]
    ],[
        [
            {'type': 'input', 'name': 'name', 'data': 'Иван'},
            {'type': 'input', 'name': 'second_name', 'data': 'Иванов'},
            {'type': 'input', 'name': 'address', 'data': 'ул. Бакунинская, д51'},
            {'type': 'input', 'name': 'phone', 'data': '+79992225566'},
            {'type': 'select', 'name': 'metro', 'item': 'metro_item', 'index': 3}
        ],
        [
            {'type': 'input', 'name': 'date', 'data': '20.10.2025' + Keys.ENTER},
            {'type': 'input', 'name': 'comment', 'data': 'Прелупредить за час до выезда'},
            {'type': 'select', 'name': 'period', 'item': 'period_item', 'index': 3},
            {'type': 'checkbox', 'name': 'color', 'index': 1}
        ]
]]