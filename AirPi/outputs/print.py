import output
import datetime

class Print(output.Output):
	requiredData = []
	optionalData = []
	def __init__(self,data):
		pass
	def outputData(self,dataPoints):
		print ""
		print "Time: " + str(datetime.datetime.now())
		for i in dataPoints:
			print i["quantity"] + ": " + str(i["value"]) + " " + i["uom_symbol"]
		return True
