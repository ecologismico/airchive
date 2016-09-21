#!/usr/bin/python
import calendar, os, sys
from datetime import datetime
import json
import re
from InvalidUsage import InvalidUsage
from filters import FilterMax, FilterMin, FilterAverageMean, FilterAverageMedian

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from app import db, models


class QueryHandler:
	"""
        Example call QueryHandler("Temperature","2006-02-22 14:35:00","2006-03-01 14:49:00", "csv", "NOA_Sensor", "Galatsi")
    """

	def __init__(self, quantity='', fromtime='', totime='', format='',
	             station='', sensor='', filter='', granularity='', page=''):
		# TODO this needs to be more dynamic - store in a table probably
		self.available_formats = {'georss': 'georss.xml', 'geojson': 'geojson.json'
			, 'sos': 'sos.xml', 'csv': 'csv.csv', 'flot': 'flot.json'}

		# TODO this needs to be more dynamic - store in a table probably
		self.available_filters = ['none', 'mean', 'median', 'max', 'min']

		self.page = 9999999
		# check quantity:
		if quantity is '':
			raise InvalidUsage('Quantity parameter is empty.')
		elif quantity not in [Tquantity.name for Tquantity in models.Quantities.query.all()]:
			raise InvalidUsage('Requested quantity is not supported.')
		else:
			self.quantity = models.Quantities.query.filter_by(name=quantity).first()

		if station is '':
			raise InvalidUsage('Station paremeter is empty.')
		elif station not in [Tstation.name for Tstation in models.Stations.query.all()]:
			raise InvalidUsage('Requested station is not supported')
		else:
			self.station = models.Stations.query.filter_by(name=station).first()

		if sensor is '':
			raise InvalidUsage('Sensor parameter is empty.')
		elif sensor not in [Tsensor.urn for Tsensor in models.Sensors.query.all()]:
			raise InvalidUsage('Requested sensor is not supported')
		else:
			self.sensor = models.Sensors.query.filter_by(urn=sensor).first()

		if filter is '':
			self.filter = 'none'
		elif filter.lower() not in self.available_filters:
			raise InvalidUsage('Requested filter is not supported')
		else:
			if granularity is '':
				self.granularity = "1h"
			self.filter = filter.lower()
			self.granularity = granularity

		if models.Sensors.query.filter_by(quantity_id=self.quantity.id).first().first_measurement is not None:

			# check fromtime:
			if fromtime is '':
				raise InvalidUsage('Fromtime parameter is empty.')
			else:
				# transform fromtime from string to datetime (easier comparisons
				# and db queries) fromtime format should be "2015-06-04 01:04:00"
				try:
					self.fromtime = datetime.strptime(fromtime, "%Y-%m-%d %H:%M:%S")
				except:
					raise InvalidUsage('Fromtime not in the correct format.')

				if (self.fromtime < models.Sensors.query.filter_by
					(quantity_id=self.quantity.id).first().first_measurement) \
						or (self.fromtime > models.Sensors.query.filter_by
							(quantity_id=self.quantity.id).first().last_measurement):
					raise InvalidUsage('Fromtime is out of boundaries.')

			if totime is '':
				# same as fromtime
				raise InvalidUsage('Totime parameter is empty')
			else:
				try:
					self.totime = datetime.strptime(totime, "%Y-%m-%d %H:%M:%S")
				except:
					raise InvalidUsage('Totime not in the correct format')

				if (self.totime < models.Sensors.query.filter_by
					(quantity_id=self.quantity.id).first().first_measurement) \
						or (self.totime > models.Sensors.query.filter_by
							(quantity_id=self.quantity.id).first().last_measurement):
					raise InvalidUsage('Totime is out of boundaries')

			if self.fromtime > self.totime:
				raise InvalidUsage('Fromtime > totime')
		else:
			raise InvalidUsage('Measurements with the give criteria does not exist')
		if format is '':
			raise InvalidUsage('Format parameter is empty')
		elif format not in self.available_formats.keys():
			raise InvalidUsage('Requested format is not supported')
		else:
			self.format = dict(type=format, file=self.available_formats[format]
			                   , content_type=self.available_formats[format].split('.')[1])
			# use regular expressions to check if page is in the correct format
			# to check that page is positive only int number I use: \D
		re1 = r'(\D)'
		if page is '':
			self.page = 1
		elif not re.findall(re1, page):
			self.page = int(page)

	def submitQuery(self):
		m = models.Measurements.query.filter(models.Measurements.quantity_id == self.quantity.id
		                                     , models.Measurements.station_id == self.station.id
		                                     , models.Measurements.sensor_id == self.sensor.id
		                                     , models.Measurements.timestamp >= self.fromtime
		                                     , models.Measurements.timestamp <= self.totime) \
			.order_by(models.Measurements.timestamp.asc()).paginate(self.page, 10, False)

		if self.filter == 'none':
			results = m
		elif self.filter == 'mean':
			results = FilterAverageMean.FilterAverageMean(m, self.granularity).apply()
		elif self.filter == 'median':
			results = FilterAverageMedian.FilterAverageMedian(m, self.granularity).apply()
		elif self.filter == 'max':
			results = FilterMax.FilterMax(m, self.granularity).apply()
		elif self.filter == 'min':
			results = FilterMin.FilterMin(m, self.granularity).apply()

		return results