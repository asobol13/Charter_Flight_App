from flask import Blueprint, jsonify, abort, request, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, IntegerField
from wtforms.validators import DataRequired
from ..models import Aircraft, db

#Create a Form Class
class Form(FlaskForm):
    tail_number = StringField("Tail Number", validators=[DataRequired()])
    aircraft_name = StringField("Aircraft Name", validators=[DataRequired()])
    hourly_rate = StringField("Hourly Rate", validators=[DataRequired()])
    wait_time_rate = StringField("Wait Time Rate", validators=[DataRequired()])
    capacity = IntegerField("Capacity", validators=[DataRequired()])
    maintenance_date = StringField("Maintenance Date")
    fuel_load = StringField("Fuel Load")
    fuel_type = StringField("Fuel Type")
    aircraft_notes = StringField("Aircraft Notes")
    submit = SubmitField("Save")

# Creating blueprint
bp = Blueprint('aircrafts', __name__, url_prefix='/aircrafts')

# Index of aircrafts
@bp.route('/', methods=['GET'])
def index():
    aircrafts = Aircraft.query.all()
    result = []
    for a in aircrafts:
        result.append(a.serialize())
    return render_template('aircrafts.html', result=result)

# Showing aircrafts
@bp.route('/view/<tail_number>', methods=['GET'])
def show(tail_number):
    a = Aircraft.query.get_or_404(tail_number)
    return render_template('showaircrafts.html', a=a)

# Adding new aircrafts
@bp.route('/create', methods=['POST', 'GET'])
def create():
    form = Form()

    # Construct aircraft account
    if form.validate_on_submit():
        a = Aircraft(
            tail_number = request.form['tail_number'],
            aircraft_name = request.form['aircraft_name'],
            hourly_rate = request.form['hourly_rate'],
            wait_time_rate = request.form['wait_time_rate'],
            capacity = request.form['capacity'],
            maintenance_date = request.form['maintenance_date'],
            fuel_load = request.form['fuel_load'],
            fuel_type = request.form['fuel_type'],
            aircraft_notes = request.form['aircraft_notes']
        )
        db.session.add(a) # Preparing create statement
        db.session.commit() # Executing create statement
        return redirect(url_for('aircrafts.index'))
    return render_template('createaircrafts.html', form=form)

# Deleting aircrafts
@bp.route('/delete/<tail_number>', methods = ['POST', 'GET'])
def delete(tail_number):
    a = Aircraft.query.get_or_404(tail_number)
    try:
        db.session.delete(a) # prepare delete statement
        db.session.commit() # execute delete statement
        return redirect(url_for('aircrafts.index'))
    except:
        # something went wrong
        flash("Oops, looks like there was a problem. Please try again!")
        return render_template("aircrafts.html", a=a)

# Updating aircrafts
@bp.route('/update/<tail_number>', methods = ['GET', 'POST'])
def update(tail_number):
    form = Form()
    a = Aircraft.query.get_or_404(tail_number)

    if request.method == "POST" and form.validate_on_submit():
        a.aircraft_name = request.form['aircraft_name']
        a.hourly_rate = request.form['hourly_rate']
        a.wait_time_rate = request.form['wait_time_rate']
        a.capacity = request.form['capacity']
        a.maintenance_date = request.form['maintenance_date']
        a.fuel_load = request.form['fuel_load']
        a.fuel_type = request.form['fuel_type']
        a.aircraft_notes = request.form['aircraft_notes']

        try:
            db.session.add(a) # Preparing to update statement
            db.session.commit() # Executing update statement
            flash("Aircraft Updated Successfully!")
            return redirect(url_for('aircrafts.index'))
        except:
            db.session.rollback()
            flash("Oops, looks like there was a problem. Please try again!")
            return render_template("updateaircrafts.html", form=form, a=a)
    return render_template("updateaircrafts.html", form=form, a=a)
