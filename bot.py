from telebot import types

# Обработка команд и заказов
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    # Ваш код обработки команд start и help

@bot.message_handler(commands=['order'])
def handle_order(message):
    # Запрос имени пользователя
    msg = bot.reply_to(message, 'Введите ваше имя:')
    bot.register_next_step_handler(msg, ask_phone_number)

def ask_phone_number(message):
    # Получение имени пользователя
    name = message.text

    # Запрос номера телефона
    msg = bot.reply_to(message, 'Введите ваш номер телефона:')
    bot.register_next_step_handler(msg, ask_width, name)

def ask_width(message, name):
    # Получение номера телефона
    phone_number = message.text

    # Запрос ширины окна
    msg = bot.reply_to(message, 'Введите ширину окна в сантиметрах:')
    bot.register_next_step_handler(msg, ask_height, name, phone_number)

def ask_height(message, name, phone_number):
    # Получение ширины окна
    width = message.text

    # Запрос высоты окна
    msg = bot.reply_to(message, 'Введите высоту окна в сантиметрах:')
    bot.register_next_step_handler(msg, ask_material, name, phone_number, width)

def ask_material(message, name, phone_number, width):
    # Получение высоты окна
    height = message.text

    # Создание клавиатуры с вариантами материалов
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    material_1 = types.KeyboardButton('Материал 1')
    material_2 = types.KeyboardButton('Материал 2')
    material_3 = types.KeyboardButton('Материал 3')
    material_4 = types.KeyboardButton('Материал 4')
    keyboard.add(material_1, material_2, material_3, material_4)

    # Запрос выбора материала
    msg = bot.reply_to(message, 'Выберите тип материала окна:', reply_markup=keyboard)
    bot.register_next_step_handler(msg, send_order, name, phone_number, width, height)

def send_order(message, name, phone_number, width, height):
    # Получение выбранного материала
    material = message.text

    # Формирование данных о заказе
    order_data = f'Имя: {name}\nНомер телефона: {phone_number}\nШирина: {width} см\nВысота: {height} см\nМатериал: {material}'

    # Отправка данных о заказе в телеграм-чат
    send_telegram_message(order_data)

    bot.reply_to(message, 'Спасибо за ваш заказ!')

# Запуск бота
bot.polling()