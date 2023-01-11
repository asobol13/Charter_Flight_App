from flask import Blueprint, jsonify, abort, request
from ..models import Charter, db, Customer, Aircraft, Pilot

# Creating blueprint
bp = Blueprint('charters', __name__, url_prefix='/charters')

# Index of charters
@bp.route('', methods=['GET'])
def index():
    charters = Charter.query.all()
    result = []
    for ch in charters:
        result.append(ch.serialize())
    return jsonify(result)

# Showing charters
@bp.route('/<int:charter_number>', methods=['GET'])
def show(charter_number:int):
    ch = Charter.query.get_or_404(charter_number)
    return jsonify(ch.serialize())

# Creating accounts
@bp.route('', methods=['POST'])
def create():
    # Request body must contain account_number, destination_airport, departure time
    if ('account_number' not in request.json or 
    'destination_airport' not in request.json or
    'departure_time' not in request.json):
        return abort(400)
    # Construct charter trip
    ch = Charter(
        departure_airport = request.json['departure_airport'],
        destination_airport = request.json['destination_airport'],
        departure_date = request.json['departure_date'],
        return_date = request.json['return_date'],
        departure_time = request.json['departure_time'],
        return_time = request.json['return_time'],
        wait_hours = request.json['wait_hours'],
        flight_hours = request.json['flight_hours'],
        number_pax = request.json['number_pax'],
        account_number = request.json['account_number'],
        tail_number = request.json['tail_number'],
        pilot_id = request.json['pilot_id']
    )
    db.session.add(ch) # Preparing create statement
    db.session.commit() # Executing create statement
    return jsonify(ch.serialize())

# Deleting charter trips
@bp.route('/<int:charter_number>', methods = ['DELETE'])
def delete(charter_number:int):
    ch = Charter.query.get_or_404(charter_number)
    try:
        db.session.delete(ch) # prepare delete statement
        db.session.commit() # execute delete statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)

# Updating charter trips
@bp.route('/<int:charter_number>', methods = ['PATCH', 'PUT'])
def update(charter_number:int):
    ch = Charter.query.get_or_404(charter_number)
    # if charter_number not in request.json:
    #     return abort(400)

    if 'departure_airport' in request.json:
        ch.departure_airport = request.json['departure_airport']
    if 'destination_airport' in request.json:
        ch.destination_airport = request.json['destination_airport']
    if 'departure_date' in request.json:
        ch.departure_date= request.json['departure_date']
    if 'return_date' in request.json:
        ch.return_date = request.json['return_date']
    if 'departure_time' in request.json:
        ch.departure_time = request.json['departure_time']
    if 'return_time' in request.json:
        ch.return_time = request.json['return_time']
    if 'wait_hours' in request.json:
        ch.wait_hours = request.json['wait_hours']
    if 'flight_hours' in request.json:
        ch.flight_hours = request.json['flight_hours']
    if 'number_pax' in request.json:
        ch.number_pax = request.json['number_pax']
    if 'account_number' in request.json:
        ch.account_number = request.json['account_number']
    if 'tail_number' in request.json:
        ch.tail_number = request.json['tail_number']
    if 'pilot_id' in request.json:
        ch.pilot_id = request.json['pilot_id']

    try:
        db.session.commit()
        return jsonify(ch.serialize())
    except:
        return jsonify(False)
