import services

from aiogram import Router, F, types
from aiogram.filters import Command


router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    await services.GreetingService().start_command(message)


@router.message(Command('help'))
async def help(message: types.Message):
    await services.GreetingService().help_command(message)
    