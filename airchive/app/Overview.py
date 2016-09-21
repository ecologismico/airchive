#!/usr/bin/python
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from app import db,models


class Overview:

    def __init__(self):
        self.stations = models.Stations.query.all()
        self.quantities = models.Quantities.query.all()
        self.sensors = models.Sensors.query.all()
        self.available_formats = {'georss':'georss.xml', 'geojson':'geojson.json', 'sos':'sos.xml', 'csv':'csv.csv', 'flot':'flot.html'}

    def overview(self):
        dictionary = {}
        for station in self.stations:
            dictionary[station.name] = {}
            for quantity in self.quantities:
                try:

                    sensor = models.Sensors.query.filter_by(quantity_id = quantity.id).first()
                    first_timestamp = sensor.first_measurement
                    last_timestamp = sensor.last_measurement
                    dictionary[station.name][quantity.name] = {
	                     'Unit of Measure': quantity.uom_name
	                    , 'Unit of Measure symlol': quantity.uom_symbol
	                    , 'first measurement': first_timestamp
	                    , 'last measurement': last_timestamp
                        , 'sensor': sensor.long_name
                        , 'sensor URN': sensor.urn}

                except:
                    pass
        return dictionary

