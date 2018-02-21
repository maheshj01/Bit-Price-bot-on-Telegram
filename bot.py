import telebot
import requests
import time
import json

bot_token = '477501756:AAFkPGmVOewzI_Ruh7i44g9IPeFBhetXX00'
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
    help="Hi " + username + " ! \nthis bot sends you crypto market stats from various exchanges.\nBittrex\nto get altcoin stats from bittrex send a crypto pair e.g btc-eth \n "
    help=help + "\nZebpay\nto get price of btc,ltc,bch,xrp from zebpay in inr  send \n/zebpay btc \n/zebpay ltc \n/zebpay bch\n/zebpay xrp"
    bot.send_message(message.chat.id,help)

@bot.message_handler(commands=['zebpay'])
def compare_price(message):
    url = "https://www.zebapi.com/api/v1/market/ticker-new/"
    try:
        currency=message.text.strip("/zebpay")
        currency=currency.strip()
        if len(currency) !=0:
            url=url + currency + "/inr"
            response = requests.get(url)
            zebticker ="buy price:" + str(response.json()['buy'])+ " inr" +"\nsell price:" + str(response.json()['sell'])
            zebticker=zebticker + " inr" + "\nVolume:" + str(response.json()['volume'])+currency
            bot.send_message(message.chat.id,zebticker)
        else:
            bot.send_message(message.chat.id,"please follow the format \n e.g /zebpay ltc \n or try using /help")
    except Exception:
        print(Exception)
        bot.send_message(message.chat.id,"invalid currency,\nplease try /help")

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
            text="Last Price:" + str(response["result"][0]['Last']) +" "+ str(coin[0]) + "\nHigh:" + str(response["result"][0]['High']) +"\nLow:" + str(response["result"][0]['Low']) + "\nVolume:" + str(response["result"][0]['Volume'])
            bot.send_message(chatid,text)
        else:
            print "success:false"
            text="Invalid pair entered,please try again! or use /help"
            bot.send_message(chatid,text)
    except Exception:
        print(Exception)
        print("your internet is broken :( please try again!")


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(10)

































