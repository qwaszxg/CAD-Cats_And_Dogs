import os

from dotenv import load_dotenv

from telegram.ext import Updater
from telegram import ReplyKeyboardMarkup

load_dotenv()

TOKEN = os.getenv('TOKEN')

URL_DOG = os.getenv('URL_DOG')

URL_CAT = os.getenv('URL_CAT')

# CHAT_ID = 1163164424

updater = Updater(token=TOKEN, use_context=True)

BUTTON = ReplyKeyboardMarkup([['Новая собачка', 'Новый котик', 'Собачка с котиком'], ['Мои возможности']], resize_keyboard=True)

BUTTON_HI = ReplyKeyboardMarkup([['/start'], ['Мои возможности']], resize_keyboard=True)