from flask import Flask, request, Response, jsonify
from aiogram import Bot, Dispatcher, types

import settings

bot = Bot(token=settings.API_KEY, parse_mode="html")
dp = Dispatcher(bot)
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    # if request.headers.get('content-type') == 'application/json':
    print(123)
    # return jsonify({"message": "OK"})
    return "<h1>Hello test</h1>"


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "Hello",
    )


# @dp.message_handler(content_types=['text'])
# def send_message(message: types.Message):
#     if message == "привет":
#         bot.send_message(
#             message.from_user.id,
#             "Hello Hello",
#         )
#     else:
#         bot.send_message(
#             message.from_user.id,
#             "Not hello for you",
#         )


if __name__ == '__main__':
    app.run(port=8003, debug=True, host='0.0.0.0')
