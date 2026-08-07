import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "👋 سلام\n\n"
        "به ربات فروش VPN خوش اومدی."
    )

print("Bot Started...")

bot.infinity_polling(skip_pending=True)
