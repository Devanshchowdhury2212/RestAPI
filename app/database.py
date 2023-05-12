from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings 



# SQLALCHEMY_DB_URL = "postgresql://<username>:<password>@<ip-address/hostname>/<database name>"
# SQLALCHEMY_DB_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.DATABASE_HOSTNAME}:{settings.database_port}/{settings.database_name}"
SQLALCHEMY_DB_URL = f"postgresql://testdb_2dj9_user:zvprnD19uj3HvhQVZlGExw513GBgOJO8@dpg-checkue7avja5m9gunsg-a.singapore-postgres.render.com/testdb_2dj9"
SQLALCHEMY_DB_URL = f"{settings.SQLALCHEMY_DB_URL}"

engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Using PostGres adapter of Python for connection rather than SQL alchemy 
# while True:
#     try:
#         conn = connect(host='localhost',database='fastapidb',user='postgres',password='password',cursor_factory=psycopg2.extras.RealDictCursor)
#         cursor = conn.cursor()
#         print("Connected .. ")
#         break
#     except:
#         print('Connection Failed','Wait for 30 seconds')
#         time.sleep(30)