from fastapi import FastAPI, Depends
import models
from ML.predict import predict_model
from database import engine
from sqlalchemy.orm import Session
from database import get_db
import random
import datetime
from datetime import datetime



models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get('/sensor/')
async def sensor(temp: float, hum: float, db: Session = Depends(get_db)):
    time_vn = datetime.now()
    x = models.Sensor(temperature=temp, humidity=hum, createdOn=time_vn)
    db.add(x)
    db.commit()
    db.refresh(x)
    return {'temperature': temp, 'humidity': hum}


@app.get("/get_15")
def get_15(db: Session = Depends(get_db)):
    skip = 0
    limit = 15
    data = db.query(models.Sensor).order_by(models.Sensor.id.desc())
    data = data[skip: skip + limit]
    data = data[::-1]
    x = []
    for i in data:
        date = i.createdOn.strftime('%m-%d')
        time = i.createdOn.strftime('%H:%M')
        y = {"id": i.id, "temperature": i.temperature,
             "humidity": i.humidity, "time": time, "date": date}
        x.append(y)
    return x


@app.delete("/delete")
def delete_all(db: Session = Depends(get_db)):
    db.query(models.Sensor).delete()
    db.commit()
    return {"OK"}


@app.get("/get_new")
def get_th(db: Session = Depends(get_db)):
    data = db.query(models.Sensor).order_by(models.Sensor.id.desc()).first()
    return {"temperature": data.temperature, "humidity": data.humidity, "time": data.createdOn}


@app.get("/loikhuyen")
def get_loikhuyen(db: Session = Depends(get_db)):
    data = db.query(models.Sensor).order_by(models.Sensor.id.desc()).first()
    label0 = ['Hôm nay trời khá đẹp bạn nên ra ngoài chơi',
              'Đừng ở trong nhà nữa ra ngoài chơi đê', 'Hôm nay là ngày thích hợp để đi cắm trại']
    label1 = ['Nay có khả năng mưa to đó', 'Hôm nay trời có thể mưa đó, nhớ cầm ô theo nha !',
              'Nay không thích hợp đi chơi đâu, trời khả năng mưa cao đó']
    time = data.createdOn.timestamp()
    res = predict_model(time,data.temperature,data.humidity)
    if (res == 1):
        a= random.choice(label0)
    elif(res == 0):
        a= random.choice(label1)
    return {'mess': a}


@app.get("/get_15")
def get_15(db: Session = Depends(get_db)):
    skip = 0
    limit = 15
    data = db.query(models.Sensor).order_by(models.Sensor.id.desc())
    data = data[skip : skip + limit]
    data = data[::-1]
    x = []
    for i in data:
        date = i.createdOn.strftime('%m-%d')
        time = i.createdOn.strftime('%H:%M')
        y ={"id": i.id, "temperature" : i.temperature , "humidity": i.humidity, "time": time,"date": date}
        x.append(y)
    return x

@app.delete("/delete")
def delete_all(db: Session = Depends(get_db)):
    db.query(models.Sensor).delete()
    db.commit()
    return {"OK"}

@app.get("/get_new")
def get_th(db: Session = Depends(get_db)):
    data = db.query(models.Sensor).order_by(models.Sensor.id.desc()).first()
    return {"temperature": data.temperature ,"humidity" : data.humidity, "time" : data.createdOn}

@app.get('/all')
def get_all(db: Session = Depends(get_db)):
    y = db.query(models.Sensor).all()
    return y


@app.get('/')
def root_api():
    return {"message": "Welcome to The Nghia"}