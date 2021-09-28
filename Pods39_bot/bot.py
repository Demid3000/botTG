import telebot
from telebot import types, TeleBot

import config

bot: TeleBot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    #keyboard
    item1 = types.KeyboardButton("💜Жижи💜")
    item2 = types.KeyboardButton("❤Поды❤")
    item3 = types.KeyboardButton("О нас/Связь")
    item4 = types.KeyboardButton("🛠Техподдержка🛠")
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Приветствую тебя, {0.first_name} в нашем магазине Pods39 и т.д".format(message.from_user, bot.get_me()), parse_mode='html',  reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '💜Жижи💜':
            markup = types.InlineKeyboardMarkup()
            pay = types.InlineKeyboardButton(text='Заказать', url='https://t.me/gengstaInScaM')
            markup.add(pay)
            bot.send_photo(message.chat.id, 'https://ic.wampi.ru/2021/09/14/ZIZKI.jpg', caption='Тут список цен на каждую жижу(текст можно сделать жирнее) типа так \n *Бруско - 450* \n *Хаски* - _400_', parse_mode="Markdown", reply_markup=markup)
        elif message.text == '❤Поды❤':
            markup = types.InlineKeyboardMarkup()
            pay = types.InlineKeyboardButton(text='Заказать', url='https://t.me/gengsta228')
            markup.add(pay)
            bot.send_photo(message.chat.id, 'https://ic.wampi.ru/2021/09/14/PODY.jpg', caption='Так же как и с жижами', parse_mode="Markdown", reply_markup=markup)
        elif message.text == 'О нас/Связь':
            markup = types.InlineKeyboardMarkup()
            vk = types.InlineKeyboardButton(text='VK', url='https://vk.com/dmdkuznecov')
            markup.add(vk)
            bot.send_message(message.chat.id, 'Лучший бот в Калининграде с жижками и подами!', reply_markup=markup)
        elif message.text == '🛠Техподдержка🛠':
            bot.send_message(message.chat.id, 'Для связи с ТС пишите: @gengstaInScaM')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

# RUN
bot.polling(none_stop=True)