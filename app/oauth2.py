from fastapi import Depends,status,HTTPException
from jose import JWTError, jwt
from . import schema,database,models
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
# Secret Key 
# Algo
# Expiration time
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data:dict):
    to_encode  = data.copy()
    expire_time = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode['exp'] = expire_time
    token = jwt.encode(to_encode ,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_access_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id:str = payload.get("user_id")# type: ignore #oauth2.create_access_token(data = {'user_id':user.id})
        if id is None:raise credentials_exception
        token_data = schema.TokenData(id = id)
    except JWTError:
        raise credentials_exception
    return token_data
    
def get_current_user(token:str = Depends(oauth2_scheme),db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail="INVALID CRED",
                                          headers = {"WWW-Authenticate":"Bearer"})
    user = verify_access_token(token,credentials_exception)
    user = db.query(models.User).filter(models.User.id == user.id).first()
    
    return user
