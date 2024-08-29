# Инлайн-клавиатура 1: Выбор типа сайта
web_type_inline_keyboard = [
    [{'text': 'Корпоративные сайты', 'callback_data': 'web_corporate'}, {'text': 'Интернет-магазины', 'callback_data': 'web_shop'}],
    [{'text': 'Лендинги', 'callback_data': 'web_landing'}, {'text': 'Назад', 'callback_data': 'back_services'}]
]

# Инлайн-клавиатура 2: Выбор стека технологий для сайта
web_technologies_inline_keyboard = [
    [{'text': 'HTML/CSS', 'callback_data': 'tech_html_css'}, {'text': 'JavaScript', 'callback_data': 'tech_js'}],
    [{'text': 'Python/Django', 'callback_data': 'tech_python_django'}, {'text': 'Назад', 'callback_data': 'back_web_types'}]
]

# Инлайн-клавиатура 3: Выбор типа мобильного приложения
mobile_type_inline_keyboard = [
    [{'text': 'iOS приложения', 'callback_data': 'mobile_ios'}, {'text': 'Android приложения', 'callback_data': 'mobile_android'}],
    [{'text': 'Кроссплатформенные', 'callback_data': 'mobile_crossplatform'}, {'text': 'Назад', 'callback_data': 'back_services'}]
]

# Инлайн-клавиатура 4: Выбор стека технологий для мобильных приложений
mobile_technologies_inline_keyboard = [
    [{'text': 'Swift', 'callback_data': 'tech_swift'}, {'text': 'Kotlin', 'callback_data': 'tech_kotlin'}],
    [{'text': 'Flutter', 'callback_data': 'tech_flutter'}, {'text': 'Назад', 'callback_data': 'back_mobile_types'}]
]

# Инлайн-клавиатура 5: Выбор системы для интеграции
integration_systems_inline_keyboard = [
    [{'text': 'CRM системы', 'callback_data': 'integration_crm'}, {'text': 'Платежные системы', 'callback_data': 'integration_payments'}],
    [{'text': 'Аналитические системы', 'callback_data': 'integration_analytics'}, {'text': 'Назад', 'callback_data': 'back_services'}]
]

# Инлайн-клавиатура 6: Подтверждение заказа
confirm_order_inline_keyboard = [
    [{'text': 'Подтвердить заказ', 'callback_data': 'confirm_order'}, {'text': 'Отменить заказ', 'callback_data': 'cancel_order'}],
    [{'text': 'Назад', 'callback_data': 'back_main_menu'}]
]

# Инлайн-клавиатура 7: Выбор контактного способа
contact_options_inline_keyboard = [
    [{'text': 'Позвонить', 'callback_data': 'contact_call'}, {'text': 'Написать Email', 'callback_data': 'contact_email'}],
    [{'text': 'Назад', 'callback_data': 'back_contacts'}]
]

# Инлайн-клавиатура 8: Информация о компании
about_company_inline_keyboard = [
    [{'text': 'Наши проекты', 'callback_data': 'about_projects'}, {'text': 'Наши клиенты', 'callback_data': 'about_clients'}],
    [{'text': 'Назад', 'callback_data': 'back_main_menu'}]
]

# Инлайн-клавиатура 9: Заказ услуги
order_service_inline_keyboard = [
    [{'text': 'Заказать разработку сайта', 'callback_data': 'order_web'}, {'text': 'Заказать мобильное приложение', 'callback_data': 'order_mobile'}],
    [{'text': 'Заказать интеграцию', 'callback_data': 'order_integration'}, {'text': 'Назад', 'callback_data': 'back_main_menu'}]
]

# Инлайн-клавиатура 10: Назад к главному меню
back_to_main_menu_inline_keyboard = [
    [{'text': 'Назад в главное меню', 'callback_data': 'back_main_menu'}]
]

# Инлайн-клавиатура 11: Выбор типа оплаты
payment_type_inline_keyboard = [
    [{'text': 'Оплата картой', 'callback_data': 'payment_card'}, {'text': 'Оплата через PayPal', 'callback_data': 'payment_paypal'}],
    [{'text': 'Назад', 'callback_data': 'back_order_service'}]
]

# Инлайн-клавиатура 12: Подтверждение контактных данных
confirm_contact_inline_keyboard = [
    [{'text': 'Подтвердить телефон', 'callback_data': 'confirm_phone'}, {'text': 'Подтвердить Email', 'callback_data': 'confirm_email'}],
    [{'text': 'Назад', 'callback_data': 'back_contact_options'}]
]

# Инлайн-клавиатура 13: Выбор языка интерфейса
language_selection_inline_keyboard = [
    [{'text': 'Русский', 'callback_data': 'lang_ru'}, {'text': 'English', 'callback_data': 'lang_en'}],
    [{'text': 'Назад', 'callback_data': 'back_main_menu'}]
]

# Обычная клавиатура 6: Корпоративные сайты
corporate_sites_keyboard = [
    ['Описание услуги', 'Цены'],
    ['Примеры работ', 'Назад к разработке сайтов']
]

# Обычная клавиатура 7: Интернет-магазины
web_shop_keyboard = [
    ['Описание услуги', 'Цены'],
    ['Примеры работ', 'Назад к разработке сайтов']
]

# Обычная клавиатура 8: Лендинги
landing_pages_keyboard = [
    ['Описание услуги', 'Цены'],
    ['Примеры работ', 'Назад к разработке сайтов']
]
# Обычная клавиатура 1: Главное меню
main_menu_keyboard = [
    ['Услуги', 'О компании'],
    ['Контакты', 'Сделать заказ']
]

# Обычная клавиатура 2: Услуги
services_keyboard = [
    ['Разработка сайтов', 'Мобильные приложения'],
    ['Интеграция систем', 'Назад в главное меню']
]

# Обычная клавиатура 3: Разработка сайтов
web_development_keyboard = [
    ['Корпоративные сайты', 'Интернет-магазины'],
    ['Лендинги', 'Назад к услугам']
]

# Обычная клавиатура 4: Мобильные приложения
mobile_apps_keyboard = [
    ['iOS приложения', 'Android приложения'],
    ['Кроссплатформенные', 'Назад к услугам']
]

# Обычная клавиатура 5: Контакты
contacts_keyboard = [
    ['Телефон', 'Email'],
    ['Адрес', 'Назад в главное меню']
]


# Словарь с обычными клавиатурами
keyboards = {
    'main_menu_keyboard': main_menu_keyboard,
    'services_keyboard': services_keyboard,
    'web_development_keyboard': web_development_keyboard,
    'mobile_apps_keyboard': mobile_apps_keyboard,
    'contacts_keyboard': contacts_keyboard,
    'corporate_sites_keyboard': corporate_sites_keyboard,
    'web_shop_keyboard': web_shop_keyboard,
    'landing_pages_keyboard': landing_pages_keyboard
}


# Словарь с инлайн-клавиатурами
inline_keyboards = {
    'web_type_inline_keyboard': web_type_inline_keyboard,
    'web_technologies_inline_keyboard': web_technologies_inline_keyboard,
    'mobile_type_inline_keyboard': mobile_type_inline_keyboard,
    'mobile_technologies_inline_keyboard': mobile_technologies_inline_keyboard,
    'integration_systems_inline_keyboard': integration_systems_inline_keyboard,
    'confirm_order_inline_keyboard': confirm_order_inline_keyboard,
    'contact_options_inline_keyboard': contact_options_inline_keyboard,
    'about_company_inline_keyboard': about_company_inline_keyboard,
    'order_service_inline_keyboard': order_service_inline_keyboard,
    'back_to_main_menu_inline_keyboard': back_to_main_menu_inline_keyboard,
    'payment_type_inline_keyboard': payment_type_inline_keyboard,
    'confirm_contact_inline_keyboard': confirm_contact_inline_keyboard,
    'language_selection_inline_keyboard': language_selection_inline_keyboard
}
