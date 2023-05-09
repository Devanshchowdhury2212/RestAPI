from fastapi import FastAPI, HTTPException,Depends,Response,status,APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schema,database,models,utils,oauth2
router = APIRouter(tags=['AUTHENTICATION'])

@router.post('/login')
def login(user_cred:OAuth2PasswordRequestForm = Depends(),db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_cred.username).first()
    if user and utils.verify(user_cred.password,user.password):
        pass
    else:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,detail="INVALID CREDENTIALS")
    token = oauth2.create_access_token(data = {'user_id':user.id})
    return {'token':token,"token_type":"bearer"}
