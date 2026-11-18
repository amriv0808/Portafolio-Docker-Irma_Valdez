import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def generate_and_train():
    # Crear un dataset tabular sintético basado en características físicas
    data = {
        "weight_kg": [
            25,
            30,
            28,
            6,
            8,
            7,
            3,
            4,
            2.5,
            12,
            14,
            11,
        ],  # Peso medio
        "height_cm": [
            58,
            60,
            55,
            35,
            38,
            33,
            20,
            22,
            18,
            38,
            40,
            36,
        ],  # Altura a la cruz
        "energy_level": [
            5,
            4,
            5,
            3,
            4,
            3,
            2,
            2,
            3,
            5,
            4,
            5,
        ],  # Escala 1-5
        "breed": [
            "Labrador Retriever",
            "Labrador Retriever",
            "Golden Retriever",
            "Beagle",
            "Beagle",
            "Beagle",
            "Chihuahua",
            "Chihuahua",
            "Chihuahua",
            "French Bulldog",
            "French Bulldog",
            "French Bulldog",
        ],
    }

    df = pd.DataFrame(data)

    X = df[["weight_kg", "height_cm", "energy_level"]]
    y = df["breed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    model = RandomForestClassifier(n_estimators=30, random_state=42)
    model.fit(X_train, y_train)

    # Guardar modelo
    joblib.dump(model, "dog_breed_model.joblib")
    print(
        f"Modelo entrenado con precisión: {model.score(X_test, y_test)*100:.1f}%"
    )


if __name__ == "__main__":
    generate_and_train()