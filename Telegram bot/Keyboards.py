from telebot import types

#TODO убрать команды из кнопок, чтобы выглядило хорошо

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row("/help", "МТУСИ")

keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
NextPage = types.KeyboardButton("Следующая страница👉")
keyboard1.row("Начать💎", "Помощь😿", "Справка📄")
keyboard1.row(NextPage)

keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
PrevPage = types.KeyboardButton("👈Предыдущая страница")
keyboard2.row("Хочу спать", "Пошли гулять", "Выключи свет", "Скажи мой id",)
keyboard2.row(PrevPage)

Home_button = types.KeyboardButton("В начало🏠")

keyboard_link = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_link.row("О проекте⚙", "Инст📺", "ВК👥", "GitHub💾")
keyboard_link.row(Home_button)
keyboard_link.row("Мтуси💌", "Мтуси📺", "Мтуси👥", "Мтуси🔎")

keyboard_rasp = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_rasp.row("Понедельник🏞", "Вторник🌅", "Среда🌄")
keyboard_rasp.row("Текущая неделя", Home_button, "Неделя🗓", "Следующая неделя")
keyboard_rasp.row("Четверг🌠", "Пятница🎇", "Суббота🎆")

Backtorasp = types.KeyboardButton("Назад к расписанию")

keyboard_backtorasp = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_backtorasp.row(Backtorasp)
keyboard_backtorasp.row(Home_button)