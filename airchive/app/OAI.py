#!/usr/bin/python
import os, sys, ConfigParser
import json
from Overview import Overview
from QueryHandler import QueryHandler
import calendar
from datetime import datetime

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from app import db,models

basedir = os.path.abspath(os.path.dirname(__file__))


class OAI:

    def __init__(self, verb, fromtime = None, until = None
                 , metadataPrefix = None, set = None, resumptionToken = None):
        self.available_verbs = ['Identify', 'ListIdentifiers', 'ListMetadaFormats', 'ListRecords']
        self.sensors = models.Sensors.query.all()
        self.station = models.Stations.query.first()
        self.filters = ['mean', 'median', 'max', 'min']

        if verb in self.available_verbs:
            if verb == "Identify":
                self.template = "Identify.xml"


            elif verb == "DescribeSensor":
                self.sensor = models.Sensors.query.filter_by(urn = self.procedure).first()
                if self.sensor:
                    self.template = "DescribeSensor.xml"
                else:
                    self.template = "DescribeSensorException.xml"

            elif request == "GetObservation":
                self.template = "GetObservation.xml"


    def available_identifiers(self):
        
        self.available_ids = {}
        for sensor in models.Sensors.query.all():
            self.available_ids[sensor.quantity.name + '/' + sensor.short_name]= {}
            self.start_month = sensor.first_measurement.month
            self.start_year = sensor.first_measurement.year
        
            self.end_month = sensor.last_measurement.month
            self.end_year = sensor.last_measurement.year
            
            
            for year, month in self.month_year_iter(self.start_month, self.start_year, self.end_month, self.end_year):
                self.available_ids[sensor.quantity.name + '/' + sensor.short_name][calendar.month_name[month] + ' ' + str(year)] = {}
                for filter in self.filters:
                    self.available_ids[sensor.quantity.name + '/' + sensor.short_name][calendar.month_name[month] + ' ' + str(year)][filter] = {}
                    for day in range(1,calendar.monthrange(year,month)[1] +1 ):
                        
                        #fromtime and totime in datetime format
                        fromtime = datetime(year,month,day,0,0,0)
                        totime = datetime(year,month,day,23,59,59)
                        
                        #fromtime and totime in string format, so as they can be submited in QueryHandler
                        string_fromtime = datetime.strftime(fromtime,"%Y-%m-%d %H:%M:%S")
                        string_totime = datetime.strftime(totime,"%Y-%m-%d %H:%M:%S")
                        #format 'csv' doesnt make any difference heres
                        #If granularity is larger than the requested time(1d) I take average of the requested time
                        try:
                            value = QueryHandler(sensor.quantity.name, string_fromtime, string_totime, 'csv', self.station.name, sensor.urn, filter, "2d").submitQuery()

                        except:
                            db.session.rollback()
                            value = models.Measurements()
                            value.value = "NA"
                            value.station_id = self.station.id
                            value.quantity_id = sensor.quantity.id
                            value.sensor_id = sensor.id
                            value.timestamp = fromtime
                        self.available_ids[sensor.quantity.name + '/' + sensor.short_name][calendar.month_name[month] + ' ' + str(year)][filter][day] = value



        return self.available_ids

    def month_year_iter(self, start_month, start_year, end_month, end_year ):
        ym_start= 12*start_year + start_month - 1
        ym_end= 12*end_year + end_month - 1
        #for ym in range( ym_start, ym_end ):
        #if start_month == end_month function yields nothing
        for ym in range( ym_start, ym_end +1):
            y, m = divmod( ym, 12 )
            yield y, m+1