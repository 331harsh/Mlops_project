from flask import Blueprint, request, jsonify, render_template
from ml.predict import predict_one

bp = Blueprint("main", __name__)

# Home page with form
@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = {
            "gender": request.form.get("gender"),
            "age": float(request.form.get("age")),
            "hypertension": int(request.form.get("hypertension")),
            "heart_disease": int(request.form.get("heart_disease")),
            "ever_married": request.form.get("ever_married"),
            "work_type": request.form.get("work_type"),
            "Residence_type": request.form.get("Residence_type"),
            "avg_glucose_level": float(request.form.get("avg_glucose_level")),
            "bmi": float(request.form.get("bmi")),
            "smoking_status": request.form.get("smoking_status"),
        }
        result = predict_one(form_data)
        return render_template("index.html", result=result)
    return render_template("index.html", result=None)

# API endpoint
@bp.route("/predict", methods=["POST"])
def predict_api():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input provided"}), 400
    try:
        result = predict_one(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
