from fastapi import FastAPI
from users.user_api import user_router
from cars.car_api import car_router
from comments.comment_api import comment_router
from database import Base, engine

app = FastAPI(
    title="Car Catalog",
    docs_url='/')

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(car_router)
app.include_router(comment_router)
