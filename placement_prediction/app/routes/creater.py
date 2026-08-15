from flask import Blueprint, render_template, redirect, Response, url_for, session, flash





creater_bp = Blueprint('creater', __name__)


@creater_bp.route('/creater')
def creater():
    return render_template('creater.html')