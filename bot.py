import telebot
import requests
import time
import json

bot_token = '477501756:AAFW8vtaZyVe3qF9r-YJqWLFax_ru33-XCM'
api_url = "https://api.telegram.org/bot{}/".format(bot_token)
bot=telebot.TeleBot(token = bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username=message.from_user.first_name
    welcome="Hello *" + username + "*!\n_Welcome to bittrex price bot, this bot gives the price of cryptocurrency pair from bittrex in real time,try sending me a valid pair e.g btc-ltc_\n /help *incase you need help* "
    bot.send_message(message.chat.id,welcome,parse_mode='Markdown')

@bot.message_handler(commands=['help'])
def send_help(message):
    username=message.from_user.first_name
    help="Hi *" + username + "* ! \nthis bot sends you crypto market stats from various exchanges.\n*#BITTREX* _\nto get altcoin stats from bittrex send a crypto pair_ *e.g btc-eth* \n "
    help=help + "*\n#ZEBPAY* _\nto get price of_ * btc,ltc,bch,xrp,eth* _from zebpay in inr send_ \n/zebpay btc \n/zebpay ltc \n/zebpay bch\n/zebpay xrp\n/zebpay eth"
    bot.send_message(message.chat.id,help,parse_mode='Markdown')

@bot.message_handler(commands=['zebpay'])
def compare_price(message):
    url = "https://www.zebapi.com/api/v1/market/ticker-new/"
    try:
        currency=message.text.strip("/zebpay")
        currency=currency.strip()
        if len(currency) !=0:
            url=url + currency + "/inr"
            response = requests.get(url)
            zebticker ="*buy price:* " + "_"+str(response.json()['buy'])+"_"+ " inr" +"*\nsell price:* " + "_" + str(response.json()['sell'])+ "_"
            zebticker=zebticker + " inr" + "*\nVolume:* " + "_" + str(response.json()['volume'])+"_"+currency
            bot.send_message(message.chat.id,zebticker,parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id,"_please follow the format_ \n e.g /zebpay ltc\n _or try using_ /help",parse_mode='Markdown')
    except Exception:
        print(Exception)
        bot.send_message(message.chat.id,"*invalid currency*,\nplease try /help",parse_mode='Markdown')

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
            text="#"+str(coin[1].upper()) +"\n*Last Price:* "+"_"+str(response["result"][0]['Last'])+"_ " + str(coin[0]) + "*\nHigh:* _" + str(response["result"][0]['High']) +"_ *\nLow:* _" + str(response["result"][0]['Low']) + "_ *\nVolume:* _" + str(response["result"][0]['Volume']) +"_"
            bot.send_message(chatid,text,parse_mode='Markdown')
        else:
            print("success:false");
            text="Invalid pair entered,please try again! or use /help"
            bot.send_message(chatid,text,parse_mode='Markdown')
    except Exception:
        print(Exception)
        print("your internet is broken :( please try again!")


while True:
    try:
    	bot.polling()
    except Exception:
        time.sleep(10)
















# import telebot

# bot = telebot.TeleBot("477501756:AAFW8vtaZyVe3qF9r-YJqWLFax_ru33-XCM")

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

# bot.polling()
















