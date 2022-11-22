import joblib
def predict_model(day: int ,temp: float, hum: float ):
    model = joblib.load("ML/knn_model.pkl")
    data =[[day,temp,hum]]
    res = model.predict(data)
    return res[0]
