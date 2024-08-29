from pydantic import BaseModel
from typing import Annotated, Union

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

class UserInDB(User):
    hashed_password: str

fake_users_db = {
    "vijay": {
        "username": "vijay",
        "full_name": "vijaykishore",
        "email": "vijaykishore861@gmail.com",
        "hashed_password": "$2b$12$yBfvwwOcUPTQgqchmx3TdONn5IHWDqI3EN7soO9sjsmtJxdOBdCAq",
        "disabled": False,     
    }

}


