from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Setting up the class for customers table
class Customer(db.Model):
    __tablename__ = 'customers'
    account_number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    signed_agreement = db.Column(db.Boolean, nullable=False, default=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    phonenumber = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=True, default=None)
    
    # Initializing the customers table
    def __init__(self, name:str, signed_agreement:bool, 
    username:str, password:str, phonenumber:str, email:str):
        self.name = name
        self.signed_agreement = signed_agreement
        self.username = username
        self.password = password
        self.phonenumber = phonenumber
        self.email = email

    # Returning customers table into json
    def serialize(self):
        return {
            'account_number' : self.account_number,
            'name': self.name,
            'signed_agreement': self.signed_agreement,
            'username': self.username,
            'password': self.password,
            'phonenumber': self.phonenumber,
            'email': self.email
        }

# Setting up the class for charters table
class Charter(db.Model):
    __tablename__ = 'charters'
    charter_number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    departure_airport = db.Column(db.String(50), nullable = False)
    destination_airport = db.Column(db.String(50), nullable = False)
    departure_date = db.Column(db.String(20), nullable = False)
    return_date = db.Column(db.String(20), nullable = True)
    departure_time = db.Column(db.String(20), nullable = False)
    return_time = db.Column(db.String(20), nullable = False)
    wait_hours = db.Column(db.String(20), nullable = True)
    flight_hours = db.Column(db.String(20), nullable = True)
    number_pax = db.Column(db.Integer, nullable = False)
    account_number = db.Column(db.Integer, db.ForeignKey('customers.account_number'), nullable=False)
    tail_number = db.Column(db.String(10), db.ForeignKey('aircrafts.tail_number'), nullable=False)
    pilot_id = db.Column(db.Integer, db.ForeignKey('pilots.pilot_id'), nullable=False)

    # Initializing the charters table
    def __init__(self, departure_airport:str, destination_airport:str,
    departure_date:str, return_date:str, departure_time:str,
    return_time:str, wait_hours:str, flight_hours:str,
    number_pax:int, account_number:int, tail_number:int, pilot_id:int):
        self.departure_airport = departure_airport
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date
        self.departure_time = departure_time
        self.return_time = return_time
        self.wait_hours = wait_hours
        self.flight_hours = flight_hours
        self.number_pax = number_pax
        self.account_number = account_number
        self.tail_number = tail_number
        self.pilot_id = pilot_id

    # Returning charters table into json
    def serialize(self):
        return {
            'charter_number': self.charter_number,
            'departure_airport': self.departure_airport,
            'destination_airport': self.destination_airport,
            'departure_date': self.departure_date,
            'return_date': self.return_date,
            'departure_time': self.departure_time,
            'return_time': self.return_time,
            'wait_hours': self.wait_hours,
            'flight_hours': self.flight_hours,
            'number_pax': self.number_pax,
            'account_number': self.account_number,
            'tail_number': self.tail_number,
            'pilot_id': self.pilot_id
        }

# Setting up the class for aircrafts table
class Aircraft(db.Model):
    __tablename__ = 'aircrafts'
    tail_number = db.Column(db.String(10), primary_key=True)
    aircraft_name = db.Column(db.String(50), unique=True, nullable=False)
    hourly_rate = db.Column(db.String(10), nullable=False)
    wait_time_rate = db.Column(db.String(10), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    maintenance_date = db.Column(db.String(255), nullable=True)
    fuel_load = db.Column(db.String(255), nullable=True)
    fuel_type = db.Column(db.String(255), nullable=True)
    aircraft_notes = db.Column(db.String(500), nullable=True)

    # Initializing the aircrafts table
    def __init__(self, tail_number:str, aircraft_name:str, hourly_rate:int, wait_time_rate:int,
    capacity:int, maintenance_date:str, fuel_load:str, fuel_type:str, aircraft_notes:str):
        self.tail_number = tail_number
        self.aircraft_name = aircraft_name
        self.hourly_rate = hourly_rate
        self.wait_time_rate = wait_time_rate
        self.capacity = capacity
        self.maintenance_date = maintenance_date
        self.fuel_load = fuel_load
        self.fuel_type = fuel_type
        self.aircraft_notes = aircraft_notes

    # Returning aircrafts table into JSON
    def serialize(self):
        return{
            'tail_number': self.tail_number,
            'aircraft_name': self.aircraft_name,
            'hourly_rate': self.hourly_rate,
            'wait_time_rate': self.wait_time_rate,
            'capacity': self.capacity,
            'maintenance_date': self.maintenance_date,
            'fuel_load': self.fuel_load,
            'fuel_type':self.fuel_type,
            'aircraft_notes':self.aircraft_notes
        }

# Setting up the class for pilots table
class Pilot(db.Model):
    __tablename__ = 'pilots'
    pilot_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pilot_name= db.Column(db.String(50), nullable=False)
    hourly_rate = db.Column(db.String(10), nullable=False)
    wait_time_rate = db.Column(db.String(10), nullable=False)

    # Initializing the class pilos
    def __init__(self, pilot_name:str, hourly_rate:str, wait_time_rate:str):
        self.pilot_name = pilot_name
        self.hourly_rate = hourly_rate
        self.wait_time_rate = wait_time_rate

    # Returning pilots table into JSON
    def serialize(self):
        return{
            'pilot_id': self.pilot_id,
            'pilot_name': self.pilot_name,
            'hourly_rate': self.hourly_rate,
            'wait_time_rate': self.wait_time_rate
        }
