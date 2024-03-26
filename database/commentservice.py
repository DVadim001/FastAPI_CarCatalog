from database.models import Comment
from database import get_db


# Добавить комментарий
def add_comment_db(user_id, car_id, comment_text):
    db = next(get_db())
    new_comment = Comment(user_id=user_id, car_id=car_id, comment_text=comment_text)
    db.add(new_comment)
    db.commit()
    return "Комментарий успешно добавлен"


# Получить все комментарии
def get_all_comment_db():
    db = next(get_db())
    comment = db.query(Comment).all()
    if comment:
        return comment
    else:
        return "Комментарии отсутствуют"


# Получить комментарии определённого пользователя
def get_user_comments_db(user_id):
    db = next(get_db())
    users_comment = db.query(Comment).filter_by(user_id=user_id).all()
    if users_comment:
        return users_comment
    else:
        return "Комментарий или пользователь отсутствует"


# Получить все комментарии определённой машины
def get_car_comments_db(car_id):
    db = next(get_db())
    car_comment = db.query(Comment).filter_by(car_id=car_id).all()
    if car_comment:
        return car_comment
    else:
        return "Комментарий или машина отсутствует"


# Удалить комментарий
def delete_comment_db(comment_id):
    db = next(get_db())
    comment = db.query(Comment).filter_by(comment_id=comment_id).first()
    if comment:
        db.delete(comment)
        db.commit()
        return "Комментарий успешно удалён"
    else:
        return "Комментарий или пользователь не найден"
