from aiogram import Router, F, types
import services

router = Router()

"""
По разному можно реализовать здесь логику
1. Через if else в одной функции
2. Разделить всё по частям


В моем случае, использовать отдельные функции к каждому разделу(приветствие, прощание)
является более удобным, т.к. код будет чище и читабельнее в случае когда будет больше условий
"""

#приветствие
@router.message(F.text.in_(services.ChatService.greeting_words)) 
async def greeting_answer(message: types.Message):
    await services.ChatService().greeting_answer(message)

#обычные вопросы по типу как дела
@router.message(F.text.in_(services.ChatService.casual_questions)) 
async def greeting_answer(message: types.Message):
    await services.ChatService().casual_answer(message)

#прощание
@router.message(F.text.in_(services.ChatService.goodbye_words)) 
async def greeting_answer(message: types.Message):
    await services.ChatService().goodbye_answer(message)