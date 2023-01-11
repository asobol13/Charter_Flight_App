from flask import Blueprint, jsonify, abort, request
from ..models import Aircraft, db #Charter

# Creating blueprint
bp = Blueprint('aircrafts', __name__, url_prefix='/aircrafts')

# Index of aircrafts
@bp.route('', methods=['GET'])
def index():
    aircrafts = Aircraft.query.all()
    result = []
    for a in aircrafts:
        result.append(a.serialize())
    return jsonify(result)

# Showing aircrafts
@bp.route('<tail_number>', methods=['GET'])
def show(tail_number):
    a = Aircraft.query.get_or_404(tail_number)
    return jsonify(a.serialize())

# Adding new aircrafts
@bp.route('', methods=['POST'])
def create():
    # Request body must contain a tail_number
    if 'tail_number' not in request.json:
        return abort(400)
    # Construct aircraft account
    a = Aircraft(
        tail_number = request.json['tail_number'],
        aircraft_name = request.json['aircraft_name'],
        hourly_rate = request.json['hourly_rate'],
        wait_time_rate = request.json['wait_time_rate'],
        capacity = request.json['capacity']
    )
    db.session.add(a) # Preparing create statement
    db.session.commit() # Executing create statement
    return jsonify(a.serialize())

# Deleting aircrafts
@bp.route('<tail_number>', methods = ['DELETE'])
def delete(tail_number):
    a = Aircraft.query.get_or_404(tail_number)
    try:
        db.session.delete(a) # prepare delete statement
        db.session.commit() # execute delete statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)

# Updating aircrafts
@bp.route('<tail_number>', methods = ['PATCH', 'PUT'])
def update(tail_number):
    a = Aircraft.query.get_or_404(tail_number)
    if (
        'tail_number' not in request.json and 
        'aircraft_name' not in request.json and
        'hourly_rate' not in request.json and 
        'wait_time_rate' not in request.json and
        'capacity' not in request.json):
        return abort(400)

    if 'aircraft_name' in request.json:
        a.aircraft_name = request.json['aircraft_name']
    if 'hourly_rate' in request.json:
        a.hourly_rate = request.json['hourly_rate']
    if 'wait_time_rate' in request.json:
        a.wait_time_rate = request.json['wait_time_rate']
    if 'capacity' in request.json:
        a.capacity = request.json['capacity']

    try:
        db.session.commit() # Preparing to update statement
        return jsonify(a.serialize()) # Executing update statement
    except:
        return jsonify(False)
