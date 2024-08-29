from main import app
from datalayer import Usercreation
from Database import get_database_connection
from encrypt import message_skey,secret_key1
from logger import logger
from config import get_current_active_user
from typing import Annotated
from fastapi import Depends
from datalayer import book


async def edit_user(user: book):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "select * from books  where id = %s "
    vaules = user.id
    cursor.execute(query,vaules)
    users = cursor.fetchall()
    connection.commit()
    connection.close()
    return users



