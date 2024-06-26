import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'UCCEoh3278dda17c&@38nc(&*Y'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTE = 30


# Наш JWT тут создает токен
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({'expires': expire.isoformat()})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt
