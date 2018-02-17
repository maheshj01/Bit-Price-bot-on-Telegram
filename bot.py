import telebot
import time
import requests
import json

bot_token = '<Token here>'
api_url = "https://api.telegram.org/bot{}/".format(bot_token)

bot=telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username=message.from_user.first_name
    welcome="Hello " + username + " Welcome to bittrex price bot, this bot gives the price of cryptocurrency pair from bittrex in real time,try sending me a valid pair e.g btc-ltc\n incase you need /help "
    bot.send_message(message.chat.id,welcome)

@bot.message_handler(commands=['help'])
def send_help(message):
    username=message.from_user.first_name
    help="Hi " + username + " ! this bot sends you crypto market stats such as \nlast price,High,Low,Volume \nsend me a crypto pair \ne.g btc-eth"
    bot.send_message(message.chat.id,help)

@bot.message_handler(content_types =['text'])
def price(message):
    url='https://bittrex.com/api/v1.1/public/getmarketsummary?market='
    chatid=message.chat.id
    coin=message.text.lower()
    url=url+coin
    coin=coin.split("-")
    coin[0].capitalize()
    try:
        response = requests.get(url).json()
        if(response["success"]==True):
            print "success:true"
            text="Last Price:" + str(response["result"][0]['Last']) + "\nHigh:" + str(response["result"][0]['High']) +"\nLow:" + str(response["result"][0]['Low']) + "\nVolume:" + str(response["result"][0]['Volume'])
            bot.send_message(chatid,text)
        else:
            print "success:false"
            text="Invalid pair entered,please try again! or use /help"
            bot.send_message(chatid,text)
        print("response sent")
    except Exception:
        print(Exception)
        print("your internet is broken :( please try again!")



while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(10)

































