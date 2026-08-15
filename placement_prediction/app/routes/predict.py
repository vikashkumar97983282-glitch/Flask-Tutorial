from flask import Blueprint, render_template, redirect, Response, url_for, session, flash,request
import joblib




predict_bp = Blueprint('predict', __name__)


with open("app/models/random_forest_regressor.pkl", "rb") as file:
    model = joblib.load(file)



@predict_bp.route('/predict', methods=["GET","POST"])
def predict():
    if request.method == "POST":

        cgpa = request.form.get("cgpa")
        resume = request.form.get("resume")

        input = [[
            cgpa,
            resume
        ]]

        prediction = model.predict(input)[0]

        if prediction > 0.5:
            result = "Likely to be Placed"
        else:
            result = "Less Likely to be Placed"

        return render_template('result.html', prediction=result, score=prediction)

    return render_template('predict.html')

