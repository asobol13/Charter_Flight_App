from flask import Blueprint, jsonify, abort, request, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from ..models import Pilot, db

#Create a Form Class
class Form(FlaskForm):
    pilot_name = StringField("Name", validators=[DataRequired()])
    hourly_rate = StringField("Hourly Rate", validators=[DataRequired()])
    wait_time_rate = StringField("Wait Time Rate", validators=[DataRequired()])
    submit = SubmitField("Save")

# Creating blueprint
bp = Blueprint('pilots', __name__, url_prefix='/pilots')

# Index of pilots
@bp.route('/', methods=['GET'])
def index():
    pilots = Pilot.query.all()
    result = []
    for p in pilots:
        result.append(p.serialize())
    return render_template('pilots.html', result=result)

# Showing pilots
@bp.route('/view/<int:pilot_id>', methods=['GET'])
def show(pilot_id:int):
    p = Pilot.query.get_or_404(pilot_id)
    return render_template('showpilots.html', p=p)

# Adding new pilots
@bp.route('/create', methods=['POST', 'GET'])
def create():
    form = Form()
    # Construct pilot account
    if form.validate_on_submit():
        p = Pilot(
            pilot_name = request.form['pilot_name'],
            hourly_rate = request.form['hourly_rate'],
            wait_time_rate = request.form['wait_time_rate']
        )
        db.session.add(p) # Preparing create statement
        db.session.commit() # Executing create statement
        return redirect(url_for('pilots.index'))
    return render_template('createpilots.html', form=form)

# Deleting pilots
@bp.route('/delete/<int:pilot_id>', methods = ['POST', 'GET'])
def delete(pilot_id:int):
    p = Pilot.query.get_or_404(pilot_id)
    try:
        db.session.delete(p) # prepare delete statement
        db.session.commit() # execute delete statement
        return redirect(url_for('pilots.index'))
    except:
        # something went wrong
        flash("Oops, looks like there was a problem. Please try again!")
        return render_template("pilots.html", p=p)

# Updating pilots
@bp.route('/update/<int:pilot_id>', methods = ['GET', 'POST'])
def update(pilot_id:int):
    form = Form()
    p = Pilot.query.get_or_404(pilot_id)

    if request.method == "POST" and form.validate_on_submit():
        p.pilot_name = request.form['pilot_name']
        p.hourly_rate = request.form['hourly_rate']
        p.wait_time_rate = request.form['wait_time_rate']

    # Next feature: Create a statement that allows you to change the pilot_id as long as
    # there is not another pilot with the same id number

        try:
            db.session.add(p) # Preparing to update statement
            db.session.commit() # Executing update statement
            flash("Pilot Updated Successfully!")
            return redirect(url_for('pilots.index'))
        except:
            db.session.rollback()
            flash("Oops, looks like there was a problem. Please try again!")
            return render_template("updatepilots.html", form=form, p=p)
    return render_template("updatepilots.html", form=form, p=p)
