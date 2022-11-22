from database import Base
from sqlalchemy import Column,Integer,Float
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from datetime import datetime

time_vn = datetime.now()


class Sensor(Base):
    __tablename__= "sensor"
    id = Column(Integer, primary_key=True, nullable=False)
    temperature=Column(Float, nullable=False) 
    humidity=Column(Float, nullable=False)
    createdOn=Column(TIMESTAMP(timezone=True),nullable=False)
