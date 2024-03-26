from pydantic import BaseModel


class PublicCarValidator(BaseModel):
    user_id: int
    model: str


class EditCarValidator(BaseModel):
    car_id: int
    edited_field: str
    new_value: str
