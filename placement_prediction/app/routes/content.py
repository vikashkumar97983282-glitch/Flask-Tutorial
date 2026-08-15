from flask import Blueprint, render_template, redirect, Response, session, url_for, flash




content_bp = Blueprint('content', __name__)



@content_bp.route('/content')
def content():
    return render_template('content.html')