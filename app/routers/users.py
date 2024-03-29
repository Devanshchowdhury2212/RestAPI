from .. import schema,database,utils,models
from fastapi import Response,status,APIRouter
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException,Depends


router = APIRouter(prefix='/users',tags=['Users'])

@router.post('',response_model=schema.User_Out)
def create_user(user:schema.UserCreate,db: Session = Depends(database.get_db)):
    user.password = utils.get_hash(user.password)
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail="USER ALREADY Registered")
    new_user = models.User(**user.dict())
    db.add(new_user);db.commit();db.refresh(new_user)
    return new_user

@router.get('/{id}',response_model=schema.User_Out)
def get_user(id:int,db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                                    detail=f"No User with {id} found")
    return user
