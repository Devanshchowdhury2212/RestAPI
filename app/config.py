from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOSTNAME:str 
    database_port:str
    database_password:str 
    database_name:str
    database_username:str
    secret_key:str
    algorithm:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    SQLALCHEMY_DB_URL:str

    class Config:
        env_file = '.env'

settings = Settings()