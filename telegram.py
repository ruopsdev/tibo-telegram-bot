# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the private license.

"""
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import os
import requests
import random
import math
import logging
# import json

from flask import Flask, request

import teleads

import asyncio
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.utils.markdown import bold, hbold
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from teleads.aiogram3 import BapMiddleware

# from teleads.aiogram3 import BapMiddleware
# from teleads.aiogram2 import BapMiddleware

# dp.update.middleware(BapMiddleware("meteoritt"))

import telebot

from telebot import types
from telebot.types import Message
from telebot import apihelper

# MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
TIBO_TELEGRAM_BOT_TOKEN = os.environ['TIBO_TELEGRAM_BOT_TOKEN']
TOKEN_METEORITT = getenv("BOT_TOKEN", "TIBO_TELEGRAM_BOT_TOKEN")
METEORITT_ID = getenv("TELEADS_API_KEY", "meteoritt")
OPEN_WAETHER_MAP_TOKEN = 'e92f4ab649c62931261157c7cf958e1d'


# TIMEZONE = 'Asia/Yekaterinburg'
# TIMEZONE_COMMON_NAME = 'Yekaterinburg'
# P_TIMEZONE = pytz.timezone(config.TIMEZONE)
# TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME


service_id = os.environ['RENDER_SERVICE_ID']
api_key = os.environ['RENDER_API_KEY']
url = f"https://api.render.com/v1/services/{service_id}/restart"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
# response = requests.post(url, headers=headers)
# print(response.status_code)


def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    Note: This is called AFTER message handlers, so it won't interfere with processing.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            first_name = getattr(m.chat, 'first_name', 'Unknown')
            print(f"Listener: {first_name} [{m.chat.id}]: {m.text}")


bot = telebot.TeleBot(TIBO_TELEGRAM_BOT_TOKEN, threaded=False)
bot.set_update_listener(listener)  # register listener
print(f"Bot initialized with token: {TIBO_TELEGRAM_BOT_TOKEN[:10]}...")
STICKERID = 'CAACAgIAAxkBAAMbXrPw-PFI1fxdd1PM4gvH4ByBzU8AAqwAA1dPFQieKyFie6ajbxkE'

# USERS = set()

telebot.logger.setLevel(logging.DEBUG)

knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start': 'Get used to the bot',
    'help': 'Gives you information about the available commands',
    'getimage': 'A test using multi-stage messages, custom keyboard, and media sending',
    'weather': 'OpenWeatherMap data',
    'погода': 'по-русски',
    'bar': 'GO DRINK',
    'mem': 'send memories',
    'meme': 'send memories pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679',
    'emotion': 'AI @albert_ai_bot love you so much my lifehack' 
}

beer_photo = [
    "https://img1.thelist.com/img/gallery/what-happens-to-your-body-when-you-drink-beer-every-night/intro-1577191347.jpg",
    "https://i.ytimg.com/vi/TumxeIPQfTI/maxresdefault.jpg",
    "https://media-cdn.tripadvisor.com/media/photo-s/10/bd/94/25/drink-beer.jpg",
    "https://media.daysoftheyear.com/20171223124045/drink-beer-day1.jpg",
    "https://kajabi-storefronts-production.global.ssl.fastly.net/kajabi-storefronts-production/blogs/15486/images/0snKererQUCYqgNGYGNA_vegan-beer.jpg",
    "https://cdn.craftbeer.com/wp-content/uploads/Craft-Beer-Glasses-1200.jpg",
    "https://static.toiimg.com/thumb/msid-10815880,width-800,height-600,resizemode-75/10815880.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMn1izpSbHb0ClIycPeiePnl1Ct9fG6qmJcBLKSTulaSmaVGyyjg&s",
    "https://www.tasteofhome.com/wp-content/uploads/2019/03/shutterstock_1212903172-line-of-beers.jpg",
    "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/close-up-of-hands-holding-beer-glasses-royalty-free-image-736280003-1534346317.jpg?crop=0.669xw:1.00xh;0.166xw,0&resize=640:*",
    "https://d.newsweek.com/en/full/889150/00.jpg?w=737&f=f9b6f7a8e63a146820640f5531752c0c",
    "https://media.npr.org/assets/img/2018/10/16/rts1u2te-71fe69214f2094429ea5ca2485cd1fbd5ee8383f-s800-c85.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqe0xsBCQK1sR0JyRVofx3oJns30ApYA1pk59DpTpdeqxD4Lc1&s",
    "https://www.dw.com/image/43830445_303.jpg",
    "https://www.ft.com/__origami/service/image/v2/images/raw/http://prod-upp-image-read.ft.com/8db8265e-1cff-11ea-81f0-0c253907d3e0?source=next&fit=scale-down&quality=highest&width=1067",
    "https://static-38.sinclairstoryline.com/resources/media/95577ddb-38e7-4480-9723-81b89498a10f-large1x1_MGN_1280x960_70804P00KLNAV.jpg?1587064678520",
    "https://upload.wikimedia.org/wikipedia/commons/d/db/Aufse%C3%9F_Bier.JPG",
    "https://img.washingtonpost.com/rf/image_1484w/2010-2019/WashingtonPost/2017/02/01/Food/Images/food_011-004.JPG?uuid=_NMimOgwEeaQPZsR7X2NKg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo85_Z348eJyMvHDtwy-BcLl8B1XltoHaK1xhcUr7sEcQDWGZT&s",
    "https://katu.com/resources/media/bad96236-45dd-405d-895a-89a85b619707-large16x9_manifest4.PNG?1588253194556",
    "https://www.mlive.com/resizer/OhjAoigJKQKOsIbXWO6Gwd-Week=/450x0/smart/image.mlive.com/home/mlive-media/width600/img/michigan_beer/photo/2017/09/28/celebrate-national-drink-beer-day-01020f2d1f374e07.jpg"
]

bar_members = {
    '41365750': {
        'username': 'ChudakovSergey',
        'first': 'Sergey'
    },
    '670403191': {
        'username': 'elijah_here',
        'first': 'Илья',
        'last': 'Полосков'
    },
    '1006923818': {
        'first': 'James',
        'last': 'Touchet'
    },
    '61049840': {
        'first': 'Pavel',
        'last': 'S'
    },
    '652907968': {
        'first': 'Nikita'
    }
}
            
            
# handle the "/check" command
@bot.message_handler(commands=['check'])
def command_check(m):
    try:
        cid = m.chat.id
        print(f"Command_/start handler triggered! Chat ID: {cid}, Message: {m.text}")
        if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
            knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
            userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
            print(f"Sending welcome messages to {cid}")
            bot.send_message(cid, "Hello, stranger, let me scan you...")
            bot.send_message(cid, "Scanning complete, I know you now")
            command_help(m)  # show the new user the help page
            print(f"Successfully processed /start for new user {cid}")
        else:
            print(f"User {cid} already known, sending existing user message")
            bot.send_message(cid, "I already know you, no need for me to scan you again!")
    except Exception as e:
        print(f"Error in command_start: {e}")
        import traceback
        traceback.print_exc()
        try:
            bot.send_message(m.chat.id, "Sorry, an error occurred. Please try again.")
        except Exception as send_error:
            print(f"Failed to send error message: {send_error}")


@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + " - "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)
    bap.send_advertisement(update)# send the generated help page


@bot.message_handler(commands=['promo'])
async def command_promo(m):
    cid = m.chat.id
    service = teleads.Bap('meteoritt')
    # sending telegram update data
    needHandle = await service.handle_update(
        {
            'update_id': cid,
            # ...
        }
    )
    bap.send_advertisement(update)

    # or if your advertisement mode is set to manual you can mark ad placement in your code by calling:
    await service.send_advertisement(
        {
            'update_id': cid
            # ...
        }
    )

    dp.update.middleware(BapMiddleware("meteoritt"))

    # dp.update.middleware(BapMiddleware("meteoritt"))


default_city = 'Perm'


def weather_get(apikey, city):
    try:
        r = requests.get("https://api.openweathermap.org/data/2.5/weather",
                         params={'q': city, 'units': 'metric', 'APPID': apikey})
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"Weather error: {e}")
        return None


@bot.message_handler(commands=['weather', 'погода'])
def command_weather(message: Message):
    cid = message.chat.id
    command_params = message.text.split()
    params_count = len(command_params)
    city = command_params[1] if params_count > 1 else default_city
    weather = weather_get(OPEN_WAETHER_MAP_TOKEN, city)
    print(weather)
    if weather is None:
        bot.send_message(cid, f'Failed to get weather data for {city}')
        return
    conditions = weather['weather'][0]['description']
    current_temp = weather['main']['temp']
    temp_min = weather['main']['temp_min']
    temp_max = weather['main']['temp_max']
    bot.send_message(cid,
                     f'{current_temp} {conditions}, up to {temp_max}, at night {temp_min}')


@bot.message_handler(commands=['8', 'eight', 'восемь', 'рандом'])
def command_eight(message: Message):
    cid = message.chat.id
    command_params = message.text.split()
    chislo = random.randint(1, 100)
    print(chislo)
    bot.send_message(cid, f'{chislo}')
    bot.send_message(cid,
                     f'{chislo}')


@bot.message_handler(commands=['3.14', '3', 'three', 'три', 'pi', 'пи'])
def command_pi(message: Message):
    cid = message.chat.id
    command_params = message.text.split()
    pi = math.pi
    print(pi)
    bot.send_message(cid, f'{pi}')
    bot.send_message(cid,
                     f'{pi}')


def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


@bot.message_handler(commands=['bar'])
def command_bar(message: Message):
    cid = message.chat.id
    chat = bot.get_chat(message.chat.id)
    mention = []
    for i in bar_members:
        if 'username' in bar_members[i]:
            user = bar_members[i].get('username')
            mention.append(f'@{user}')
        else:
            first = bar_members[i].get('first')
            last = bar_members[i].get('last')
            mention.append(f'<a href="tg://user?id={i}">{first} {last}</a>')
    random.shuffle(mention)
    print(mention)
    push_alert = listToString(mention)
    print(push_alert)
    bot.send_message(cid, f'{push_alert} GO BAR', parse_mode="HTML")
    bot.send_poll(cid, 'DRINK BEER SAVE WATER', ["Drink beer", "Discord", "Play computer"], is_anonymous=False)
    pic_choise = random.randint(0, len(beer_photo))
    bot.send_photo(cid, beer_photo[pic_choise])
    # bot.send_poll(cid, 'Poll', {
    #     "Drink beer",
    #     "Play computer"
    # })


@bot.message_handler(commands=['mem'])
def command_mem(message: Message):
    cid = message.chat.id
    r = requests.get("https://api.imgflip.com/get_memes")
    print(r.content)
    json_data = r.json()
    list_mem = json_data['data']['memes']
    # print(list_mem)
    count_memes = len(list_mem)
    mem = []
    for i in range(0, count_memes):
        mem.append(json_data['data']['memes'][i]['url'])
        # print(mem[i])
    random.shuffle(mem)
    bot.send_photo(cid, mem[0])


# test api
@bot.message_handler(commands=['getimage', 'image'])
def command_image(message: Message):
    cid = message.chat.id
    r = requests.get("https://api.imgflip.com/get_memes")
    print(r.content)
    json_data = r.json()
    list_mem = json_data['data']['memes']
    # print(list_mem)
    count_memes = len(list_mem)
    image = []
    for i in range(0, count_memes):
        image.append(json_data['data']['memes'][i]['url'])
        # print(image[i])
    random.shuffle(image)
    bot.send_photo(cid, image[0])


@bot.message_handler(commands=['meme'])
def command_mem(message: Message):
    cid = message.chat.id
    r = requests.get("https://api.imgflip.com/get_memes")
    print(r.content)
    json_data = r.json()
    list_mem = json_data['data']['memes']
    # print(list_mem)
    count_memes = len(list_mem)
    meme = []
    for i in range(0, count_memes):
        meme.append(json_data['data']['memes'][i]['url'])
        # print(mem[i])
    random.shuffle(meme)
    bot.send_photo(cid, meme[0])


@bot.message_handler(commands=['help_auth'])
def command_help_auth(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='telegram.me/ChudakovSergey'
        )
    )
    bot.send_message(
        message.chat.id,
        'The bot supports inline. Type @<botusername> in any chat',
        reply_markup=keyboard
    )


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Lazy initialization of NLTK sentiment analyzer
_sia = None


def _ensure_nltk_data():
    """Ensure NLTK data is downloaded (non-blocking check)."""
    try:
        nltk.data.find('sentiment/vader_lexicon.zip')
    except LookupError:
        # Only download if not found
        nltk.download('vader_lexicon', quiet=True)


def _get_sia():
    """Get or initialize SentimentIntensityAnalyzer."""
    global _sia
    if _sia is None:
        _ensure_nltk_data()
        _sia = SentimentIntensityAnalyzer()
    return _sia


def is_positive(message: str) -> str:
    """True if message has positive compound sentiment, False otherwise."""
    sia = _get_sia()
    scores = sia.polarity_scores(message)
    compound = scores["compound"]
    if compound > 0.75:
        return f"😁 {scores}"
    elif compound > 0.5:
        return f"😀 {scores}"
    elif compound > 0.25:
        return f"😊 {scores}"
    elif compound > 0:
        return f"🤨 {scores}"
    elif compound > -0.25:
        return f"😥 {scores}"
    elif compound > -0.5:
        return f"😈 {scores}"
    elif compound > -0.75:
        return f"👹 {scores}"
    elif compound > -1:
        return f"🤬 {scores}"
    else:
        return "🙄"


@bot.message_handler(commands=['emotion', 'themes', 'idea', 'more', 'mind', 'context', 'echo', 'bet', 'produce', 'think', 'note', 'tibo', 'agenda', 'graph', 'map', 'push', 'fact', 'top', 'stat', 'game', 'quiz', 'test', 'chat', 'bio', 'date', 'rpg', 'lol', 'notify', 'quote', 'advice', 'contact', 'donate', 'share', 'random', 'schedule', 'settings', 'new'])
def sentiment_handler(message: Message):
    msg = bot.reply_to(message, """\
    Send your text
    """)
    bot.register_next_step_handler(msg, sentiment_reply)
    # bot.send_message(
    #     message.chat.id,
    #     }'
    # )


def sentiment_reply(message):
    bot.reply_to(message, f'{is_positive(message.text)}')


app = Flask(__name__)


@app.route('/' + TIBO_TELEGRAM_BOT_TOKEN, methods=['POST'])
def getMessage():
    try:
        json_string = request.get_json()
        print(f"Received webhook update: {json_string}")
        if json_string:
            # Convert dict to Update object
            update = telebot.types.Update.de_json(json_string)
            print(f"Parsed update: {update}")
            if update:
                # Check if update has a message
                if update.message:
                    print(f"Update contains message: {update.message.text if update.message.text else 'No text'}")
                # Process updates - this will trigger message handlers
                bot.process_new_updates([update])
                print(f"Processed update successfully")
            else:
                print("Warning: Update object is None")
        # Return immediately to avoid timeout
        return "!", 200
    except Exception as e:
        print(f"Error processing webhook update: {e}")
        import traceback
        traceback.print_exc()
        # Still return 200 to prevent Telegram from retrying
        return "!", 200


@app.route('/')
def webhook():
    try:
        bot.remove_webhook()
        webhook_url = f'https://tibo-telegram-bot.onrender.com/{TIBO_TELEGRAM_BOT_TOKEN}'
        bot.set_webhook(url=webhook_url)
        print(f"Webhook set to: {webhook_url}")
        # Verify webhook info
        webhook_info = bot.get_webhook_info()
        print(f"Webhook info: {webhook_info}")
        return f"Webhook configured: {webhook_url}<br>Webhook info: {webhook_info}", 200
    except Exception as e:
        print(f"Error setting webhook: {e}")
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}", 500


@app.route('/restart', methods=['GET', 'POST'])
def webhook_restart():
    try:
        restart_url = f"https://api.render.com/v1/services/{service_id}/restart"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.post(restart_url, headers=headers)
        print(f"Restart request sent. Status code: {response.status_code}")
        print(f"Restart response: {response.text}")
        
        if response.status_code == 200 or response.status_code == 201:
            # Parse the restart response to get current status
            try:
                restart_data = response.json()
                # Render API returns service info in the restart response
                # Try different possible paths for status
                service_status = None
                if 'service' in restart_data:
                    service_obj = restart_data['service']
                    # Check various possible status fields
                    service_status = (service_obj.get('status') or 
                                    service_obj.get('serviceDetails', {}).get('status') or
                                    service_obj.get('deploy', {}).get('status') or
                                    'Restart initiated')
                elif 'status' in restart_data:
                    service_status = restart_data['status']
                else:
                    service_status = 'Restart initiated'
                
                return f"Service restart initiated successfully.<br>Current Status: {service_status}<br>HTTP Status: {response.status_code}", 200
            except (ValueError, KeyError) as parse_error:
                # If JSON parsing fails, return basic success message
                print(f"Could not parse restart response: {parse_error}")
                return f"Service restart initiated successfully. Status code: {response.status_code}", 200
        else:
            return f"Failed to restart service. Status: {response.status_code}, Response: {response.text}", response.status_code
    except Exception as e:
        print(f"Error restarting service: {e}")
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}", 500


@app.route('/status', methods=['GET'])
def service_status():
    """Check Render service status"""
    try:
        service_url = f"https://api.render.com/v1/services/{service_id}"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(service_url, headers=headers)
        
        if response.status_code == 200:
            service_data = response.json()
            # Try to extract status from various possible locations
            status_info = {}
            if 'service' in service_data:
                service_obj = service_data['service']
                status_info['status'] = service_obj.get('status', 'Unknown')
                status_info['name'] = service_obj.get('name', 'Unknown')
                if 'serviceDetails' in service_obj:
                    status_info['details'] = service_obj['serviceDetails'].get('status', 'Unknown')
            else:
                status_info = service_data
            
            return {
                "service_id": service_id,
                "status": status_info,
                "http_status": response.status_code
            }, 200
        else:
            return {"error": f"Failed to get service status. HTTP {response.status_code}", "response": response.text}, response.status_code
    except Exception as e:
        print(f"Error checking service status: {e}")
        import traceback
        traceback.print_exc()
        return {"error": str(e)}, 500


@app.route('/health')
def health():
    """Health check endpoint"""
    return "OK", 200


@app.route('/debug')
def debug():
    """Debug endpoint to check bot status"""
    try:
        webhook_info = bot.get_webhook_info()
        return {
            "bot_token_set": bool(TIBO_TELEGRAM_BOT_TOKEN),
            "webhook_info": str(webhook_info),
            "known_users_count": len(knownUsers),
            "message_handlers": "Registered"
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500


# Removed automatic restart on module import - restart should only be triggered via /restart endpoint


first_request = True

@app.before_request
def before_first_request_func():
    global first_request
    if first_request:
        bot.send_message(41365750, 'Bot started in Render cloud')  # Updated message
        first_request = False


dp = Dispatcher()
dp.update.middleware(BapMiddleware(METEORITT_ID))

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


if __name__ == "__main__":
    if 'IDE' not in os.environ:
        # logger = telebot.logger
        # telebot.logger.setLevel(logging.INFO)
        app.run(host="0.0.0.0", port=os.environ.get('PORT', 8443))
    else:
        bot.send_message(41365750, 'Bot started from IDE')
        bot.remove_webhook()
        bot.polling(none_stop=True)
