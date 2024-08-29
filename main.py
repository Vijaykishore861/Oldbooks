from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import FastAPI,Depends, HTTPException, status
from config import authenticate_user,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES
from config import fake_users_db,get_current_active_user
from jwtmodel import Token,User
from datetime import  timedelta
from datalayer import Usercreation,books
from logger import logger
from Database import get_database_connection
from encrypt import secret_key1, message_skey
from datalayer import book


app = FastAPI()

@app.post('/token')
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user

@app.post("/user_details")
async def create_user(user: Usercreation, current_user: Annotated[User, Depends(get_current_active_user)]):
    connection = get_database_connection()
    cursor = connection.cursor()
    password = message_skey(user.user_password)
    logger.debug(password)
    salt = secret_key1
    logger.debug(salt)
    query = "INSERT INTO user_details(email,user_name,user_password,salt,created_on,created_by) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (user.email,user.user_name,password,salt,user.created_on,user.created_by)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    current_user()
    return {"message": "User created successfully"}

@app.get("/Books")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM books"
    cursor.execute(query)
    users = cursor.fetchall()
    connection.close()
    current_user
    return users


@app.put("/add/Books")
async def create_user(user: books, current_user: Annotated[User, Depends(get_current_active_user)]):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO books(book_name,author_name,descryption,damagePercentage,created_by,created_on) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (user.book_name,user.author_name,user.descryption,user.damagePercentage,user.created_by,user.created_on)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    current_user()
    return {"message": "User created successfully"}

@app.get("/get/Books")
async def edit_user(user:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "select * from books where id = {}".format (user)
    cursor.execute(query)
    users = cursor.fetchall()
    connection.commit()
    connection.close()
    return users

@app.patch("/get/Books")
async def edit_user(user:int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "select * from books where id = {}".format (user)
    cursor.execute(query)
    users = cursor.fetchall()
    connection.commit()
    connection.close()
    return users


