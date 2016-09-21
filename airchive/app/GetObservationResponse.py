#!/usr/bin/python


class GetObservationResponse:

	"""
	Objects of this class represent a response to a GetObservation request.
	There are the following fields:
	1. results: []
	2. exception: [bool]
	3. request: [dictionary]
	4. template: [string]
	4. exceptionDetails: [dictionary], {'exceptionName': 'NAME', 'exceptionFile': 'ResponseExceedsSizeLimit',
	 'exceptionMessage': 'this exception happened' }
	"""
	def __init__(self, observedProperty, procedure, offering, fromtime, totime, page, results, exception,
	             exceptionDetails, template):
		self.request = {}
		self.request['observedProperty'] = observedProperty
		self.request['procedure'] = procedure
		self.request['offering'] = offering
		self.request['fromtime'] = fromtime
		self.request['totime'] = totime
		self.request['page'] = page

		self.results = results

		self.template = template
		self.exception = exception
		self.exceptionDetails = exceptionDetails

		pass