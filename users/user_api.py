
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from users import RegisterUserValidator, EditUserValidator
from database.userservice import (register_user_db,
                                  get_all_users_db,
                                  get_exact_user_db,
                                  login_user_db,
                                  edit_user_info_db,
                                  delete_user_db)

# Создаём компонент
user_router = APIRouter(prefix='/users', tags=['Управление пользователями'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


# Регистрация пользователя
@user_router.post('/register')
async def register_user(data: RegisterUserValidator):
    result = register_user_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Такой пользователь уже имеется'}


# Получить всех пользователей
@user_router.get('/all')
async def get_all_users():
    return get_all_users_db()


# Получить одного пользователя
@user_router.get('/one')
async def get_user(user_id: int):
    user = get_exact_user_db(user_id)
    return user


# Логин пользователя
@user_router.post('/login')
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = login_user_db(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail='Неверный номер или пароль')
    else:
        return user


# Изменение данных пользователя
@user_router.put('/edit')
async def edit_user(data: EditUserValidator):
    change_data = data.model_dump()
    result = edit_user_info_db(**change_data)
    return result


# Удаление пользователя
@user_router.delete('/delete')
async def delete_user(user_id):
    user = delete_user_db(user_id)
    return user



