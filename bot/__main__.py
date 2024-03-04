import asyncio
from aiogram import Bot, Dispatcher
# from sqlalchemy import URL

from bot.handlers import echo_text
from bot.misc.configuration import conf
from aiogram.fsm.storage.redis import RedisStorage
# from bot.data.base import BaseModel
# from bot.data.engine import create_async_engine, proceed_schemas, get_session_maker



async def main():
    bot = Bot(conf.bot.token)
    storage = RedisStorage.from_url("redis://localhost:6379/0")
    dp = Dispatcher(stotage=storage)

    dp.include_router(echo_text.router)

    
    # go_db = URL.create(conf.db.database_url_asyncpg())
    # async_engine = create_async_engine(go_db)
    # session_maker = get_session_maker(async_engine)
    # await proceed_schemas(async_engine, BaseModel.metadata)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())