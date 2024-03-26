from fastapi import APIRouter
from comments import PublicCommentValidator
from database.commentservice import (add_comment_db,
                                     get_all_comment_db,
                                     get_user_comments_db,
                                     get_car_comments_db,
                                     delete_comment_db)

comment_router = APIRouter(prefix='/comments', tags=['Работа с комментариями'])


# Добавить комментарий
@comment_router.post("/add")
async def add_comment(data: PublicCommentValidator):
    result = add_comment_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': "Комментарий не найден"}


# Получить все комментарии
@comment_router.get("/all")
async def get_all_comments():
    return get_all_comment_db()


# Получить комментарии определённого пользователя
@comment_router.get("/user")
async def get_user_comments(user_id):
    return get_user_comments_db(user_id)


# Получить все комментарии определённой машины
@comment_router.get("/car")
async def get_car_comments(car_id):
    return get_car_comments_db(car_id)


# Удалить комментарий
@comment_router.delete("/delete")
async def delete_comment(comment_id, user_id):
    result = delete_comment_db(comment_id, user_id)
    if result:
        return {'message': result}
    else:
        return {'message': "Комментарий не найден"}
