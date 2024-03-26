from pydantic import BaseModel


class PublicCommentValidator(BaseModel):
    user_id: int
    car_id: int
    comment_text:str
