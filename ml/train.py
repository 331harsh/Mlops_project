import os
import joblib
import mlflow
import mlflow.sklearn
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from preprocess import load_data, preprocess, train_test_split_df

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "stroke_data.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "model.pkl")

def train():
    print("🔹 Loading data...")
    df = load_data(DATA_PATH)
    X, y, preprocessor = preprocess(df)

    print("🔹 Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split_df(X, y)

    print("🔹 Building pipeline...")
    clf = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', RandomForestClassifier(
            n_estimators=200,
            max_depth=8,
            random_state=42,
            class_weight="balanced"
        ))
    ])

    print("🔹 Training model...")
    clf.fit(X_train, y_train)

    print("🔹 Evaluating...")
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"✅ Accuracy: {acc:.4f}, F1: {f1:.4f}")

    # Log to MLflow
    mlflow.set_experiment("StrokePrediction")
    with mlflow.start_run():
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1", f1)
        mlflow.sklearn.log_model(clf, "model")

    # Save model locally for Flask
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(clf, MODEL_PATH)
    print(f"💾 Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()
