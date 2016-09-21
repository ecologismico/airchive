import sensor
import bmpBackend

class BMP085(sensor.Sensor):
	bmpClass = None
	requiredData = ["measurement","i2cbus"]
	optionalData = ["altitude","mslp","unit","sensor_longName", "sensor_shortName", "sensor_manufacturerURL",
	                "sensor_manufacturer", "sensor_URN", "ontology", "uom_name", "uom_ontology", "uom_symbol"]

	def __init__(self,data):
		self.sensorName = "BMP085"
		self.valName = data["measurement"]
		self.ontology = data["ontology"]
		self.valUnit = data["uom_name"]
		self.valUnitSymbol = data["uom_symbol"]
		self.uom_ontology = data["uom_ontology"]
		self.sensor_longName = data["sensor_longName"]
		self.sensor_shortName= data["sensor_shortName"]
		self.sensor_manufacturerURL = data["sensor_manufacturerURL"]
		self.sensor_manufacturer = data["sensor_manufacturer"]
		self.sensor_URN = data["sensor_URN"]
		if "pres" in data["measurement"].lower():
			self.altitude = 0
			self.mslp = False
			if "mslp" in data:
				if data["mslp"].lower in ["on","true","1","yes"]:
					self.mslp = True
					if "altitude" in data:
						self.altitude=data["altitude"]
					else:
						print "To calculate MSLP, please provide an 'altitude' config setting (in m) for the BMP085 pressure module"
						self.mslp = False
		if (BMP085.bmpClass==None):
			BMP085.bmpClass = bmpBackend.BMP085(bus=int(data["i2cbus"]))
		return

	def getVal(self):
		if "Temperature" in self.valName:
			temp = BMP085.bmpClass.readTemperature()
			if self.valUnit == "Fahrenheit":
				temp = temp * 1.8 + 32
			return temp
		elif "Pressure" in self.valName:
			if self.mslp:
				return BMP085.bmpClass.readMSLPressure(self.altitude) * 0.01 #to convert to Hectopascals
			else:
				return BMP085.bmpClass.readPressure() * 0.01 #to convert to Hectopascals
