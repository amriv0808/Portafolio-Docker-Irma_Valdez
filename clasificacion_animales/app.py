import joblib
import numpy as np
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

# Cargar el modelo entrenado
model = joblib.load("dog_breed_model.joblib")

# Configurar el directorio de plantillas HTML
templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="API de Clasificación de Razas de Perros",
    description="Predicción de raza según métricas físicas mediante Docker",
)


class DogFeatures(BaseModel):
    weight_kg: float = Field(..., example=27.5)
    height_cm: float = Field(..., example=57.0)
    energy_level: int = Field(..., example=5)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Sintaxis compatible con las versiones recientes de FastAPI/Starlette
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/predict")
def predict_breed(dog: DogFeatures):
    features = np.array([[dog.weight_kg, dog.height_cm, dog.energy_level]])
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features).max()

    return {
        "predicted_breed": str(prediction),
        "confidence": round(float(probabilities), 2),
    }