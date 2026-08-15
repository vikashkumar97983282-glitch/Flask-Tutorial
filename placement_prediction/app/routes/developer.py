from flask import Blueprint, render_template, redirect, Response, url_for, session, flash





developer_bp = Blueprint('developer', __name__)


@developer_bp.route('/developer')
def developer():
    return render_template('developer.html')