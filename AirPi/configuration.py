#!/usr/bin/python
import ConfigParser
import os
import sys
sys.path.append('../airchive')
from app import db, models


def set_database():
	config = ConfigParser.RawConfigParser()
	config.read('sensors.cfg')
	sensors = models.Sensors.query.all()
	quantities = models.Quantities.query.all()
	set_station()
	for sensor in config.sections():
		try:
			set_quantities(sensor,config, quantities)
			set_sensors(sensor, config, sensors)
		except:
			pass


def set_station():
	config = ConfigParser.RawConfigParser()
	config.read('station.cfg')
	stations = models.Stations.query.all()
	exist = False
	for station in config.sections():
		if config.get(station,"name") in [Tstation.name for Tstation in stations] and \
			config.get(station,"institution") in [Tstation.institution for Tstation in stations]:
			s = models.Stations.query.filter(models.Stations.name == config.get(station,"name")
			                                 , models.Stations.institution == config.get(station,"institution")).first()
			exist = True
		else:
			s = models.Stations()

		s.name = config.get(station,"name")
		s.station_url = config.get(station,"station_url")
		s.station_port = config.get(station,"station_port")
		s.latitude = config.get(station,"latitude")
		s.longitude = config.get(station,"longitude")
		s.institution = config.get(station,"institution")
        s.description = config.get(station, "description")
        s.admin_email = config.get(station, "admin_email")
        if exist:
			db.session.commit()
        else:
			db.session.add(s)
			db.session.commit()


def set_sensors(sensor, config, sensors):
	exist = False
	if config.get(sensor,"sensor_longName") in [Tsensor.long_name for Tsensor in sensors] and \
			config.get(sensor,"sensor_shortName") in [Tsensor.short_name for Tsensor in sensors] and \
			config.get(sensor,"sensor_URN") in [Tsensor.urn for Tsensor in sensors]:
		s = models.Sensors.query.filter(models.Sensors.long_name == config.get(sensor,"sensor_longName")
		                                ,models.Sensors.short_name == config.get(sensor,"sensor_shortName")
		                                ,models.Sensors.urn == config.get(sensor,"sensor_URN")).first()
		exist = True
	else:
		s = models.Sensors()

	quantity = models.Quantities.query.filter(models.Quantities.name == config.get(sensor,"measurement")).first()
	s.long_name = config.get(sensor,"sensor_longName")
	s.short_name = config.get(sensor,"sensor_shortName")
	s.manufacturer = config.get(sensor,"sensor_manufacturer")
	s.manufacturer_url = config.get(sensor,"sensor_manufacturerURL")
	s.urn = config.get(sensor,"sensor_URN")
	s.quantity_id = quantity.id

	if exist:
		db.session.commit()
	else:
		db.session.add(s)
		db.session.commit()


def set_quantities(sensor, config, quantities):
	exist = False
	if config.get(sensor,"ontology") in [Tquantity.ontology for Tquantity in quantities] and \
			config.get(sensor,"measurement") in [Tquantity.name for Tquantity in quantities]:
		q = models.Quantities.query.filter(models.Quantities.ontology == config.get(sensor,"ontology")
		                                   ,models.Quantities.measurement == config.get(sensor,"measurement")).first()
		exist = True
	else:
		q= models.Quantities()

	q.name = config.get(sensor,"measurement")
	q.ontology = config.get(sensor,"ontology")
	q.uom_name = config.get(sensor,"uom_name")
	q.uom_ontology = config.get(sensor,"uom_ontology")
	q.uom_symbol = config.get(sensor,"uom_symbol")

	if exist:
		db.session.commit()
	else:
		db.session.add(q)
		db.session.commit()


if __name__ == "__main__":
	set_database()