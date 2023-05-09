from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_hash(password:str):
    return pwd_context.hash(password)

def verify(p1,p2):return pwd_context.verify(p1,p2)