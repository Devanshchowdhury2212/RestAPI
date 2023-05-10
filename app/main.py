from fastapi import FastAPI
from .database import engine 
from . import models
from .routers import posts,users,auth,votes
from .config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)
@app.get("/")#decorator 
def root():
    return {"message": "Welcome to RestfUL API .. \n Connected"}

# uvicorn app.main:app --reload
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNywiZXhwIjoxNjgzNTcwNDYyfQ.vBj1_BkVBU7VrzqrPK1IWwdZgyUl8qAlT-Aoameb7Xc
