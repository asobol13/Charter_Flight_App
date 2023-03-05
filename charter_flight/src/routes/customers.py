from flask import Blueprint, jsonify, abort, request, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, PasswordField
from wtforms.validators import InputRequired
from ..models import Customer, db
import hashlib
import secrets

# Scramble function here
def scramble(password:str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

#Create a Form Class
class Form(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    signed_agreement = BooleanField("Signed Agreement")
    radiobutton = RadioField
    phonenumber = StringField("Phone Number", validators=[InputRequired()])
    email = StringField("Email")
    submit = SubmitField("Submit")

# Creating blueprint
bp = Blueprint('customers', __name__, url_prefix='/customers')

# Index of customers
@bp.route('/', methods=['GET'])
def index():
    customers = Customer.query.all()
    result = []
    for c in customers:
        result.append(c.serialize())
    return render_template('customers.html', result=result)

# Showing accounts
@bp.route('/view/<int:account_number>', methods=['GET'])
def show(account_number:int):
    c = Customer.query.get_or_404(account_number)
    return render_template('view.html', c=c)

# Creating accounts
# @bp.route('/create/', methods=['GET', 'POST'])
# def create():
#     # Request body must contain username, password and phone number
#     if 'username' not in request.json or 'password' not in request.json or 'phonenumber' not in request.json:
#         return redirect(url_for('index.html'))
#     if len(request.json['username']) < 3 or len(request.json['password']) < 8:
#         #return abort(400)
#         return redirect(url_for('index.html'))
#     # Construct account
#     if request.method =='POST':
#         c = Customer (
#             #account_number = request.json['account_number'],
#             name = request.form['name'],
#             signed_agreement = request.form['signed_agreement'],
#             username = request.form['username'],
#             password = scramble(request.form['password']),
#             phonenumber = request.form['phonenumber'],
#             email = request.form['email']
#         )
#         db.session.add(c) # Preparing create statement
#         db.session.commit() # Executing create statement
#         #return jsonify(c.serialize())
#         return redirect(url_for('view.html'))
#     return render_template('create.html', c=c)

@bp.route('/create', methods=['POST', 'GET'])
def create():
    form = Form(request.form)
    # Request body must contain username, password and phone number
    if 'username' not in request.json or 'password' not in request.json or 'phonenumber' not in request.json:
        return redirect(url_for('index.html'))
    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        #return abort(400)
        return redirect(url_for('index.html'))

    # Construct account
    if request.method == 'POST' and form.validate():
        c = Customer(form.name.data, form.username.data, form.password.data, form.signed_agreement.data,
            form.phonenumber.data, form.email.data)
        db.session.add(c)
        db.session.commit()
        return redirect(url_for('cusomters.html'))
    return render_template('create.html', form=form)


# Deleting accounts
@bp.route('/delete/<int:account_number>', methods = ['DELETE'])
def delete(account_number:int):
    c = Customer.query.get_or_404(account_number)
    try:
        db.session.delete(c) # prepare delete statement
        db.session.commit() # execute delete statement
        #return jsonify(True)
        #return render_template('view.html',c=c)
    except:
        # something went wrong
        return jsonify(False)

# Updating accounts
@bp.route('/update/<int:account_number>', methods = ['PATCH', 'PUT'])
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
        #return jsonify(c.serialize())
        #return render_template('view.html', c=c)
    except:
        return jsonify(False)
