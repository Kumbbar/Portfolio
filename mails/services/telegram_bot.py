import os

from dotenv import load_dotenv
import telebot

load_dotenv()


class TelegramBotService:
    TElEGRAM_ADMIN_ID = os.environ.get('TElEGRAM_ADMIN_ID')
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    bot = telebot.TeleBot(BOT_TOKEN)

    @classmethod
    def send_message(cls, name: str, contacts: str, text: str):
        cls.bot.send_message(
            cls.TElEGRAM_ADMIN_ID,
            f"Имя: {name}\n{text}\nКонтакты: {contacts}"
        )

