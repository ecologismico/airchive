import mcp3008
import sensor
class Analogue(sensor.Sensor):
	requiredData = ["adcPin","measurement","sensorName"]
	optionalData = ["pullUpResistance","pullDownResistance","sensor_longName", "sensor_shortName", "sensor_manufacturerURL",
	                "sensor_manufacturer", "sensor_URN", "ontology", "uom_name", "uom_ontology", "uom_symbol"]
	def __init__(self, data):
		self.adc = mcp3008.MCP3008.sharedClass
		self.adcPin = int(data["adcPin"])
		self.valName = data["measurement"]
		self.sensorName = data["sensorName"]
		self.pullUp, self.pullDown = None, None
		if "pullUpResistance" in data:
			self.pullUp = int(data["pullUpResistance"])
		if "pullDownResistance" in data:
			self.pullDown = int(data["pullDownResistance"])
		class ConfigError(Exception): pass
		if self.pullUp!=None and self.pullDown!=None:
			print "Please choose whether there is a pull up or pull down resistor for the " + self.valName + " measurement by only entering one of them into the settings file"
			raise ConfigError
		self.valUnit = data["uom_name"]
		self.valUnitSymbol = data["uom_symbol"]
		self.ontology = data["ontology"]
		self.uom_ontology = data["uom_ontology"]
		self.sensor_longName = data["sensor_longName"]
		self.sensor_shortName= data["sensor_shortName"]
		self.sensor_manufacturerURL = data["sensor_manufacturerURL"]
		self.sensor_manufacturer = data["sensor_manufacturer"]
		self.sensor_URN = data["sensor_URN"]
		
	def getVal(self):
		result = self.adc.readADC(self.adcPin)
		if result==0:
			print "Check wiring for the " + self.sensorName + " measurement, no voltage detected on ADC input " + str(self.adcPin)
			return None
		if result == 1023:
			print "Check wiring for the " + self.sensorName + " measurement, full voltage detected on ADC input " + str(self.adcPin)
			return None
		vin = 3.3
		vout = float(result)/1023 * vin
		
		if self.pullDown!=None:
			#Its a pull down resistor
			resOut = (self.pullDown*vin)/vout - self.pullDown
		elif self.pullUp!=None:
			resOut = self.pullUp/((vin/vout)-1)
		else:
			resOut = vout*1000
		return resOut
		
