from sqlalchemy import BigInteger, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from bot.data.base import Base


class Name_test_ORM(Base):
    __tablename__ = "nameuser"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)

