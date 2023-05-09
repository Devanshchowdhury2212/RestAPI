from fastapi import Depends,status,HTTPException
from jose import JWTError, jwt
from . import schema
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
# Secret Key 
# Algo
# Expiration time
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    to_encode  = data.copy()
    expire_time = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode['exp'] = expire_time
    token = jwt.encode(to_encode ,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_access_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id:str = payload.get("user_id")#oauth2.create_access_token(data = {'user_id':user.id})
        if id is None:raise credentials_exception
        token_data = schema.TokenData(id = id)
    except JWTError:
        raise credentials_exception
    return token_data
    
def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail="INVALID CRED",
                                          headers = {"WWW-Authenticate":"Bearer"})
    return verify_access_token(token,credentials_exception)
