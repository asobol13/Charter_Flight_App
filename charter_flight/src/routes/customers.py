from flask import Blueprint, jsonify, abort, request, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField
from wtforms.widgets import PasswordInput
from wtforms.validators import DataRequired
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
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", widget=PasswordInput(hide_value=False),validators=[DataRequired()])
    signed_agreement = RadioField("Signed Agreement", coerce=bool, choices=[(1, 'True'), (0, 'False')], default=0)
    # signed_agreement = BooleanField("Signed Agreement", default=False)
    phonenumber = StringField("Phone Number", validators=[DataRequired()])
    email = StringField("Email")
    submit = SubmitField("Save")

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
@bp.route('/create', methods=['POST', 'GET'])
def create():
    form = Form()

#     # Request body must contain username, password and phone number
#     if 'username' not in request.json or 'password' not in request.json or 'phonenumber' not in request.json:
#         return redirect(url_for('index.html'))
#     if len(request.json['username']) < 3 or len(request.json['password']) < 8:
#         #return abort(400)
#         return redirect(url_for('index.html'))
    # Construct account
    if form.validate_on_submit():
        c = Customer(
            #.query.get_or_404
            name = form.name.data,
            username = form.username.data,
            password = form.password.data,
            signed_agreement = form.signed_agreement.data,
            phonenumber = form.phonenumber.data,
            email = form.email.data
        )
        db.session.add(c)
        db.session.commit()
        return redirect(url_for('customers.index'))
    return render_template('create.html', form=form)


# Deleting accounts
# @bp.route('/delete/<int:account_number>', methods = ['DELETE'])
# def delete(account_number:int):
#     c = Customer.query.get_or_404(account_number)
#     try:
#         db.session.delete(c) # prepare delete statement
#         db.session.commit() # execute delete statement
#         #return jsonify(True)
#         #return render_template('view.html',c=c)
#     except:
#         # something went wrong
#         return jsonify(False)

@bp.route('/delete/<int:account_number>', methods = ['POST', 'GET'])
def delete(account_number:int):
    c = Customer.query.get_or_404(account_number)
    try:
        db.session.delete(c) # prepare delete statement
        db.session.commit() # execute delete statement
        return redirect(url_for('delete.html'))
        #return jsonify(True)
        #return render_template('view.html',c=c)
    except:
        # something went wrong 
        flash("Oops, looks like there was a problem. Please try again!")
        return render_template("customers.html", c=c)

# Updating accounts
# @bp.route('/update/<int:account_number>', methods = ['PATCH', 'PUT'])
# def update(account_number:int):
#     c = Customer.query.get_or_404(account_number)
#     if (
#         'username' not in request.json and 
#         'password' not in request.json and
#         'phonenumber' not in request.json and 
#         'email' not in request.json and
#         'name' not in request.json and 
#         'signed_agreement' not in request.json):
#         return abort(400)

#     if 'username' in request.json:
#         if len(request.json['username']) < 3:
#             return abort(400)
#         c.username = request.json['username']
#     if 'password' in request.json:
#         if len(request.json['password']) < 8:
#             return abort(400)
#         c.password = scramble(request.json['password'])
#     if 'phonenumber' in request.json:
#         if len(request.json['phonenumber']) > 12 or len(request.json['phonenumber']) < 7:
#             return abort(400)
#         c.phonenumber = request.json['phonenumber']
#     if 'email' in request.json:
#         c.email = request.json['email']
#     if 'name' in request.json:
#         c.name = request.json['name']
#     if 'signed_agreement' in request.json:
#         c.signed_agreement = request.json['signed_agreement']

#     # Next feature: Create a statement that allows you to change the account_number as long as
#     # there is not another customer with the same account number

#     try:
#         db.session.commit()
#         #return jsonify(c.serialize())
#         #return render_template('view.html', c=c)
#     except:
#         return jsonify(False)

#TODO: Not updating, also boolean field is not populating
@bp.route('/update/<int:account_number>', methods = ['POST', 'GET'])
def update(account_number:int):
    c = Customer.query.get_or_404(account_number)
    form = Form()

    if request.method == "POST" and form.validate():
        c.name = request.form['name']
        c.username = request.form['username']
        c.password = request.form['password']
        c.signed_agreement = request.form['signed_agreement']
        c.phonenumber = request.form['phonenumber']
        c.email = request.form['email']
        # c.name = form.name.data,
        # c.username = form.username.data,
        # c.password = form.password.data,
        # c.signed_agreement = form.signed_agreement.data,
        # c.phonenumber = form.phonenumber.data,
        # c.email = form.email.data
        
        try:
            db.session.add(c)
            db.session.commit()
            flash("Customer Updated Successfully!")
            return render_template("customers.html", form=form, c=c)
        except:
            flash("Oops, looks like there was a problem. Please try again!")
            return render_template("update.html", form=form, c=c)
    else:
        return render_template("update.html", form=form, c=c)