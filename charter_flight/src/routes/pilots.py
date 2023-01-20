from flask import Blueprint, jsonify, abort, request
from ..models import Pilot, db

# Creating blueprint
bp = Blueprint('pilots', __name__, url_prefix='/pilots')

# Index of pilots
@bp.route('', methods=['GET'])
def index():
    pilots = Pilot.query.all()
    result = []
    for p in pilots:
        result.append(p.serialize())
    return jsonify(result)

# Showing pilots
@bp.route('/<int:pilot_id>', methods=['GET'])
def show(pilot_id:int):
    p = Pilot.query.get_or_404(pilot_id)
    return jsonify(p.serialize())

# Adding new pilots
@bp.route('', methods=['POST'])
def create():
    # Construct pilot account
    p = Pilot(
        #pilot_id = request.json['pilot_id'],
        pilot_name = request.json['pilot_name'],
        hourly_rate = request.json['hourly_rate'],
        wait_time_rate = request.json['wait_time_rate']
    )
    db.session.add(p) # Preparing create statement
    db.session.commit() # Executing create statement
    return jsonify(p.serialize())

# Deleting pilots
@bp.route('/<int:pilot_id>', methods = ['DELETE'])
def delete(pilot_id:int):
    p = Pilot.query.get_or_404(pilot_id)
    try:
        db.session.delete(p) # prepare delete statement
        db.session.commit() # execute delete statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)

# Updating pilots
@bp.route('/<int:pilot_id>', methods = ['PATCH', 'PUT'])
def update(pilot_id:int):
    p = Pilot.query.get_or_404(pilot_id)
    if (
        'pilot_id' not in request.json and 
        'pilot_name' not in request.json and
        'hourly_rate' not in request.json and 
        'wait_time_rate' not in request.json):
        return abort(400)

    if 'pilot_name' in request.json:
        p.pilot_name = request.json['pilot_name']
    if 'hourly_rate' in request.json:
        p.hourly_rate = request.json['hourly_rate']
    if 'wait_time_rate' in request.json:
        p.wait_time_rate = request.json['wait_time_rate']


    # Next feature: Create a statement that allows you to change the pilot_id as long as
    # there is not another pilot with the same id number

    try:
        db.session.commit()
        return jsonify(p.serialize())
    except:
        return jsonify(False)
