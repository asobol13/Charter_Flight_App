from flask import Blueprint, render_template


# Creating blueprint
bp = Blueprint('home', __name__)#, url_prefix='/')

# Getting the template index.html
@bp.route('/')#, methods=['GET'])
def home():
    return render_template('index.html')