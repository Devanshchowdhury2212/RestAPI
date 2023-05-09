from random import randint
from sqlite3 import Cursor, Timestamp
import stat
from typing import Optional,List
from urllib import response
from xmlrpc.client import Boolean
from fastapi import FastAPI, HTTPException,Depends
from psycopg2 import connect 
import psycopg2.extras
import time
from fastapi import Response,status
from .database import engine,get_db
from . import models,utils
from sqlalchemy.orm import Session
from .schema import PostCreate,Post,UserCreate,User_Out
from .routers import posts,users,auth


status_var = False
while not status_var:
    try:
        conn = connect(host='localhost',database='fastapidb',user='postgres',password='password',cursor_factory=psycopg2.extras.RealDictCursor)
        cursor = conn.cursor()
        print("Connected .. ")
        status_var = True
    except:
        print('Connection Failed','Wait for 30 seconds')
        time.sleep(30)


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
@app.get("/")#decorator 
def root():
    return {"message": "Welcome to RestfUL API .. \n Connected"}

# uvicorn app.main:app --reload
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNywiZXhwIjoxNjgzNTcwNDYyfQ.vBj1_BkVBU7VrzqrPK1IWwdZgyUl8qAlT-Aoameb7Xc
