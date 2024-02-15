from aiogram import types
from log_writer import logger

class GreetingService:

    HELP_TEXT = """
    Доступные команды:
    <b>/start</b> - Начать взаимодействие с ботом
    <b>/help</b> - Получить список доступных команд
    <b>/convert &lt;сумма&gt; &lt;из_валюты&gt; в &lt;в_валюту&gt;</b> - Конвертировать заданную сумму из одной валюты в другую
    Например: /convert 100 USD в EUR - конвертировать 100 долларов США в евро
    """


    async def start_command(self, message: types.Message):
        logger.info(f"Пользователь {message.from_user.id}: {message.from_user.full_name} запустил бота('/start')")
        await message.answer('Привет! Я бот. Для получения списка доступных команд введите /help.')

    async def help_command(self, message: types.Message):
        logger.info(f"Пользователь {message.from_user.id}: {message.from_user.full_name} прописал команду /help ")
        await message.answer(self.HELP_TEXT, parse_mode="HTML")