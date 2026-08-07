import telebot
from config import BOT_TOKEN
from keyboards import main_menu
from database import create_table, add_user


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):

    add_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name
    )

    bot.send_message(
        message.chat.id,
        "👋 سلام\n\n"
        "به ربات فروش VPN خوش آمدید.",
        reply_markup=main_menu()
    )
    

print("Bot Started...")

bot.infinity_polling(skip_pending=True)
