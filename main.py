import logging

from aiogram.utils.executor import start_webhook
# from flask import Flask, request, abort
from aiogram import Bot, Dispatcher, types

import settings

API_TOKEN = settings.API_KEY

# webhook settings
WEBHOOK_HOST = 'https://8eb8-213-230-102-125.eu.ngrok.io'
WEBHOOK_PATH = '/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '0.0.0.0'  # or ip
WEBAPP_PORT = 8003

bot = Bot(token=API_TOKEN, parse_mode="html")
dp = Dispatcher(bot)
# app = Flask(__name__)


# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.headers.get('content-type') == 'application/json':
#         return request.stream.read().decode('utf-8')
#     else:
#         abort(403)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_HOST)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "Hello",
    )


@dp.message_handler(content_types=['text'])
async def send_message(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'test',
    )


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
