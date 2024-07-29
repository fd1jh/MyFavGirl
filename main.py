#подключение библеотек и импорт
import telebot
import webbrowser
from telebot import types
import datetime
#подключение к боту через токен
bot = telebot.TeleBot('7322318827:AAFA4GIi0Esfhb_CYCcfbbayymkGs3JhvOk')
#ответ бота на фото
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton('Получить сердечко', callback_data='get')
    btn2=types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    markup.row(btn1, btn2)
    bot.reply_to(message, 'Какая красивая! А если ты всё-таки подлая и специально скинула чужую фотку то жми на кнопку "Удалить фото"! Ну а если нет, то жми на кнопку "Получить сердечко"', reply_markup=markup)
#перехват значений delete, edit и выполнение функций
@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'get':
        bot.send_message(callback.message.chat.id, 'Вот сердечко для тебя, дороточка!' )
        bot.send_message(callback.message.chat.id, '❤️')
#ответ бота на команды связанные с сайтом
'''@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://itproger.com')'''
#ответ бота на команду start
@bot.message_handler(commands=['start'])
def start(message):
    '''markup1 = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup1.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup1.row(btn2, btn3)
    file=open('./screenshot.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup1)'''
    #bot.send_message(message.chat.id, f'Привет!, {message.from_user.username}', reply_markup=markup1)
    bot.send_message(message.chat.id, '👋')
    bot.send_message(message.chat.id, 'Привет, дороточка! Это явно не то, о чём ты думала, когда я говорил о том, что что-то делаю, я знаю, что уже делал тебе такое, но сейчас я попробовал сделать лучше прошлых разов. Хоть и функционал снова скромный, я надеюсь тебе понравится. Ты можешь нажать на три палочки слева внизу либо воспользоваться командой /help,чтобы узнать, что ты можешь сделать😊')
    #bot.register_next_step_handler(message, on_click)
#функция для реакции на нажатие (только одно без последующих т к написана только 1 функция
'''def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id,'Вы перешли на сайт😘')'''
# ответ бота на команду help (список возможных команд)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Ты можешь использовать эти команды: /text - отправить тебе милый текст /photo - отправить тебе фото самой красивой девочки на свете /video - отправить тебе видео, которое я сделал в тот же день, что и этого бота /time - узнать сколько времени мы вместе /reasons - три причины, по которым я тебя люблю. Такаже ты можешь отправить мне свою фотку и увидеть мою реакцию, написать слово, которое ты используешь очень часто, и, если ты угадаешь его, я тебе отвечу на него', parse_mode='html')

@bot.message_handler(commands=['text'])
def text(message):
    bot.send_message(message.chat.id, 'Моя милая и любимая девочка, я так тебя люблю, твои прекрасные глазки заставляют влюбляться и всматриваться в них вечно, а твои чудесные волосики трогать их и ощущать, будто на твоей руке не волосы, а что-то неземное, твоя улыбка и твой смех завораживают, тобой можно любоваться вечно, но кроме этого ты сама по себе прекрасна, ты самая добрая, самая ласковая и самая волшебная девочка на свете, таких как ты попросту нет и не будет, я люблю тебя каждым кусочком своего сердца и надеюсь, что ты чувствуешь тоже самое❤️❤️❤️')
@bot.message_handler(commands=['photo'])
def photo_send(message):
    file=open('./photo.JPG', 'rb')
    bot.send_photo(message.chat.id, file)
    bot.send_message(message.chat.id, 'Вот одна из фоток самой красивой девочки на свете')
@bot.message_handler(commands=['video'])
def video(message):
    file_v=open('./video.MP4', 'rb')
    bot.send_video(message.chat.id, file_v)
@bot.message_handler(commands=['time'])
def time(message):
    now=datetime.datetime.now()
    old=datetime.datetime(year=2022, month=7, day=23)
    total=now-old
    bot.send_message(message.chat.id, f'Время с момента начала наших отношений: {total} seconds ')
@bot.message_handler(commands=['reasons'])
def reasons(message):
    bot.send_message(message.chat.id, '1. Ты')
    bot.send_message(message.chat.id, '2. Самая')
    bot.send_message(message.chat.id, '3. Лушая!')
    bot.send_message(message.chat.id, '🤗')
#ответ бота на конкретное сообщение
@bot.message_handler()
def info(message):
    if message.text.lower() == 'пр':
        bot.send_message(message.chat.id, 'Пр, моя самая любимая девочка!💋')
    elif message.text.lower() == 'ты меня не любишь':
        bot.send_message(message.chat.id, 'Люблю, наглач!😡💋')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_message(message.chat.id, 'И я тебя, котеночек💋💋💋')

#бесконечная работа кода
bot.polling(none_stop=True)