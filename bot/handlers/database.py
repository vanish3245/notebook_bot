# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from bot.misc.configuration import conf
# from sqlalchemy.ext.asyncio import create_async_engine




# engine = create_async_engine(conf.db.database_url_asyncpg())#Сюда надо имя пароль для PostgreSQL

# Base = declarative_base()

# class Profile(Base):
#     __tablename__ = 'profile'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)

# def save_user_data(data):
#     with Session() as session:
#         user = Profile(name=data['name'], age=data['age'])
#         session.add(user)
#         session.commit()


# Base.metadata.create_all(engine)


# Session = sessionmaker(bind=engine)
# session = Session()


# registrations = session.query(Profile).all()
# for reg in registrations:
#     print(reg.id, reg.name, reg.age)