from database.models import Car
from database import get_db


# Добавить машину
def add_new_car_db(user_id, model):
    db = next(get_db())
    new_car = Car(user_id=user_id, model=model)
    db.add(new_car)
    db.commit()
    return f"Машина добавлена под ID {new_car.car_id}"


# Получить все машины
def get_all_car_db():
    db = next(get_db())
    all_car = db.query(Car).all()
    return all_car


# Получить определённую машину
def get_one_car_db(car_id):
    db = next(get_db())
    car = db.query(Car).filter_by(car_id=car_id).first()
    if car:
        return car
    else:
        return 'Машина не найдена'


# Измененить информацию в машине
def edit_car_db(car_id, edited_field, new_value):
    db = next(get_db())
    car = db.query(Car).filter_by(car_id=car_id).first()
    if car:
        if edited_field == "model":
            car.model = new_value
        elif edited_field == "year":
            car.year = new_value
        elif edited_field == "price":
            car.price = new_value
        elif edited_field == "description":
            car.description = new_value
        elif edited_field == "color":
            car.color = new_value
        elif edited_field == "mileage":
            car.mileage = new_value
        elif edited_field == "status":
            car.status = new_value
        elif edited_field == "category":
            car.category = new_value
        elif edited_field == "manufacturer":
            car.manufacturer = new_value
        db.commit()
    else:
        return "Машина не найдена"


# Удалить машину
def delete_car_db(car_id):
    db = next(get_db())
    car = db.query(Car).filter_by(car_id=car_id).first()
    if car:
        db.delete(car)
        db.commit()
        return "Машина удалена"
    else:
        return "Машина не найдена"
