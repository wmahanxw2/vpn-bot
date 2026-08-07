
from telebot import types

def main_menu():
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    btn1 = types.KeyboardButton("🛒 خرید VPN")
    btn2 = types.KeyboardButton("📦 سرویس من")
    btn3 = types.KeyboardButton("🔄 تمدید سرویس")
    btn4 = types.KeyboardButton("👤 حساب کاربری")
    btn5 = types.KeyboardButton("💬 پشتیبانی")

    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    keyboard.add(btn5)

    return keyboard
