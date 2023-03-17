from flask import Blueprint, jsonify, abort, request, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from ..models import Charter, db

#Create a Form Class
class Form(FlaskForm):
    departure_airport = StringField("Departure Airport", validators=[DataRequired()])
    destination_airport = StringField("Destination Airport", validators=[DataRequired()])
    departure_date = StringField("Departure Date", validators=[DataRequired()])
    return_date = StringField("Return Date")
    departure_time = StringField("Departure Time", validators=[DataRequired()])
    return_time = StringField("Return Time", validators=[DataRequired()])
    wait_hours = StringField("Wait Hours")
    flight_hours = StringField("Flight Hours")
    number_pax = IntegerField("Number of Passengers", validators=[DataRequired()])
    account_number = IntegerField("Customer Account Number", validators=[DataRequired()])
    tail_number = StringField("Tail Number", validators=[DataRequired()])
    pilot_id = IntegerField("Pilot Id", validators=[DataRequired()])
    submit = SubmitField("Save")

# Creating blueprint
bp = Blueprint('charters', __name__, url_prefix='/charters')

# Index of charters
@bp.route('/', methods=['GET'])
def index():
    charters = Charter.query.all()
    result = []
    for ch in charters:
        result.append(ch.serialize())
    return render_template('charters.html', result=result)

# Showing charters
@bp.route('/view/<int:charter_number>', methods=['GET'])
def show(charter_number:int):
    ch = Charter.query.get_or_404(charter_number)
    return render_template('showcharters.html', ch=ch)

# Creating accounts
@bp.route('/create', methods=['POST', 'GET'])
def create():
    form = Form()

    # Construct charter trip
    if form.validate_on_submit():
        ch = Charter(
            departure_airport = request.form['departure_airport'],
            destination_airport = request.form['destination_airport'],
            departure_date = request.form['departure_date'],
            return_date = request.form['return_date'],
            departure_time = request.form['departure_time'],
            return_time = request.form['return_time'],
            wait_hours = request.form['wait_hours'],
            flight_hours = request.form['flight_hours'],
            number_pax = request.form['number_pax'],
            account_number = request.form['account_number'],
            tail_number = request.form['tail_number'],
            pilot_id = request.form['pilot_id']
        )
        db.session.add(ch) # Preparing create statement
        db.session.commit() # Executing create statement
        return redirect(url_for('charters.index'))
    return render_template('createcharter.html', form=form)

# Deleting charter trips
@bp.route('/delete/<int:charter_number>', methods = ['POST', 'GET'])
def delete(charter_number:int):
    ch = Charter.query.get_or_404(charter_number)
    try:
        db.session.delete(ch) # prepare delete statement
        db.session.commit() # execute delete statement
        return redirect(url_for('charters.index'))
    except:
        # something went wrong
        flash("Oops, looks like there was a problem. Please try again!")
        return render_template("charters.html", ch=ch)

# Updating charter trips
@bp.route('/update/<int:charter_number>', methods = ['GET', 'POST'])
def update(charter_number:int):
    form = Form()
    ch = Charter.query.get_or_404(charter_number)

    if request.method == "POST" and form.validate_on_submit():
        ch.departure_airport = request.form['departure_airport']
        ch.destination_airport = request.form['destination_airport']
        ch.departure_date= request.form['departure_date']
        ch.return_date = request.form['return_date']
        ch.departure_time = request.form['departure_time']
        ch.return_time = request.form['return_time']
        ch.wait_hours = request.form['wait_hours']
        ch.flight_hours = request.form['flight_hours']
        ch.number_pax = request.form['number_pax']
        ch.account_number = request.form['account_number']
        ch.tail_number = request.form['tail_number']
        ch.pilot_id = request.form['pilot_id']

        try:
            db.session.add(ch) # Preparing to update statement
            db.session.commit() # Executing update statement
            flash("Charter Updated Successfully!")
            return redirect(url_for('charters.index'))
        except:
            db.session.rollback()
            flash("Oops, looks like there was a problem. Please try again!")
            return render_template("updatecharter.html", form=form, ch=ch)
    return render_template("updatecharter.html", form=form, ch=ch)
