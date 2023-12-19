import telebot
import random

bot = telebot.TeleBot('...')

# Список фамилий для использования
last_names = ["Дворова", "Подлесняк", "Муравьев", "Бурыкин", "Кольцов", "Усов", "Висков", "Данилов", "Хрыкин", "Оськин", "Булычев", "Колтун", "Фатехов", "Чиботарь", "Рустамов", "Коршунов", "Стребков", "Аверьянов", "Винидиктова"]

# Словарь для хранения пар "пользователь - получатель"
secret_santas = {}

# Обработчик команды /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Для участия в тайном санте используй /join.")

# Обработчик команды /join
@bot.message_handler(commands=['join'])
def join(message):
    # Получаем имя пользователя
    username = message.from_user.username
    # Инициализируем пользователя со значением None в качестве тайного санты
    secret_santas[username] = None
    bot.reply_to(message, "Ты присоединился к тайному санте! Напиши /assign для продолжения")

# Обработчик команды /assign
@bot.message_handler(commands=['assign'])
def assign(message):
    # Получаем имя пользователя
    username = message.from_user.username
    # Проверяем, что у пользователя нет назначенного тайного санты
    if username in secret_santas and secret_santas[username] is None:
        # Получаем список доступных пользователей для назначения
        available_users = [name for name in secret_santas if name != username and secret_santas[name] is None]
        if available_users:
            # Выбираем случайного получателя
            selected_santa_name = random.choice(available_users)
            # Назначаем тайного санту для пользователя и пользователя для тайного санты
            secret_santas[username] = selected_santa_name
            secret_santas[selected_santa_name] = username
            # Отправляем пользователю сообщение с именем его тайного санты
            bot.send_message(message.chat.id, f'Ваш тайный санта: {selected_santa_name}')
            # Отправляем пользователю сообщение, что он тайный санта для кого-то
            bot.send_message(message.chat.id, f'Вы тайный санта для: {random.choice(last_names)}')
        else:
            bot.send_message(message.chat.id, "Извините, не удалось найти тайного санту.")
    else:
        # Если у пользователя уже есть тайный санта, отправляем сообщение с его именем
        santa_name = secret_santas[username]
        bot.send_message(message.chat.id, f"Вы уже получили тайного санту: {santa_name}.")

bot.polling()
