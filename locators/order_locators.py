from selenium.webdriver.common.by import By

# Кнопка заказать (вверху страницы)
order_button_top = [By.CSS_SELECTOR, 'div[class^="Header_Nav"] > button[class^="Button_Button"]']

# Кнопка заказать (внизу страницы)
order_button_bottom = [By.CSS_SELECTOR, 'div[class^="Home_FinishButton"] > button[class^="Button_Button"]']

# Форма заказа
order_form = [By.CSS_SELECTOR, 'div[class^="Order_Form"]']

# Поле "Имя"
order_field_name = [By.CSS_SELECTOR, 'input[type="text"][placeholder="* Имя"]']

# Поле "Фамилия"
order_field_second_name = [By.CSS_SELECTOR, 'input[type="text"][placeholder="* Фамилия"]']

# Поле "Адресс"
order_field_address = [By.CSS_SELECTOR, 'input[type="text"][placeholder="* Адрес: куда привезти заказ"]']

# Поле "Станция метро"
order_field_metro = [By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]']

# Поле "Станция метро" - выдабщий список
order_field_metro_select = [By.CLASS_NAME, 'select-search__select']

# Поле "Станция метро" - элемент выпадающего списка
order_field_metro_select_item = [By.CLASS_NAME, 'select-search__row']

# Поле "Телефон"
order_field_phone = [By.CSS_SELECTOR, 'input[type="text"][placeholder="* Телефон: на него позвонит курьер"]']

# Кнопка "Далее"
order_button_next = [By.CSS_SELECTOR, 'div[class^="Order_NextButton"] > button[class^="Button_Button"]']

# Всплывающее окно с сообщением об успешном создании заказа

# Логотип «Самоката»
order_link_logo_scooter = [By.CSS_SELECTOR, 'div[class^="Header_Logo"] > a[class^="Header_LogoScooter"]']

# Логотип "Яндекса"
order_link_logo_yandex = [By.CSS_SELECTOR, 'div[class^="Header_Logo"] > a[class^="Header_LogoYandex"]']

# Поде "Дата"
order_field_date = [By.CSS_SELECTOR, 'input[type="text"][placeholder="* Когда привезти самокат"]']

# Поле "Срок аренды"
order_field_period = [By.CLASS_NAME, 'Dropdown-control']

# Поле "Срок аренды" - выпадающий список
order_field_period_select = [By.CLASS_NAME, 'Dropdown-menu']

# Поле "Срок аренды" - элемент выпадающего списка
order_field_period_select_option = [By.CLASS_NAME, 'Dropdown-option']

# Поле "Выбор цвета"
order_field_color = [By.CSS_SELECTOR, 'input[type="checkbox"]']

# Поле "Комментарии"
order_field_comment = [By.CSS_SELECTOR, 'input[type="text"][placeholder="Комментарий для курьера"]']

# Кнопка "Заказать"
order_button_order = [By.CSS_SELECTOR, 'div[class^="Order_Buttons"] > button[class^="Button_Button"]:nth-child(2)']

# Форма подтверждения заказа
order_confirm = [By.CSS_SELECTOR, 'div[class^="Order_Modal"]']

# Кнопка "Да"
order_confirm_confirm = [By.CSS_SELECTOR, 'div[class^="Order_Modal"] button[class^="Button_Button"]:nth-child(2)']
