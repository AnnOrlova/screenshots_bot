import telebot
from telebot import types
import random
from random import choice


bot = telebot.TeleBot('6241785570:AAEDRkG-3S3U9fiKqrhGi7ocwZuPnloOJF0')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Профиль и регистрация')
    btn2 = types.KeyboardButton('Меню')
    btn3 = types.KeyboardButton('Адрес')
    btn4 = types.KeyboardButton('Корзина')
    btn5 = types.KeyboardButton('Заказ')
    btn6 = types.KeyboardButton('Скидка сотрудника')
    btn7 = types.KeyboardButton('Тестовая группа')
    btn8 = types.KeyboardButton('Замены')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Профиль и регистрация':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Бонусы при регистрации')
    btn2 = types.KeyboardButton('Выход')
    btn3 = types.KeyboardButton('Изменить промик')
    btn4 = types.KeyboardButton('Имя')
    btn5 = types.KeyboardButton('Заказы')
    btn6 = types.KeyboardButton('Пропустить номер при регистрации')
    btn7 = types.KeyboardButton('Кол-во бонусов')
    btn8 = types.KeyboardButton('Личный промик')
    btn9 = types.KeyboardButton('Оферта')
    btn10 = types.KeyboardButton('Сколько сделать заказов по КМ')
    btn11 = types.KeyboardButton('Способы оплаты')
    btn12 = types.KeyboardButton('Удалить аккаунт')
    btn13 = types.KeyboardButton('Удалить карту')
    btn14 = types.KeyboardButton('Фото')
    btn15 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)

    if message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Профиль и регистрация')
    btn2 = types.KeyboardButton('Меню')
    btn3 = types.KeyboardButton('Адрес')
    btn4 = types.KeyboardButton('Корзина')
    btn5 = types.KeyboardButton('Заказ')
    btn6 = types.KeyboardButton('Скидка сотрудника')
    btn7 = types.KeyboardButton('Тестовая группа')
    btn8 = types.KeyboardButton('Замены')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    if message.text == 'Бонусы при регистрации':
        bot.send_photo(photo.from_user.id, photo='https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8295a0a1-c467-47dd-affb-a18b08dfe372/%D0%91%D0%BE%D0%BD%D1%83%D1%81%D1%8B_%D0%BF%D1%80%D0%B8_%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T085938Z&X-Amz-Expires=86400&X-Amz-Signature=7177fa9def2b7747f62b01cbb4aa0312642890112d87addfea85987b14736929&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%2591%25D0%25BE%25D0%25BD%25D1%2583%25D1%2581%25D1%258B%2520%25D0%25BF%25D1%2580%25D0%25B8%2520%25D1%2580%25D0%25B5%25D0%25B3%25D0%25B8%25D1%2581%25D1%2582%25D1%2580%25D0%25B0%25D1%2586%25D0%25B8%25D0%25B8.jpg%22&x-id=GetObject')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Выход':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3a870902-b0f0-4214-b707-295e5e8790d2/%D0%92%D1%8B%D1%85%D0%BE%D0%B4_%D0%B8%D0%B7_%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T090240Z&X-Amz-Expires=86400&X-Amz-Signature=051ffdbe4021cf5cdb2416cd765a904e859cac57e847da32724c3abc3318c439&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%2592%25D1%258B%25D1%2585%25D0%25BE%25D0%25B4%2520%25D0%25B8%25D0%25B7%2520%25D0%25BF%25D1%2580%25D0%25B8%25D0%25BB%25D0%25BE%25D0%25B6%25D0%25B5%25D0%25BD%25D0%25B8%25D1%258F.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → экран личного профиля → раздел Настройки → кнопка Выйти')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Изменить промик':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/80542a33-7312-46a0-b496-f3dfb6e33e42/IMAGE_2021-03-01_103610.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T090558Z&X-Amz-Expires=86400&X-Amz-Signature=90f2d05bd8a2327f2a65ef8a5f3736daca57113957e8ed2f303ef66903cfddd1&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22IMAGE_2021-03-01_103610.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → экран личного профиля → раздел Бонусы → рядом с названием промокода нажать на карандашик')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Имя':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6dec203e-2326-4f6b-a3c8-cbacadf4abf4/%D0%98%D0%BC%D1%8F.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T090756Z&X-Amz-Expires=86400&X-Amz-Signature=5ddf9d74f26501e936b71c20681db9cb15b537a884ce001c16c4e964178830ca&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%2598%25D0%25BC%25D1%258F.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата, чтобы перейти в Профиль. Затем нажать на имя или Настройки → добавить или изменить имя в поле «Как вас зовут»')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Заказы':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c652ed88-7e7c-435c-8d18-dc947f098caa/%D0%97%D0%B0%D0%BA%D0%B0%D0%B7%D1%8B.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T091019Z&X-Amz-Expires=86400&X-Amz-Signature=10357b24e5283fd487f9bd157c022a581073599786f48d7dcce7e73abd0739cf&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%2597%25D0%25B0%25D0%25BA%25D0%25B0%25D0%25B7%25D1%258B.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата, чтобы перейти в Профиль. Далее выбрать раздел Заказы')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Пропустить номер при регистрации':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8734ec08-7320-4bd5-a7ea-66d734937758/IMG_9012.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T091239Z&X-Amz-Expires=86400&X-Amz-Signature=20ed5a4dc106c3ddc10aa8be72b5e0e29645c2f14ea10074d5c1f51e034b4cdd&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22IMG_9012.PNG.png%22&x-id=GetObject')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Кол-во бонусов':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d7f73d53-0180-4cf6-bd38-70a232059ada/%D0%9A%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE_%D0%B1%D0%BE%D0%BD%D1%83%D1%81%D0%BE%D0%B2_%D0%B2_%D0%BF%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D0%B5.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T091409Z&X-Amz-Expires=86400&X-Amz-Signature=64bfd1db59890a28777c2efef95cc56c11fb19cc49cea11b7d70f1a7bfc739f3&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%259A%25D0%25BE%25D0%25BB%25D0%25B8%25D1%2587%25D0%25B5%25D1%2581%25D1%2582%25D0%25B2%25D0%25BE%2520%25D0%25B1%25D0%25BE%25D0%25BD%25D1%2583%25D1%2581%25D0%25BE%25D0%25B2%2520%25D0%25B2%2520%25D0%25BF%25D1%2580%25D0%25BE%25D1%2584%25D0%25B8%25D0%25BB%25D0%25B5.jpeg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу и перейти в раздел Бонусы')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Личный промик':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/204dbef6-86c9-4238-af0e-db5044c4136f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T091643Z&X-Amz-Expires=86400&X-Amz-Signature=d45cfb52b898f3a0424e63e612f3983a7a05ef8149723d78af8837d476f82841&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → экран личного профиля → раздел Бонусы → А вот ваш код')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Оферта':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8a889394-18a8-4213-bdcf-482b53a7d105/%D0%9E%D1%84%D0%B5%D1%80%D1%82%D0%B0.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T091910Z&X-Amz-Expires=86400&X-Amz-Signature=8b005de13ba5cfd93b083b2c94e81d3ba7408e5ef7ac71272b22dc55052d4257&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%259E%25D1%2584%25D0%25B5%25D1%2580%25D1%2582%25D0%25B0.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата, чтобы перейти в Профиль. В нижнем правом углу будет ссылка на Оферту ')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Сколько сделать заказов по КМ':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e095e95f-8fca-49c1-80f6-c620616cee38/%D0%A1%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE_%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C_%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7%D0%BE%D0%B2_%D0%B4%D0%BB%D1%8F_%D0%BD%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%B1%D0%BE%D0%BD%D1%83%D1%81%D0%BE%D0%B2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T092509Z&X-Amz-Expires=86400&X-Amz-Signature=f0f5a2bd3a7e6d112d45828c8e6cedee4900abdb354ff481f59c95a6823cbd67&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25A1%25D0%25BA%25D0%25BE%25D0%25BB%25D1%258C%25D0%25BA%25D0%25BE%2520%25D1%2581%25D0%25B4%25D0%25B5%25D0%25BB%25D0%25B0%25D1%2582%25D1%258C%2520%25D0%25B7%25D0%25B0%25D0%25BA%25D0%25B0%25D0%25B7%25D0%25BE%25D0%25B2%2520%25D0%25B4%25D0%25BB%25D1%258F%2520%25D0%25BD%25D0%25B0%25D1%2587%25D0%25B8%25D1%2581%25D0%25BB%25D0%25B5%25D0%25BD%25D0%25B8%25D1%258F%2520%25D0%25B1%25D0%25BE%25D0%25BD%25D1%2583%25D1%2581%25D0%25BE%25D0%25B2.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата, чтобы перейти в Профиль.')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Способы оплаты':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2fab8ef8-069b-4fa3-8dbc-c8ec64f2da51/%D0%A1%D0%BF%D0%BE%D1%81%D0%BE%D0%B1_%D0%BE%D0%BF%D0%BB%D0%B0%D1%82%D1%8B_%D0%B2_%D0%BF%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D0%B5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T092638Z&X-Amz-Expires=86400&X-Amz-Signature=e49d11c2fd5abc40850a3f5d00c63ac25284daeb39bc09c44e143ba79159e494&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25A1%25D0%25BF%25D0%25BE%25D1%2581%25D0%25BE%25D0%25B1%2520%25D0%25BE%25D0%25BF%25D0%25BB%25D0%25B0%25D1%2582%25D1%258B%2520%25D0%25B2%2520%25D0%25BF%25D1%2580%25D0%25BE%25D1%2584%25D0%25B8%25D0%25BB%25D0%25B5.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата → Способы оплаты внизу экрана')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Удалить аккаунт':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8ebe2514-d451-4b8e-b708-315735e4f07e/%D0%A3%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D0%B0.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T092834Z&X-Amz-Expires=86400&X-Amz-Signature=3a9d875e1fa8b6c7761afa7fe7c01621fcbd9dd3f9e7784b941e5214981a9912&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25A3%25D0%25B4%25D0%25B0%25D0%25BB%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5%2520%25D0%25B0%25D0%25BA%25D0%25BA%25D0%25B0%25D1%2583%25D0%25BD%25D1%2582%25D0%25B0.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата, чтобы перейти в профиль. Затем Настройки → Удалить аккаунт')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Удалить карту':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fb5b135f-fdb9-4ebf-a3e8-57808b9c9bd2/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T093031Z&X-Amz-Expires=86400&X-Amz-Signature=a6552420ab4032c5f2cdd193575a756697ceeb5a00d58b31cbd0cbb59af7a4ec&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.jpeg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → экран личного профиля → Способы оплаты. Далее нужно выбрать карту, свайпнуть ее влево и нажать на значок с корзиной')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Фото':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ed7ffc62-213a-4027-aaaf-ff9d5a0a2cce/%D0%A4%D0%BE%D1%82%D0%BE.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T093222Z&X-Amz-Expires=86400&X-Amz-Signature=65acae8d8c0bd44bdda43c2544beade04fd67e2baebcd96ee883b02bd092094a&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25A4%25D0%25BE%25D1%2582%25D0%25BE.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на изображение профиля или значок человечка/фотоаппарата → нажать на имя или Настройки → нажать на фото → сделать снимок или выбрать из галереи')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Бонусы при регистрации')
    btn2 = types.KeyboardButton('Выход')
    btn3 = types.KeyboardButton('Изменить промик')
    btn4 = types.KeyboardButton('Имя')
    btn5 = types.KeyboardButton('Заказы')
    btn6 = types.KeyboardButton('Пропустить номер при регистрации')
    btn7 = types.KeyboardButton('Кол-во бонусов')
    btn8 = types.KeyboardButton('Личный промик')
    btn9 = types.KeyboardButton('Оферта')
    btn10 = types.KeyboardButton('Сколько сделать заказов по КМ')
    btn11 = types.KeyboardButton('Способы оплаты')
    btn12 = types.KeyboardButton('Удалить аккаунт')
    btn13 = types.KeyboardButton('Удалить карту')
    btn14 = types.KeyboardButton('Фото')
    btn15 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)

    if message.text == 'Меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('КБЖУ блюда')
    btn2 = types.KeyboardButton('Состав')
    btn3 = types.KeyboardButton('Теги')
    btn4 = types.KeyboardButton('Добавить к завтраку')
    btn5 = types.KeyboardButton('Соусы')
    btn6 = types.KeyboardButton('Раздел Вы заказывали')
    btn7 = types.KeyboardButton('Верхняя навигация')
    btn8 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    if message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Профиль и регистрация')
    btn2 = types.KeyboardButton('Меню')
    btn3 = types.KeyboardButton ('Адрес')
    btn4 = types.KeyboardButton ('Корзина')
    btn5 = types.KeyboardButton ('Заказ')
    btn6 = types.KeyboardButton ('Скидка сотрудника')
    btn7 = types.KeyboardButton ('Тестовая группа')
    btn8 = types.KeyboardButton ('Замены')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)
        
    if message.text == 'КБЖУ блюда':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d92bc805-098b-40f7-9f9f-cfffc2c522d6/IMG_9022.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T104845Z&X-Amz-Expires=86400&X-Amz-Signature=50bef66367b14703e1612dc4b4e58eeace67b1829d942ba8bee6b419dde0a47f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22IMG_9022.PNG.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на блюдо, откроется карточка с информацией. КБЖУ указан под составом')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Состав':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/11cdd6be-6662-4833-961e-39547c8ac82d/%D1%81%D0%BE%D1%81%D1%82%D0%B0%D0%B2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T105041Z&X-Amz-Expires=86400&X-Amz-Signature=6ee3e03d8a9fe968d345f3113cb65b8281bd1dfe3992e171b6b583dc78e727eb&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D1%2581%25D0%25BE%25D1%2581%25D1%2582%25D0%25B0%25D0%25B2.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на блюдо и пролистать экран вниз')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Теги':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/96f3696a-8446-40c1-a8d7-acb7d8ad955b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T105243Z&X-Amz-Expires=86400&X-Amz-Signature=4f66b0d001091b0452afd6c99a5344b4661268abe59b68c7727fec1c8e87b1a3&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject')
    bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c486b959-cfa7-4341-9ddf-3f4cf2361e95/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T105313Z&X-Amz-Expires=86400&X-Amz-Signature=9c90f7da278e7d1e24d9c0ee4fa95857d2312f30fb73dc7943fb40fe1ff4beb5&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject')
    bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5dde0770-84bb-4307-b4f7-dba24b4dc4da/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T105340Z&X-Amz-Expires=86400&X-Amz-Signature=bfde5b876681db21b4b2a53bb362bc82265ebf55c05d8ae8f626ad6988d4525c&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно нажать на блюдо. Под названием указан тег: 🌱 — веганское, 🥦 — вегетарианское, 🐧 — холодное, 🌶 — острое')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Добавить к завтраку':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2acbdd01-fee5-4f29-9666-4b979fd018b6/IMG_9026.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T105722Z&X-Amz-Expires=86400&X-Amz-Signature=968834105492760fe5af924464b84f52d56b75bdac11244d4e28f374284c722f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22IMG_9026.PNG.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Пролистать верхнюю навигацию с разделами меню влево, найти и нажать на кнопку «Добавить к завтраку». Затем в одноименном разделе выбрать нужную позицию')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Соусы':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/20082158-993f-446d-8f9f-59c13d4813e5/IMG_9028.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T105914Z&X-Amz-Expires=86400&X-Amz-Signature=a9f690e35e3a07aeee08f02e8f7ac9f4f6f79ed83e2e14467c74c4611c285a87&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22IMG_9028.PNG.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Пролистать верхнюю навигацию с разделами меню влево, найти и нажать на кнопку «Соусы». Затем в одноименном разделе выбрать нужный')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Раздел Вы заказывали':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b623fbf9-5049-4023-8395-5a6ae4fff2f8/%D0%B2%D1%8B_%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%BB%D0%B8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T110049Z&X-Amz-Expires=86400&X-Amz-Signature=e646236eefb8c497c9e15ce918bf0c3bb027b5e00644fb20d466bfa4f1c55de9&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25B2%25D1%258B%2520%25D0%25B7%25D0%25B0%25D0%25BA%25D0%25B0%25D0%25B7%25D1%258B%25D0%25B2%25D0%25B0%25D0%25BB%25D0%25B8.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Раздел находится на экране с меню под адресом')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Верхняя навигация':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d81b2f40-97a5-4d72-9ba7-6e8d58899fc2/%D0%B2%D0%B5%D1%80%D1%85%D0%BD%D1%8F%D1%8F_%D0%BD%D0%B0%D0%B2%D0%B8%D0%B3%D0%B0%D1%86%D0%B8%D1%8F.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T110437Z&X-Amz-Expires=86400&X-Amz-Signature=8e52ce1e68f615da732eb616c0dd4a6950c3acd6a58b156f9f36cad081a0a15f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25B2%25D0%25B5%25D1%2580%25D1%2585%25D0%25BD%25D1%258F%25D1%258F%2520%25D0%25BD%25D0%25B0%25D0%25B2%25D0%25B8%25D0%25B3%25D0%25B0%25D1%2586%25D0%25B8%25D1%258F.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Чтобы появилась навигация, нужно опустить экран меню чуть ниже')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('КБЖУ блюда')
    btn2 = types.KeyboardButton('Состав')
    btn3 = types.KeyboardButton('Теги')
    btn4 = types.KeyboardButton('Добавить к завтраку')
    btn5 = types.KeyboardButton('Соусы')
    btn6 = types.KeyboardButton('Раздел Вы заказывали')
    btn7 = types.KeyboardButton('Верхняя навигация')
    btn8 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)

    if message.text == 'Адрес':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Первый адрес')
    btn2 = types.KeyboardButton('Изменить адрес')
    btn3 = types.KeyboardButton('Добавить еще один адрес')
    btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
    btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
    btn6 = types.KeyboardButton('Удалить адрес')
    btn7 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    if message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Профиль и регистрация')
    btn2 = types.KeyboardButton('Меню')
    btn3 = types.KeyboardButton ('Адрес')
    btn4 = types.KeyboardButton ('Корзина')
    btn5 = types.KeyboardButton ('Заказ')
    btn6 = types.KeyboardButton ('Скидка сотрудника')
    btn7 = types.KeyboardButton ('Тестовая группа')
    btn8 = types.KeyboardButton ('Замены')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)
        
    if message.text == 'Первый адрес':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ac27689b-2c67-40b1-a9dc-9c274a01d160/%D0%9F%D0%B5%D1%80%D0%B2%D1%8B%D0%B9_%D0%B0%D0%B4%D1%80%D0%B5%D1%81.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T112804Z&X-Amz-Expires=86400&X-Amz-Signature=a28f04f87a62b1f189c38465a13ffacd655d5a87279bb0fc8aeaacdd4c655ad6&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%259F%25D0%25B5%25D1%2580%25D0%25B2%25D1%258B%25D0%25B9%2520%25D0%25B0%25D0%25B4%25D1%2580%25D0%25B5%25D1%2581.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Значок карандаша → поле ввода → кнопка «Везите сюда»')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Изменить адрес':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ee530b8a-03b1-48e9-a2cf-4a71025b393e/image_%285%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T112936Z&X-Amz-Expires=86400&X-Amz-Signature=a784bc0c27ed78fa2dcd3e87afcb00f97a7bd23b1c4d50628b5d4600e4aebe3b&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22image%2520%285%29.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать на значок карандаша на главном экране → выбрать нужный адрес из списка')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)
        
    if message.text == 'Добавить еще один адрес':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ab702884-cbeb-4c0e-b724-d764e49ad5ef/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C_%D0%B5%D1%89%D0%B5_%D0%B0%D0%B4%D1%80%D0%B5%D1%81.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T113055Z&X-Amz-Expires=86400&X-Amz-Signature=dab3ecc8684896562808600efc3f4fa3c1bc2888594ccbfb59abbeb152e08dfd&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%2594%25D0%25BE%25D0%25B1%25D0%25B0%25D0%25B2%25D0%25B8%25D1%2582%25D1%258C%2520%25D0%25B5%25D1%2589%25D0%25B5%2520%25D0%25B0%25D0%25B4%25D1%2580%25D0%25B5%25D1%2581.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Экран меню → значок карандаша → кнопка «Новый адрес» → кнопка «Везите сюда»')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)
        
    if message.text == 'Изменить комментарий(один адрес)':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/929df379-3fbb-4f33-8003-7adfeadefcf4/%D0%98%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C_%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82_1_%D0%B0%D0%B4%D1%80%D0%B5%D1%81.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T113220Z&X-Amz-Expires=86400&X-Amz-Signature=11d9ccbf2c9355c823e773ec0774ad1cf3fab31ca8b02bbb8284ed8fd74812b8&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%2598%25D0%25B7%25D0%25BC%25D0%25B5%25D0%25BD%25D0%25B8%25D1%2582%25D1%258C%2520%25D0%25BA%25D0%25BE%25D0%25BC%25D0%25BC%25D0%25B5%25D0%25BD%25D1%2582%25201%2520%25D0%25B0%25D0%25B4%25D1%2580%25D0%25B5%25D1%2581.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Дважды нажать на значок карандаша в правом верхнем углу → поле комментария → Готово')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Изменить комментарий (2 и более адресов)':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/86fc65dc-ed92-4317-ba03-6c3169f4ce61/image_%2811%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T113346Z&X-Amz-Expires=86400&X-Amz-Signature=10e7429a807c929acdd1992397a22928e263650ed9ae1f988ca49323d5fc3cc2&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22image%2520%2811%29.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Дважды нажать на значок карандаша в правом верхнем углу → поле комментария → Готово')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Удалить адрес':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/efd49b2f-72b3-4bd0-a8cd-45a69140fd4a/%D0%A3%D0%B4%D0%B0%D0%BB%D0%B8%D1%82%D1%8C_%D0%B0%D0%B4%D1%80%D0%B5%D1%81.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T113558Z&X-Amz-Expires=86400&X-Amz-Signature=64f24954cc707df27a560a42f48bafa539818bc90f6a36e43f590420f35b300f&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25A3%25D0%25B4%25D0%25B0%25D0%25BB%25D0%25B8%25D1%2582%25D1%258C%2520%25D0%25B0%25D0%25B4%25D1%2580%25D0%25B5%25D1%2581.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → экран личного профиля → раздел Адреса → значок карандаша → нажать на минус рядом с адресом, который хотите удалить → затем «Готово»')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Первый адрес')
    btn2 = types.KeyboardButton('Изменить адрес')
    btn3 = types.KeyboardButton('Добавить еще один адрес')
    btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
    btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
    btn6 = types.KeyboardButton('Удалить адрес')
    btn7 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    if message.text == 'Корзина':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Добавить приборы')
    btn2 = types.KeyboardButton('Изменить кол-во приборов')
    btn3 = types.KeyboardButton('Оставить у двери')
    btn4 = types.KeyboardButton('Скидка в корзине')
    btn5 = types.KeyboardButton('Сколько оплачено деньгами/бонусами')
    btn6 = types.KeyboardButton('Оплата бонусами')
    btn7 = types.KeyboardButton('Привязать карту')
    btn8 = types.KeyboardButton('Добавить к заказу')
    btn9 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)

    if message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Профиль и регистрация')
    btn2 = types.KeyboardButton('Меню')
    btn3 = types.KeyboardButton ('Адрес')
    btn4 = types.KeyboardButton ('Корзина')
    btn5 = types.KeyboardButton ('Заказ')
    btn6 = types.KeyboardButton ('Скидка сотрудника')
    btn7 = types.KeyboardButton ('Тестовая группа')
    btn8 = types.KeyboardButton ('Замены')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    if message.text == 'Добавить приборы':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fb6004c9-ddac-428d-8906-02304d96b62b/%D0%98%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C_%D0%BF%D1%80%D0%B8%D0%B1%D0%BE%D1%80%D1%8B_%D0%B2_%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D0%B5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T114421Z&X-Amz-Expires=86400&X-Amz-Signature=f38bfd58f7ffa19770706c1e3a150ef239afd7322a15f74564bc6078e5c8478e&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%2598%25D0%25B7%25D0%25BC%25D0%25B5%25D0%25BD%25D0%25B8%25D1%2582%25D1%258C%2520%25D0%25BF%25D1%2580%25D0%25B8%25D0%25B1%25D0%25BE%25D1%2580%25D1%258B%2520%25D0%25B2%2520%25D0%25BA%25D0%25BE%25D1%2580%25D0%25B7%25D0%25B8%25D0%25BD%25D0%25B5.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать темносерую плашку внизу экрана → «+» около позиции «Приборы» после списка блюд ')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Изменить кол-во приборов':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f84df1fb-fe8e-449b-aa80-29fe1af41f96/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C_%D0%BF%D1%80%D0%B8%D0%B1%D0%BE%D1%80%D1%8B.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T114707Z&X-Amz-Expires=86400&X-Amz-Signature=6dfd4bea76e9934a80d80144f5de41876ef13128b504567fcdbb8e7ccf17e1c1&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%2594%25D0%25BE%25D0%25B1%25D0%25B0%25D0%25B2%25D0%25B8%25D1%2582%25D1%258C%2520%25D0%25BF%25D1%2580%25D0%25B8%25D0%25B1%25D0%25BE%25D1%2580%25D1%258B.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать темносерую плашку внизу экрана → «+» или «-» около позиции «Приборы» после списка блюд ')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Оставить у двери':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8c5ce6c4-5735-4776-a03e-8b98410df07f/%D0%9E%D1%81%D1%82%D0%B0%D0%B2%D0%B8%D1%82%D1%8C_%D1%83_%D0%B4%D0%B2%D0%B5%D1%80%D0%B8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T114833Z&X-Amz-Expires=86400&X-Amz-Signature=2785f89932910c7c8254ead487695f4a4c024fc9669de6d1704e6814bead705c&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%259E%25D1%2581%25D1%2582%25D0%25B0%25D0%25B2%25D0%25B8%25D1%2582%25D1%258C%2520%25D1%2583%2520%25D0%25B4%25D0%25B2%25D0%25B5%25D1%2580%25D0%25B8.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'В корзине нужно сдвинуть ползунок «Оставить у двери»')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Скидка в корзине':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6bb676e7-78ba-4781-8ab0-e5a62150cf6b/%D0%A1%D0%BA%D0%B8%D0%B4%D0%BA%D0%B0_%D0%B2_%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D0%B5.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T114951Z&X-Amz-Expires=86400&X-Amz-Signature=149c1d194b8c88f5d2606e776769dcb7d09eeea4b13ac6842c5b126691f3bada&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25A1%25D0%25BA%25D0%25B8%25D0%25B4%25D0%25BA%25D0%25B0%2520%25D0%25B2%2520%25D0%25BA%25D0%25BE%25D1%2580%25D0%25B7%25D0%25B8%25D0%25BD%25D0%25B5.jpeg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'В корзине, над кнопкой «Заказать на», будет указана скидка, ее номинал и стоимость в рублях, которую покрывает ')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Сколько оплачено деньгами/бонусами':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8af65d8e-b031-42f6-9782-21f91ecf3751/image_%284%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T115138Z&X-Amz-Expires=86400&X-Amz-Signature=fb9d7b092773c5ecc7240c841dd97f852f1efd0f29a23314268a6b0226d44c82&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22image%2520%284%29.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'В корзине, над кнопкой «Заказать на», указано, сколько у вас бонусов, какая часть будет оплачена деньгами с их учетом')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Оплата бонусами':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/eb3e87cd-2e86-44e1-9587-5726283cb085/image_%284%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T115254Z&X-Amz-Expires=86400&X-Amz-Signature=6d6071483155f0ac37c34ff18fda5b24947f5cd994ea8876beeeb226052139d4&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22image%2520%284%29.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'В корзине включить ползунок «Оплатить бонусами»')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Привязать карту':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/18d1b160-5301-4aa9-bdd5-aeb7a7a8c5f6/%D0%9F%D1%80%D0%B8%D0%B2%D1%8F%D0%B7%D0%BA%D0%B0_%D0%BD%D0%BE%D0%B2%D0%BE%D0%B9_%D0%BA%D0%B0%D1%80%D1%82%D1%8B.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T115404Z&X-Amz-Expires=86400&X-Amz-Signature=eeabba0d9aa581614e78bbd8026ebd4f1ab5cf2e5c889b85e39f3f783cee3059&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%259F%25D1%2580%25D0%25B8%25D0%25B2%25D1%258F%25D0%25B7%25D0%25BA%25D0%25B0%2520%25D0%25BD%25D0%25BE%25D0%25B2%25D0%25BE%25D0%25B9%2520%25D0%25BA%25D0%25B0%25D1%2580%25D1%2582%25D1%258B.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'В корзине нажать на «Заказать на» → Ввести реквизиты → Нажать «Оплатить»')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Добавить к заказу':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/17aa428b-9e33-4a9c-87dc-d53b2997dae2/IMG_9029.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T115652Z&X-Amz-Expires=86400&X-Amz-Signature=fd2d3cbb659469bad613efdbfebc3858f6a9dd11283c3c5cafffbea29183db74&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22IMG_9029.PNG.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно перейти в корзину и нажать на нужную позицию в разделе Добавить к заказу')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Первый адрес')
    btn2 = types.KeyboardButton('Изменить адрес')
    btn3 = types.KeyboardButton('Добавить еще один адрес')
    btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
    btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
    btn6 = types.KeyboardButton('Удалить адрес')
    btn7 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    if message.text == 'Заказ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Приборы после заказа')
    btn2 = types.KeyboardButton('Сколько оплачено деньгами/бонусами')
    btn3 = types.KeyboardButton('Отменить заказ')
    btn4 = types.KeyboardButton('Донатсы')
    btn5 = types.KeyboardButton('Чек заказа')
    btn6 = types.KeyboardButton('Трекер со статусом заказа')
    btn7 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    if message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Профиль и регистрация')
    btn2 = types.KeyboardButton('Меню')
    btn3 = types.KeyboardButton ('Адрес')
    btn4 = types.KeyboardButton ('Корзина')
    btn5 = types.KeyboardButton ('Заказ')
    btn6 = types.KeyboardButton ('Скидка сотрудника')
    btn7 = types.KeyboardButton ('Тестовая группа')
    btn8 = types.KeyboardButton ('Замены')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    if message.text == 'Приборы после заказа':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/95a9f0d9-8519-4019-9b36-bac54a2c2f15/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T120810Z&X-Amz-Expires=86400&X-Amz-Signature=24790260457105e87bab47324ee553fc144590b2450bfbae3552bf96f0661aff&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.jpeg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать на желтую плашку внизу экрана → Под списком блюд в заказе нажать на «+» справа от приборов → добавить нужное количество → нажать кнопку «Сохранить»')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Сколько оплачено деньгами/бонусами':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/575777db-6df3-4670-adb6-355044d43985/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T120944Z&X-Amz-Expires=86400&X-Amz-Signature=cdeea120eb33ef6200eebb1de6f64b678a0089b069f627241932630bd4110939&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.jpeg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать на значок человечка в левом верхнем углу → экран личного профиля → раздел Заказы → выбрать нужный. В его карточке будет указано, какая сумма была оплачена деньгами и бонусами ')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Отменить заказ':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7e44ad1c-41a5-4446-ae6a-e6772507f6c0/%D0%9E%D1%82%D0%BC%D0%B5%D0%BD%D0%B0_%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T121052Z&X-Amz-Expires=86400&X-Amz-Signature=7ff778b855e0dee97b984dfac4ea58df06791c0db7c8b47f2a266ce088564289&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%259E%25D1%2582%25D0%25BC%25D0%25B5%25D0%25BD%25D0%25B0%2520%25D0%25B7%25D0%25B0%25D0%25BA%25D0%25B0%25D0%25B7%25D0%25B0.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать на желтый трекер заказа в статусе Оплачен, а далее на кнопку «Отменить заказ»')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Донатсы':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/db9c7a2f-854b-4e37-b240-3438f6871d23/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T121207Z&X-Amz-Expires=86400&X-Amz-Signature=7f74bc5891a03d6ece2155758a57fa91da76915cb847c4d57e2c0c7496faecc4&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.jpeg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → раздел Заказы → выбрать нужный → на баннере оценки заказа поставить палец вверх → выбрать или указать сумму → нажать «Отправить»')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Чек заказа':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6de08043-7895-47c4-8ae1-3a1e92e64b9d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T121345Z&X-Amz-Expires=86400&X-Amz-Signature=279530cb95d3170af0d5d2af414278ba17906888b5827498dae74c6b89b35496&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать на изображение профиля или значок человечка/фотоаппарата в левом верхнем углу → раздел Заказы → выбрать нужный → нажать на значок чека в правом верхнем углу')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Трекер со статусом заказа':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3cdc73c4-7246-4936-9399-186f4d7f1616/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T121521Z&X-Amz-Expires=86400&X-Amz-Signature=8bfbd8104d09e3e8647b59c5d7e9918aff4532b17555d7f338bf13590f964c28&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.jpeg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Желтая плашки внизу экрана')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Первый адрес')
    btn2 = types.KeyboardButton('Изменить адрес')
    btn3 = types.KeyboardButton('Добавить еще один адрес')
    btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
    btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
    btn6 = types.KeyboardButton('Удалить адрес')
    btn7 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    if message.text == 'Скидка сотрудника':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Вкл/выкл скидку')
    btn2 = types.KeyboardButton('Сколько оплачено компанией')
    btn3 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3)

    if message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Профиль и регистрация')
    btn2 = types.KeyboardButton('Меню')
    btn3 = types.KeyboardButton ('Адрес')
    btn4 = types.KeyboardButton ('Корзина')
    btn5 = types.KeyboardButton ('Заказ')
    btn6 = types.KeyboardButton ('Скидка сотрудника')
    btn7 = types.KeyboardButton ('Тестовая группа')
    btn8 = types.KeyboardButton ('Замены')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    if message.text == 'Вкл/выкл скидку':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/49a9de6a-0f5b-4e32-acfd-290362ac73d5/KS1.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T121937Z&X-Amz-Expires=86400&X-Amz-Signature=8bc9f87d290a38d007745b981a764f0f1cb52db269a302ccaad4988a2ca67d3a&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22KS1.jpeg%22&x-id=GetObject')
    bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c19cd17c-b9c9-40d3-a5ac-2861ac3fb14b/%D0%A1%D0%9A%D0%98%D0%94%D0%9A%D0%90_%D0%A1%D0%9E%D0%A2%D0%A0%D0%A3%D0%94%D0%9D%D0%98%D0%9A%D0%90_%D0%9A%D0%A3%D0%A5%D0%9D%D0%98.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T122018Z&X-Amz-Expires=86400&X-Amz-Signature=7c6810a50f1d1b6d4470d121b1621263fb9fc7ccac2331fea6e1e6e3c8351c86&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25A1%25D0%259A%25D0%2598%25D0%2594%25D0%259A%25D0%2590%2520%25D0%25A1%25D0%259E%25D0%25A2%25D0%25A0%25D0%25A3%25D0%2594%25D0%259D%25D0%2598%25D0%259A%25D0%2590%2520%25D0%259A%25D0%25A3%25D0%25A5%25D0%259D%25D0%2598.jpeg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нужно выбрать Способы оплаты в Корзине или Профиле и переключить тумблер')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Сколько оплачено компанией':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f46afecf-0df8-4483-86fc-961dd3b50bda/%D0%9A.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T122118Z&X-Amz-Expires=86400&X-Amz-Signature=2c9a1a669c23ff68fdbe0e4068529e70741f8d7b115277370df06de1c3eae436&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%259A.jpeg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Информация отображается в Корзине, сразу под блоком «Добавить к заказу». Там указываем, какую сумму взяла на себя компания, и какую спишем с карты. После оплаты это можно проверить в разделе Заказы')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Первый адрес')
    btn2 = types.KeyboardButton('Изменить адрес')
    btn3 = types.KeyboardButton('Добавить еще один адрес')
    btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
    btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
    btn6 = types.KeyboardButton('Удалить адрес')
    btn7 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    if message.text == 'Тестовая группа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Виджеты бонусов')
    btn2 = types.KeyboardButton('Скидки и бонусы')
    btn3 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3)

    if message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Профиль и регистрация')
    btn2 = types.KeyboardButton('Меню')
    btn3 = types.KeyboardButton ('Адрес')
    btn4 = types.KeyboardButton ('Корзина')
    btn5 = types.KeyboardButton ('Заказ')
    btn6 = types.KeyboardButton ('Скидка сотрудника')
    btn7 = types.KeyboardButton ('Тестовая группа')
    btn8 = types.KeyboardButton ('Замены')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    if message.text == 'Виджеты бонусов':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/962ed14a-6bae-4233-9d0d-4e70ab6ece50/%D0%A1%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE_%D0%BD%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D1%8F%D0%B5%D0%BC.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T122456Z&X-Amz-Expires=86400&X-Amz-Signature=bb57f0dca013ed93d6839df89d35b19935b38d346ad6754958c52f80279785be&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25A1%25D0%25BA%25D0%25BE%25D0%25BB%25D1%258C%25D0%25BA%25D0%25BE%2520%25D0%25BD%25D0%25B0%25D1%2587%25D0%25B8%25D1%2581%25D0%25BB%25D1%258F%25D0%25B5%25D0%25BC.jpg%22&x-id=GetObject')
    bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2e876b45-ca68-4882-84d1-28ec521dcd19/%D0%92%D0%B8%D0%B4%D0%B6%D0%B5%D1%82_%D1%81_%D0%B1%D0%BE%D0%BD%D1%83%D1%81%D0%B0%D0%BC%D0%B8.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T122538Z&X-Amz-Expires=86400&X-Amz-Signature=285f6ef6669b92c942bed729d89cce5ae7d8cbb8c65dabb7185ff9f6eecf1975&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%2592%25D0%25B8%25D0%25B4%25D0%25B6%25D0%25B5%25D1%2582%2520%25D1%2581%2520%25D0%25B1%25D0%25BE%25D0%25BD%25D1%2583%25D1%2581%25D0%25B0%25D0%25BC%25D0%25B8.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'На левом верхнем виджете показываем, сколько бонусов начисляем. По нажатию на виджет можно перейти на лендинг с условиями. На правом верхнем виджете показываем количество бонусов на счете. По нажатию можно перейти в раздел Бонусы')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Скидки и бонусы':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3e73279e-0285-4f87-a4b4-64e24b7b63aa/%D0%A1%D0%BA%D0%B8%D0%B4%D0%BA%D0%B0_%D0%B2_%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D0%B5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T122711Z&X-Amz-Expires=86400&X-Amz-Signature=0086d11898b2853b3cb8c53d97511ede391a45309e4aeec92559d166236e86f6&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25A1%25D0%25BA%25D0%25B8%25D0%25B4%25D0%25BA%25D0%25B0%2520%25D0%25B2%2520%25D0%25BA%25D0%25BE%25D1%2580%25D0%25B7%25D0%25B8%25D0%25BD%25D0%25B5.jpg%22&x-id=GetObject')
    bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f3dc870e-2ac8-4fd9-b0e7-8e2c254d778c/%D0%A1%D1%82%D0%BE%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C_%D0%B7%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0_%D1%81%D0%BE_%D1%81%D0%BA%D0%B8%D0%B4%D0%BA%D0%BE%D0%B9.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T122740Z&X-Amz-Expires=86400&X-Amz-Signature=a852ee0e046fe21259b836de57348246d87c9b34ed515e53c84480824ec6f6ab&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25D0%25A1%25D1%2582%25D0%25BE%25D0%25B8%25D0%25BC%25D0%25BE%25D1%2581%25D1%2582%25D1%258C%2520%25D0%25B7%25D0%25B0%25D0%25BA%25D0%25B0%25D0%25B7%25D0%25B0%2520%25D1%2581%25D0%25BE%2520%25D1%2581%25D0%25BA%25D0%25B8%25D0%25B4%25D0%25BA%25D0%25BE%25D0%25B9.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Скидка в корзине и Сумма заказа с учетом скидки')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Первый адрес')
    btn2 = types.KeyboardButton('Изменить адрес')
    btn3 = types.KeyboardButton('Добавить еще один адрес')
    btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
    btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
    btn6 = types.KeyboardButton('Удалить адрес')
    btn7 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    if message.text == 'Замены':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Выбрать блюдо')
    btn2 = types.KeyboardButton('Сбросить блюдо')
    btn3 = types.KeyboardButton('Выбрать бонусы')
    btn4 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4)

    if message.text == 'Вернуться на главную':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Профиль и регистрация')
    btn2 = types.KeyboardButton('Меню')
    btn3 = types.KeyboardButton ('Адрес')
    btn4 = types.KeyboardButton ('Корзина')
    btn5 = types.KeyboardButton ('Заказ')
    btn6 = types.KeyboardButton ('Скидка сотрудника')
    btn7 = types.KeyboardButton ('Тестовая группа')
    btn8 = types.KeyboardButton ('Замены')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    bot.send_message(message.from_user.id, 'Йоу! Какой скрин нужен?', reply_markup=markup)

    if message.text == 'Скидки и бонусы':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ad7ed47b-75a0-43cf-b440-275a58d69722/photo_2021-04-15_20-01-04.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T123149Z&X-Amz-Expires=86400&X-Amz-Signature=1b1a7981c0617204377f1ef09524dbd8608c5b4a088ff1d5f696cafc9b3184a6&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22photo_2021-04-15_20-01-04.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать «Выбрать замену» → затем «На это» справа от блюда → «Готово» в правом верхнем углу')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Сбросить блюдо':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ae6ca49f-4f3c-49b9-bd1d-dd91c0e64ed4/_.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T123359Z&X-Amz-Expires=86400&X-Amz-Signature=8d98c715e77941c09672b3d573a37cefc9455d735c9e7d17288a7fd675fce6d6&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22_.jpg%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Нажать на кнопку «Сбросить» в левом верхнем углу. После этого снова можно будет выбрать любое блюдо')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Выбрать бонусы':
        bot.send_photo(photo.from_user.id, photo= 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a993ef3b-afa3-48d9-bdfd-2241f0ba7a26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230224T123519Z&X-Amz-Expires=86400&X-Amz-Signature=857dbbe8f65c3f9c2c58947cdecb84a059127a590fcfc55614217db2f177aa55&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject')
    bot.send_message(message.from_user.id, 'Под кнопкой «Выбрать замену» нажать на «Вернуть стоимость блюда». Она вернется на бонусный счет')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Назад')
    markup.add(btn1)

    if message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Первый адрес')
    btn2 = types.KeyboardButton('Изменить адрес')
    btn3 = types.KeyboardButton('Добавить еще один адрес')
    btn4 = types.KeyboardButton('Изменить комментарий(один адрес)')
    btn5 = types.KeyboardButton('Изменить комментарий (2 и более адресов)')
    btn6 = types.KeyboardButton('Удалить адрес')
    btn7 = types.KeyboardButton('Вернуться на главную')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

bot.polling(none_stop=True, interval=0) 