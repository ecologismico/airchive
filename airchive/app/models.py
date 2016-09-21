#!/usr/bin/python
from app import db


class Measurements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    value = db.Column(db.String(120))
    
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensors.id'))
    station_id = db.Column(db.Integer, db.ForeignKey('stations.id'))
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantities.id'))
    
    def __repr__(self):
        return '<id %r>' % (self.id)


class Sensors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_name = db.Column(db.String(80))
    short_name = db.Column(db.String(60))
    manufacturer = db.Column(db.String(60))
    manufacturer_url = db.Column(db.String(140))
    urn = db.Column(db.String(60))
    first_measurement = db.Column(db.DateTime)
    last_measurement = db.Column(db.DateTime)
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantities.id'))
    
    measurement = db.relationship('Measurements', backref='sensor', lazy='dynamic')

    def __repr__(self):
        return '<Name %r>' % (self.short_name)


class Stations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    station_url = db.Column(db.String(140))
    station_port = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    institution = db.Column(db.String(80))
    description = db.Column(db.String(200))
    admin_email = db.Column(db.String(80))
    
    measurement = db.relationship('Measurements', backref='station', lazy='dynamic')
    
    def __repr__(self):
        return '<Name %r>' % (self.name)


class Quantities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    ontology = db.Column(db.String(80))
    uom_name = db.Column(db.String(40))
    uom_ontology = db.Column(db.String(80))
    uom_symbol = db.Column(db.String(20))

    measurement = db.relationship('Measurements', backref='quantity', lazy='dynamic')
    sensor = db.relationship('Sensors', backref='quantity', lazy='dynamic')

    def __repr__(self):
        return '<Name %r>' % (self.name)


