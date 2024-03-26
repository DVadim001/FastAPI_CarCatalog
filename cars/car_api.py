from fastapi import APIRouter
from database.carservice import (add_new_car_db,
                                 get_all_car_db,
                                 get_one_car_db,
                                 edit_car_db,
                                 delete_car_db)
from cars import PublicCarValidator, EditCarValidator

car_router = APIRouter(prefix='/cars', tags=['Работа с машинами'])


# Добавить машину
@car_router.post("/add")
async def add_new(data: PublicCarValidator):
    new_car = add_new_car_db(**data.model_dump())
    return {'message': new_car}


# Получить все машины
@car_router.get("/all")
async def get_all():
    get_car = get_all_car_db()
    return {'message': get_car}


# Получить определённую машину
@car_router.get("/one")
async def get_one(car_id):
    result = get_one_car_db(car_id)
    if result:
        return {'message': result}
    else:
        return {'message': "Машина не найдена."}


# Измененить информацию в машине
@car_router.put("/edit")
async def edit_car(data: EditCarValidator):
    result = edit_car_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': "Ошибка при изменении"}


# Удалить машину
@car_router.delete("/delete")
async def delete_car(car_id):
    return delete_car_db(car_id)
