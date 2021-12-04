import telebot 
import config
import random

from telebot import types 

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

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Здраствуй господин, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот сделанный чтобы служить господину".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Как дела?':
			bot.send_message(message.chat.id, 'Олтично сэмпай)сам как?')

			sti2 = open('menhera_watsup.webp.', 'rb')
			bot.send_sticker(message.chat.id, sti2)
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
		
		else:
			bot.send_message(message.chat.id, 'Я не понимаю вас,сэмпай!')
			sti = open('menhera_what.webp', 'rb')
			bot.send_sticker(message.chat.id, sti)


# RUN
bot.polling(none_stop=True)