import telebot
from config import BOT_TOKEN
from keyboards import main_menu

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 سلام\n\n"
        "به ربات فروش VPN خوش آمدید.\n"
        "یکی از گزینه‌ها را انتخاب کنید:",
        reply_markup=main_menu()
    )

print("Bot Started...")

bot.infinity_polling(skip_pending=True)
