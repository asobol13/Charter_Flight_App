from flask import Blueprint, render_template

# Creating blueprint
bp = Blueprint('home', __name__, url_prefix='/home')

bp.route('/')
def home():
    return render_template('index.html')