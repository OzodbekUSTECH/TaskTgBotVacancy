from aiogram import Router, F, types
import services

router = Router()

@router.message(F.text.startswith('/convert'))
async def convert(message: types.Message):
    await services.ConversionService().convert_command(message)


