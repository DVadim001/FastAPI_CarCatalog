from pydantic import BaseModel


class RegisterUserValidator(BaseModel):
    user_name: str
    email: str
    password: str


class EditUserValidator(BaseModel):
    user_id: int
    edited_field: str
    new_value: str
