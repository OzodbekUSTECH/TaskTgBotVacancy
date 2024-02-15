import asyncio

from aiogram import Bot, Dispatcher
from routers import all_routers



async def main():
    bot = Bot('6064434084:AAHIva6LI9dnv6m5EH4n56EKugSobYaUgDU')
    dp = Dispatcher()
    # Очищаем вебхук и отменяем ожидающие обновления перед началом работы с ботом
    await bot.delete_webhook(drop_pending_updates=True)
    
    for router in all_routers:
        dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())