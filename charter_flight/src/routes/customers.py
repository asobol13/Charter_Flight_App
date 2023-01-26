from flask import Blueprint, jsonify, abort, request, render_template
from ..models import Customer, db
import hashlib
import secrets

# Scramble function here
def scramble(password:str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

# Creating blueprint
bp = Blueprint('customers', __name__, url_prefix='/customers')

# Getting the template customers.html
@bp.route('', methods=['GET'])
def addcustomer():
    return render_template('customers.html')

# Index of customers
@bp.route('', methods=['GET'])
def index():
    customers = Customer.query.all()
    result = []
    for c in customers:
        result.append(c.serialize())
    return jsonify(result)

# Showing accounts
@bp.route('/<int:account_number>', methods=['GET'])
def show(account_number:int):
    c = Customer.query.get_or_404(account_number)
    return jsonify(c.serialize())

# Creating accounts
@bp.route('', methods=['POST'])
def create():
    # Request body must contain username, password and phone number
    if 'username' not in request.json or 'password' not in request.json or 'phonenumber' not in request.json:
        return abort(400)
    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)
    # Construct account
    c = Customer(
        #account_number = request.json['account_number'],
        name = request.json['name'],
        signed_agreement = request.json['signed_agreement'],
        username = request.json['username'],
        password = scramble(request.json['password']),
        phonenumber = request.json['phonenumber'],
        email = request.json['email']
    )
    db.session.add(c) # Preparing create statement
    db.session.commit() # Executing create statement
    return jsonify(c.serialize())

# Deleting accounts
@bp.route('/<int:account_number>', methods = ['DELETE'])
def delete(account_number:int):
    c = Customer.query.get_or_404(account_number)
    try:
        db.session.delete(c) # prepare delete statement
        db.session.commit() # execute delete statement
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)

# Updating accounts
@bp.route('/<int:account_number>', methods = ['PATCH', 'PUT'])
def update(account_number:int):
    c = Customer.query.get_or_404(account_number)
    if (
        'username' not in request.json and 
        'password' not in request.json and
        'phonenumber' not in request.json and 
        'email' not in request.json and
        'name' not in request.json and 
        'signed_agreement' not in request.json):
        return abort(400)

    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        c.username = request.json['username']
    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        c.password = scramble(request.json['password'])
    if 'phonenumber' in request.json:
        if len(request.json['phonenumber']) > 12 or len(request.json['phonenumber']) < 7:
            return abort(400)
        c.phonenumber = request.json['phonenumber']
    if 'email' in request.json:
        c.email = request.json['email']
    if 'name' in request.json:
        c.name = request.json['name']
    if 'signed_agreement' in request.json:
        c.signed_agreement = request.json['signed_agreement']

    # Next feature: Create a statement that allows you to change the account_number as long as
    # there is not another customer with the same account number

    try:
        db.session.commit()
        return jsonify(c.serialize())
    except:
        return jsonify(False)
