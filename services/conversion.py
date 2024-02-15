import requests

from aiogram import types
from log_writer import logger

class ConversionService:
    """
    Класс ConversionService отвечает за конвертацию валют.
    """

    async def convert_command(self, message: types.Message):
        logger.info(f"Пользователь {message.from_user.id}: {message.from_user.full_name} запустил конвертацию валют")

        # Получаем текст сообщения и разбиваем его на части
        msg_text = message.text 
        parts = msg_text.split()

        """
        Длина равна будет 5, т.к.
        0 - /convert(1)
        1 - amount(2)
        2 - from currency(3),
        3 - to(4)
        4 - to currency(5)
        """
        # Проверяем правильность формата сообщения
        if len(parts) != 5:
            logger.info(f"Пользователь {message.from_user.id}: {message.from_user.full_name} не правильно ввел формат для конвертации")
            return await message.answer("Неверный формат.\nИспользуйте /convert <сумма> <из_валюты> to <в_валюту>.")
        
        # Получаем сумму и коды валют из сообщения
        amount = float(parts[1])
        from_currency = parts[2].upper()
        to_currency = parts[4].upper()

        # Формируем URL для запроса курса обмена валют
        url = f"https://v6.exchangerate-api.com/v6/0f5d914610d764f3b8c595c5/pair/{from_currency}/{to_currency}"
        response = requests.get(url)
        data = response.json()

        # Проверяем успешность запроса
        if data['result'] == 'success':
            # Получаем курс конвертации и вычисляем конвертированную сумму
            conversion_rate = data['conversion_rate']
            converted_amount = amount * conversion_rate

            logger.info(f"Пользователь {message.from_user.id}: {message.from_user.full_name} успешно провел конвертацию валют")
            # Формируем ответ пользователю с результатом конвертации
            msg_response = f'{amount} {from_currency} равен {converted_amount} {to_currency}.'
        else:
            logger.info(f"Пользователь {message.from_user.id}: {message.from_user.full_name} не правильно ввел коды валют")
            # Формируем ответ пользователю с сообщением об ошибке
            msg_response = 'Неверные валюты. Пожалуйста, убедитесь, что вы ввели правильные коды валют.'


        await message.answer(msg_response)
        

