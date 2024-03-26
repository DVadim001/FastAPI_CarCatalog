from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from database import Base


# Модель пользователей
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    user_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    # Добавление связи с комментариями
    comments = relationship("Comment", back_populates='user')


# Модель машин
class Car(Base):
    __tablename__ = "cars"
    car_id = Column(Integer, autoincrement=True, primary_key=True)
    model = Column(String)
    year = Column(Integer)
    price = Column(Float)
    description = Column(Text, nullable=True)
    color = Column(String)
    mileage = Column(Integer)  # Пробег
    status = Column(String)  # Новый, Б/У
    category = Column(String)  # Седан, внедорожник и т.д.
    manufacturer = Column(String)  # Производитель

    # Добавление связи с комментариями
    comments = relationship("Comment", back_populates='car')


# Модель отзывов
class Comment(Base):
    __tablename__ = "comments"
    comment_id = Column(Integer, autoincrement=True, primary_key=True)
    comment_text = Column(Text)
    published_date = Column(DateTime)

    # ForeignKey указывает на столбец в таблице users и cars соответственно
    user_id = Column(Integer, ForeignKey("users.user_id"))
    car_id = Column(Integer, ForeignKey("cars.car_id"))

    # Определение связи для облегчения доступа к связанным объектам User и Car
    user = relationship("User", back_populates='comments')
    car = relationship("Car", back_populates='comments')
