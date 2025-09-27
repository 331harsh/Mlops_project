import os
import joblib
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "model.pkl")

# Load trained model at module import
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Trained model not found at {MODEL_PATH}. Run train.py first.")
model = joblib.load(MODEL_PATH)

def predict_one(input_dict: dict) -> dict:
    """
    Takes a dictionary of patient features and returns prediction + probability.
    Example input_dict:
    {
        "gender": "Male",
        "age": 67,
        "hypertension": 0,
        "heart_disease": 1,
        "ever_married": "Yes",
        "work_type": "Private",
        "Residence_type": "Urban",
        "avg_glucose_level": 228.69,
        "bmi": 36.6,
        "smoking_status": "formerly smoked"
    }
    """
    # Convert to DataFrame for sklearn pipeline
    X = pd.DataFrame([input_dict])

    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0][1]  # probability of stroke

    return {
        "prediction": int(pred),
        "probability": round(float(proba), 4)
    }
