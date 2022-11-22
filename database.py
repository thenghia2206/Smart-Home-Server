from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2


SQLALCHEMY_DATABASE_URL = "postgresql://lxdbcopgewquwd:1c862ff43f1cba25c4830149c6660662b1d530dac22509e511412ad7c258a4ef@ec2-52-4-87-74.compute-1.amazonaws.com:5432/dakrhdekn59o85"
#mysql+mysqldb://root:22062001@127.0.0.1:3306/sensor
#postgresql://lxdbcopgewquwd:1c862ff43f1cba25c4830149c6660662b1d530dac22509e511412ad7c258a4ef@ec2-52-4-87-74.compute-1.amazonaws.com:5432/dakrhdekn59o85
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
