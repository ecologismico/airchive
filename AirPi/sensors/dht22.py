import sensor
import dhtreader
import time
class DHT22(sensor.Sensor):
	requiredData = ["measurement","pinNumber"]
	optionalData = ["unit","sensor_longName", "sensor_shortName", "sensor_manufacturerURL",
	                "sensor_manufacturer", "sensor_URN", "ontology", "uom_name", "uom_ontology", "uom_symbol"]
	def __init__(self,data):
		dhtreader.init()
		dhtreader.lastDataTime = 0
		dhtreader.lastData = (None,None)
		self.sensorName = "DHT22"
		self.pinNum = int(data["pinNumber"])
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

	def getVal(self):
		tm = dhtreader.lastDataTime
		if (time.time()-tm)<2:
			t, h = dhtreader.lastData
		else:
			tim = time.time()
			try:
				t, h = dhtreader.read(22,self.pinNum)
			except Exception:
				t, h = dhtreader.lastData
			dhtreader.lastData = (t,h)
			dhtreader.lastDataTime=tim
		if "Temperature" in self.valName:
			temp = t
			if self.valUnit == "Fahrenheit":
				temp = temp * 1.8 + 32
			return temp
		elif "Humidity" in self.valName:
			return h
