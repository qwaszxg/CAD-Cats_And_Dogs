from settings import updater
from telegram.ext import MessageHandler, CommandHandler, Filters
import requests
from settings import (URL_DOG,
                      URL_CAT,
                      BUTTON,
                      BUTTON_HI)

from script_phrases import *
from random import randint


def response_url(url):
    response = requests.get(url).json()
    random_url = response[0].get('url')
    return random_url

def new_dog(update, context):
    id = update.message.from_user.id
    caption = random_text_for_dog[randint(0, 4)]
    context.bot.send_photo(id,
                           photo=response_url(URL_DOG),
                           caption=caption,
                           reply_markup=BUTTON)

def new_cat(update, context):
    id = update.message.from_user.id
    caption = random_text_for_dog[randint(0, 4)]
    context.bot.send_photo(id,
                           photo=response_url(URL_CAT),
                           caption=caption,
                           reply_markup=BUTTON)

def all_animals(update, context):
    id = update.message.from_user.id
    context.bot.send_message(id,
                             text=random_text_for_all_animals[randint(0, 4)],
                             reply_markup=BUTTON)
    context.bot.send_photo(id, response_url(URL_DOG))
    context.bot.send_photo(id, response_url(URL_CAT))

def say_hi(update, context):
    user_name = update.message.from_user.first_name
    id = update.message.from_user.id
    context.bot.send_message(id, text=f'Привет, {user_name}! Я включился!', reply_markup=BUTTON_HI)
    for item in loader:
        context.bot.send_message(id, text=item, reply_markup=BUTTON_HI)

def i_can(update, context):
    id = update.message.from_user.id
    for item in what_i_can:
        context.bot.send_message(id, text=item, reply_markup=BUTTON)

def main():

    updater.dispatcher.add_handler(CommandHandler('start', say_hi))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('Мои возможности'), i_can))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('Новая собачка'), new_dog))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('Новый котик'), new_cat))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('Собачка с котиком'), all_animals))

    updater.start_polling(poll_interval=0.1)
    updater.idle()

if __name__ == "__main__":
    main()