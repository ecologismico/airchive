#!/usr/bin/python
import output
import datetime
import sys
sys.path.append('../airchive')
from app import db,models

class Database(output.Output):
	requiredData = []
	optionalData = []
	def __init__(self,data):
		pass


	def outputData(self,dataPoints):
		for measures in dataPoints:
			m = models.Measurements()
			m.timestamp = datetime.datetime.now()
			m.value = measures["value"]
			sensor = models.Sensors.query.filter(models.Sensors.long_name == measures["sensor_longName"]
			                                     ,models.Sensors.short_name == measures["sensor_shortName"]
			                                     ,models.Sensors.manufacturer_url == measures["sensor_manufacturerURL"]
			                                     ,models.Sensors.manufacturer == measures["sensor_manufacturer"]
			                                     ,models.Sensors.urn == measures["sensor_URN"]).first()
			m.sensor_id = sensor.id
			quantity = models.Quantities.query.filter(models.Quantities.name == measures["quantity"]
			                                          ,models.Quantities.ontology == measures["ontology"]
			                                          ,models.Quantities.uom_name == measures["uom_name"]
			                                          ,models.Quantities.uom_ontology == measures["uom_ontology"]).first()
			m.quantity_id = quantity.id
			station = models.Stations.query.first()
			m.station_id = station.id
			db.session.add(m)
			db.session.commit()
		for sensor in models.Sensors.query.all():
			try:
				sensor.first_measurement =  models.Measurements.query.filter(models.Sensors.quantity_id == sensor.quantity_id)\
					.order_by(models.Measurements.timestamp.asc()).first().timestamp
				sensor.last_measurement = models.Measurements.query.filter(models.Sensors.quantity_id == sensor.quantity_id)\
					.order_by(models.Measurements.timestamp.desc()).first().timestamp
				db.session.commit()
			except:
				pass
		return True
