from database.models import User
from database import get_db
from database.security import create_access_token


# Регистрация пользователя
def register_user_db(user_name, email, password):
    db = next(get_db())
    user = db.query(User).filter_by(email=email).first()
    if user:
        return "Данный email уже зарегистрирован"
    else:
        new_user =User(user_name=user_name, email=email, password=password)
        db.add(new_user)
        db.commit()
        return f"Успешно зарегистрирован c ID {new_user.user_id}"


# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())
    get_all_users = db.query(User).all()
    return get_all_users


# Получить одного пользователя
def get_exact_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        return f"Пользователь найден {user.user_id}"
    else:
        return "Пользователь не найден"


# Логин пользователя
def login_user_db(user_name, password):
    db = next(get_db())
    login = db.query(User).filter_by(user_name=user_name, password=password).first()
    if login:
        token_data ={"user_id": login.user_id}
        access_token_data = create_access_token(token_data)
        return {"access_token": access_token_data, "token_type": "Bearer", "status": "Success"}
    else:
        return "Неверный логин или пароль"


# Изменение данных пользователя
def edit_user_info_db(user_id, edited_field, new_value):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        if edited_field == "user_name":
            user.user_name = new_value
        elif edited_field == "email":
            user.email = new_value
        elif edited_field == "password":
            user.password = new_value
        db.commit()
        return "Успешно изменено"
    else:
        return "Пользователь не найден"


# Удаление пользователя
def delete_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return f'Пользователь с ID {user_id} удален'
    else:
        return 'Пользователь не найден'
