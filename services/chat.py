from aiogram import types
from log_writer import logger

class ChatService:
    """
    Класс ChatService отвечает за ответ на простые текстовые сообщения 
    с приветствием или прощанием в зависимости от контекста сообщения.
    """


    greeting_words = ['привет', 'здравствуй', 'добрый день']
    casual_questions = ['как ты?', 'как дела?', 'как поживаешь?', 'что нового?']
    goodbye_words = ['пока', 'до свидания', 'до скорого']


    async def greeting_answer(self, message:types.Message):
        logger.info(f"Пользователь {message.from_user.id}: {message.from_user.full_name} написал приветствие: '{message.text}'; и получил ответ от бота")

        await message.answer('Привет! Как я могу помочь вам?')

    async def casual_answer(self, message: types.Message):
        logger.info(f"Пользователь {message.from_user.id}: {message.from_user.full_name} написал вопрос: '{message.text}'; и получил ответ от бота")

        await message.answer("Все хорошо, спасибо за ваш интерес! Как я могу помочь вам?")

    async def goodbye_answer(self, message: types.Message):
        logger.info(f"Пользователь {message.from_user.id}: {message.from_user.full_name} написал прощание: '{message.text}'; и получил ответ от бота")

        await message.answer("До свидания! Надеюсь, мы скоро увидимся снова.")

