from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()

# load and train the data
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# Define request body
class InputData(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message":"Iris classification API is running!"}

@app.post("/predict")
def predict(data: InputData):
    try:
        features = np.array(data.features).reshape(1,-1)
        prediction = model.predict(features)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
    
    