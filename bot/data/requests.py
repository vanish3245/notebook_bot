
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from bot.misc.configuration import conf
from bot.data.base import Base

db_engine = create_async_engine(conf.db.build_connection_str())
Session = async_sessionmaker(db_engine)



