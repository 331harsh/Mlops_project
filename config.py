import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MLFLOW_TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI', f"file://{os.path.join(BASE_DIR, 'mlruns')}")
REGISTERED_MODEL_NAME = os.getenv('REGISTERED_MODEL_NAME', 'StrokeModel')


# Model fallback path
LOCAL_MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')


# Flask
HOST = '0.0.0.0'
PORT = int(os.getenv('PORT', 5000))