#!/usr/bin/python
from app import app, models

app.run(host = models.Stations.query.first().station_url, port =models.Stations.query.first().station_port ,debug=True)
