#!/usr/bin/python
import os, sys, ConfigParser
import json
from Overview import Overview
from QueryHandler import QueryHandler
from GetObservationResponse import GetObservationResponse
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from app import db,models

basedir = os.path.abspath(os.path.dirname(__file__))


class OGC_SOS:

    def __init__(self, request, procedure = None, offering = None, eventTime = None, observedProperty = None,
                 page = None):
        self.available_requests = ['GetCapabilities', 'DescribeSensor', 'GetObservation']
        self.offering = offering
        self.eventTime = eventTime
        self.observedProperty = observedProperty
        self.contact = {}
        self.contact_info = {}
        self.address = {}
        self.keywords = []
        self.stations = []
        self.results = []
        self.procedure = procedure
        self.sensor = None
        self.page = page

        self.exception = False

        self.exceptionDetails = {}

        if request in self.available_requests:
            self.request = request

    def determineRequest(self):

            if self.request == "GetCapabilities":
                self.findKeywords()
                self.findInformation()
                self.findStations()
                self.template = "GetCapabilities.xml"
                self.results = self.renderCapabilities()

            elif self.request == "DescribeSensor":
                self.sensor = models.Sensors.query.filter_by(urn = self.procedure).first()
                if self.sensor:
                    self.template = "DescribeSensor.xml"
                else:
                    self.template = "DescribeSensorException.xml"

            elif self.request == "GetObservation":
                self.template = "GetObservation.xml"
                try:
                    self.fromtime = self.eventTime.split('/')[0]
                    self.totime = self.eventTime.split('/')[1]
                except:
                    self.exception = True
                    self.exceptionDetails['exceptionName'] = 'InvalidRequest'
                    self.exceptionDetails['locator'] = 'eventTime'
                    self.exceptionDetails['exceptionMessage'] = 'eventTime is not in the correct format'
                    self.exceptionDetails['exceptionFile'] = 'GetObservationException.xml'
                    self.template = 'GetObservationException.xml'

                    # give dummy values in case of exception
                    self.fromtime = ''
                    self.totime = ''

                    # raise ValueError('eventTime is not in the correct format')
                
                try:
                    self.URN = self.offering.split(':')[-1]
                except:
                    self.exception = True
                    self.exceptionDetails['exceptionName'] = 'InvalidRequest'
                    self.exceptionDetails['locator'] = 'offering'
                    self.exceptionDetails['exceptionMessage'] = 'offering is not in the correct format'
                    self.exceptionDetails['exceptionFile'] = 'GetObservationException.xml'
                    self.template = 'GetObservationException.xml'

                    #raise ValueError('offering is not in the correct format')
                
                q = QueryHandler(self.observedProperty, self.fromtime, self.totime, 'csv', self.URN, self.procedure,
                                 '', '', self.page)
                self.results = q.submitQuery()

                return GetObservationResponse(self.observedProperty, self.procedure, self.offering, self.fromtime,
                                              self.totime, self.page, self.results, self.exception,
                                              self.exceptionDetails, self.template)

    def findKeywords(self):
        [self.keywords.append(quantity.name) for quantity in models.Quantities.query.all()]

    def findInformation(self):
        config = ConfigParser.RawConfigParser()
        config.read('SOS_Information.cfg')
        for station in config.sections():
            self.contact = dict(title = config.get(station,'title'), description = config.get(station,'description'), provider_name= config.get(station,'provider_name'), provider_site=config.get(station,'provider_site'))
            self.contact_info = dict(name=config.get(station,'name'), voice=config.get(station,'voice'), fax=config.get(station,'fax'))
            self.address = dict(delivery_point = config.get(station,'delivery_point'), city = config.get(station,'city'), administration_area = config.get(station,'administration_area'), postal_code = config.get(station,'postal_code'), country = config.get(station,'country'))

    def findStations(self):
        [self.stations.append(station) for station in models.Stations.query.all()]

    def renderCapabilities(self):
        overview = Overview()
        return overview.overview()
