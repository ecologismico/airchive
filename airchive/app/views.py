#!/usr/bin/python
from flask import Flask, request, make_response, jsonify
from flask import render_template
from app import app
from QueryHandler import QueryHandler as q
from Overview import Overview as o
from OGC_SOS import OGC_SOS
from OAI import OAI
from InvalidUsage import InvalidUsage


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    return render_template('error.html', errorTitle=str(error.status_code), errorMessage=error.message)

@app.route('/home.html')
@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/Stations/')
def stations():
    over = o()
    return jsonify(over.overview())


@app.route('/Stations/<Station>')
def specific_stations(Station):
    over = o()
    if Station in [Tstation.name for Tstation in over.stations]:
        return jsonify(over.overview()[Station])
    else:
        raise InvalidUsage("Station " + Station + " not found.", status_code=404)  # 406: not acceptable


@app.route('/Stations/<Station>/<Quantity>')
def specific_stations_quantity(Station, Quantity):
    over = o()
    if Station in [Tstation.name for Tstation in over.stations] and Quantity in [Tquantity.name for Tquantity in over.quantities]:
        return jsonify(over.overview()[Station][Quantity])
    elif Station not in [Tstation.name for Tstation in over.stations]:
        raise InvalidUsage("Station " + Station + " not found.", status_code=404)  # 406: not acceptable
    else:
        raise InvalidUsage("Quantity " + Quantity+ " not found.", status_code=404)  # 406: not acceptable


@app.route('/getdata/')
def data():
    station = request.args.get('station', '')
    sensor = request.args.get('sensor', '')
    quantity = request.args.get('quantity','')
    fromTime = request.args.get('fromtime','')
    toTime = request.args.get('totime','')
    format = request.args.get('format','')
    filter = request.args.get('filter', '')
    granularity = request.args.get('granularity', '')
    page = request.args.get('page', '')
    
    try:
        query = q(quantity,fromTime,toTime,format.lower(),station, sensor, filter, granularity, page)
        data = query.submitQuery().items
        last_item = data.pop()
    except ValueError as err:
        return err.args[0]
    response = make_response(render_template(query.format['file'],last = last_item, results=data, station = query.station))

    response.headers["Content-Type"] = "application/%s"% query.format['content_type']
    if query.format['content_type'] == 'csv':
        response.headers['Content-Disposition'] = "attachment; filename=%s%s%s%s.csv" \
                                                  %(quantity.replace(' ' ,'_'), station.replace(' ' ,'-')
                                                    ,fromTime.replace(' ' ,'-'), toTime.replace(' ' ,'-'))
    return response


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/SensorObservationService')
def sensor_info():
    return render_template('SOS_Examples.html')

@app.route('/GraphicalUserInterface')
def gui():
    over = o()
    return render_template('gui.html',results = over.overview(), formats = over.available_formats)

@app.route('/oai/')
@app.route('/Oai/')
@app.route('/OAI/')
def oai():
    oai_verb = request.args.get('verb', '')
    oai_from = request.args.get('from', '')
    oai_until = request.args.get('until', '')
    oai_metadataPrefix = request.args.get('metadataPrefix', '')
    oai_set = request.args.get('set', '')
    oai_resumptionToken = request.args.get('resumptionToken', '')

    oai  = OAI(oai_verb, oai_from, oai_until, oai_metadataPrefix, oai_set, oai_resumptionToken)
    response = make_response(render_template(oai.template, station = oai.station))
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route("/oai/oai.xsl")

def xsl():
    response = make_response(render_template("oai.xsl"))
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/OpenArchiveInitiative')

def oai_examples():
    return render_template('OAI_Examples.html')


@app.route('/sos/')
@app.route('/Sos/')
@app.route('/sos/')
@app.route('/SOS/')
def sos():
    sos_request = request.args.get('request', '')
    sos_procedure = request.args.get('procedure', '')
    sos_offering = request.args.get('offering', '')
    sos_observedProperty = request.args.get('observedProperty', '')
    sos_eventTime = request.args.get('eventTime', '')
    sos_page = request.args.get('page', '')
    
    over = o()

    sos = OGC_SOS(sos_request, sos_procedure, sos_offering, sos_eventTime, sos_observedProperty, sos_page)
    getObservationResponse = sos.determineRequest()
    response = make_response(render_template(getObservationResponse.template,contact = sos.contact
                                             , keywords = sos.keywords, address = sos.address
                                             , contact_info = sos.contact_info, stations = sos.results
                                             , procedure = sos.procedure, sensor = sos.sensor, results = sos.results
                                             , all_stations = over.stations
                                             , all_sensors = over.sensors
                                             , GetObservationResponse = getObservationResponse))
    response.headers["Content-Type"] = "application/xml"
    
    return response