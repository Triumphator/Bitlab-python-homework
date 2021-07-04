import telebot
import os
import random

bot = telebot.TeleBot("1824989667:AAF1t67SNKZkYA65g_pcLy94IzOVaEA2GxI")


def log(message):
    print("\n ------------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))


@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    # переменная, которая хранит разметку нашей клавиатуры
    # 1 - True - для того,чтобы сделать размер клавиатуры поменьше, False - побольше
    # 2 - True - убрать клавиатуру после одного раза пользования
    user_markup.row('/start', '/stop')  # добавляем команды
    user_markup.row('фото', 'аудио', 'документы')  # и ограничиваем размер клавиатуры 3х4
    user_markup.row('стикер', 'видео', 'голос', 'локация')
    # перед тем, как показать клавиатуру пользователю бот должен отправить сообщение вроде приветствия
    bot.send_message(message.from_user.id, 'Давай, удиви меня', reply_markup=user_markup)
    log(message)


@bot.message_handler(commands=["stop"])
def handle_start(message):  # функция, которая убирает нашу клавиатуру
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '...', reply_markup=hide_markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'фото':
        #directory = 'H:/Obmen/WoW media/Fan art'
        directory = 'H:/My Pictures/Game Art/Red Alert 3'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'аудио':
        #audio = open("H:/Music/Bachata/Xtreme - We Got Next/01. Te Extraño.mp3", 'rb')
        audio = open("H:/Music/Bachata/Xtreme - We Got Next/01. Te Extraño.mp3", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()

    elif message.text == 'документы':
        #directory = 'H:/Obmen/WoW media/Compositions/WarCraft III'
        directory = 'H:/Reserv/SAM
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)

        for files in all_files_in_directory:
            document = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()


    elif message.text == 'локация':
        bot.send_chat_action(message.from_user.id, 'upload_location')
        bot.send_location(message.from_user.id, 42.2129150703383, 80.17346477808603)

@bot.message_handler(content_types=["text"])

def handle_text(message):
    answer = "Извините, я еще не научился отвечать на такие сложные сообщения"
    if message.text.lower() == "привет":
        answer = "Приветствую"
        bot.send_message(message.chat.id, answer)
        log(message)

    elif message.text.lower() == "как дела?":
        answer = "Хорошо,как у тебя?"
        bot.send_message(message.chat.id, answer)
        log(message)

    elif message.text.lower() == "хорошо":
        answer = "Классно, хорошего дня"
        bot.send_message(message.chat.id, answer)
        log(message)

    else:
        bot.send_message(message.chat.id, answer)
        log(message)

bot.polling(none_stop=True, interval=0)
