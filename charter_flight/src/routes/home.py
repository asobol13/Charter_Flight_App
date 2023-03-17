from flask import Blueprint, render_template


# Creating blueprint
bp = Blueprint('home', __name__)

# Getting the template index.html
@bp.route('/')
def home():
    return render_template('index.html')