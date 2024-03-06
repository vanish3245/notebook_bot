import asyncio
from aiogram import Bot, Dispatcher

from bot.handlers import echo_text
from bot.misc.configuration import conf

from aiogram.fsm.storage.redis import RedisStorage




async def main():
    bot = Bot(conf.bot.token)
    storage = RedisStorage.from_url("redis://localhost:6379/0")
    dp = Dispatcher(stotage=storage)

    dp.include_router(echo_text.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())