from flask import Blueprint, render_template

# Creating blueprint
bp = Blueprint('calendar', __name__, url_prefix='/calendar')

# Getting the template calendar.html
@bp.route('', methods=['GET'])
def calendar():
    return render_template('calendar.html')