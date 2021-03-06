import telebot 
import config
import random
import requests

from bs4 import BeautifulSoup
from telebot import types 

url = 'https://anekdotov.net/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='anekdot')

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti1 = open('menhera_hello.webp', 'rb')
	bot.send_sticker(message.chat.id, sti1)

	# KEYBOARD
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Как дела?")
	item2 = types.KeyboardButton("Может сыграем в игру?")
	item3 = types.KeyboardButton("Раскажи цитату от Симы)")
	item4 = types.KeyboardButton("Раскажи анекдот")

	markup.add(item1, item2, item4)

	bot.send_message(message.chat.id, "Здраствуй господин, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот сделанный чтобы служить господину".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Как дела?':
			bot.send_message(message.chat.id, 'Олтично сэмпай)сам как?')

			sti2 = open('menhera_watsup.webp.', 'rb')
			bot.send_sticker(message.chat.id, sti2)
		elif message.text == 'Нормально':
			sti5 = open('menhera_boo.webp.', 'rb')
			bot.send_message(message.chat.id, 'А почему не олтично?Все должно быть олтично,Сэмпай!!!')
			bot.send_sticker(message.chat.id, sti5)

		elif message.text == 'Может сыграем в игру?':
			bot.send_message(message.chat.id, 'Загадайте число до 100 и напишите "загадал",я попробую угадать')
		elif message.text == 'загадал':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
			bot.send_message(message.chat.id, 'Я угадала?')
		elif message.text == 'да':
					bot.send_message(message.chat.id, 'Ураа!!!')

		elif message.text == 'Да':
					bot.send_message(message.chat.id, 'Ураа!!!')

		elif message.text == 'нет':
					bot.send_message(message.chat.id, 'Жаль(')

		elif message.text == 'Нет':
					bot.send_message(message.chat.id, 'Жаль(')

		elif message.text == 'Раскажи цитату от Симы)':
			bot.send_message(message.chat.id, 'В🥵 жизни 💗как😈и☺️в💋 шахматах 😭 потерял💍 королеву 😂 теперь 😜 наслаждайся 💩пешками🤢')
		
		elif message.text == 'Ты мне нравишься':
			sti3 = open('lena.webp', 'rb')
			bot.send_sticker(message.chat.id, sti3)
		
		elif message.text == 'JoJo':
			sti4 = open('pngwing.com.webp', 'rb')
			bot.send_sticker(message.chat.id, sti4)
		
		elif message.text == 'jojo':
			sti4 = open('pngwing.com.webp', 'rb')
			bot.send_sticker(message.chat.id, sti4)
		
		elif message.text == 'Jojo':
			sti4 = open('pngwing.com.webp', 'rb')
			bot.send_sticker(message.chat.id, sti4)
		
		elif message.text == 'привет':
			bot.send_message(message.chat.id, 'Приветик, сэмпай)')
		
		elif message.text == 'Привет':
			bot.send_message(message.chat.id, 'Приветик, сэмпай)')
		
		elif message.text == 'приветик':
			bot.send_message(message.chat.id, 'Приветик, сэмпай)')
		
		elif message.text == 'Приветик':
			bot.send_message(message.chat.id, 'Приветик, сэмпай)')
		elif message.text == 'Раскажи анекдот':
			for allquotes in random.choice(quotes):
				bot.send_message(message.chat.id, (allquotes.text))
		elif message.text == '♂️Boss of this Gym♂️':
			sti6 = open('billy_head.webp', 'rb')
			sti7 = open('billy_body.webp', 'rb')
			sti8 = open('billy.leg.webp', 'rb')
			bot.send_message(message.chat.id, '♂️Ass We Can♂')
			bot.send_sticker(message.chat.id, sti6)
			bot.send_sticker(message.chat.id, sti7)
			bot.send_sticker(message.chat.id, sti8)
		else:
			bot.send_message(message.chat.id, 'Я не понимаю вас,сэмпай!')
			sti = open('menhera_what.webp', 'rb')
			bot.send_sticker(message.chat.id, sti)


# RUN
bot.polling(none_stop=True)