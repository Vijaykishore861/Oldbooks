from pydantic import BaseModel
from datetime import datetime

class Usercreation(BaseModel):
    email: str
    user_name: str
    user_password: str
    created_on : datetime
    created_by : str

class books(BaseModel):
    book_name : str 
    author_name :str
    descryption : str
    damagePercentage : str
    created_by : str 
    created_on : datetime

class book(BaseModel):
    id : int
