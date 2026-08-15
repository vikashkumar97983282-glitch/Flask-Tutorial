from flask import Blueprint, render_template, redirect, Response, url_for, session, flash




predict_bp = Blueprint('predict', __name__)



@predict_bp.route('/predict')
def predict():
    return render_template('predict.html')