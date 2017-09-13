from .map import Map
import time
import matplotlib
import matplotlib.pyplot as plt

# standard deviation map
STD = Map()
STD.SMALL = 1
STD.MEDIUM = 2
STD.LARGE = 3

# finesse map
FINESSE = Map()
FINESSE.SMALL = 1000
FINESSE.MEDIUM = 1e4
FINESSE.LARGE = 1e6

# skewness map
SKEWNESS = Map()
SKEWNESS.SMALL = 0.3
SKEWNESS.MEDIUM = 0.5
SKEWNESS.LARGE = 1

class Simulator:
	def __init__(self, finesse):
		self.finesse = finesse
		self.numOps = 0
		self.pltCounter = 1

		# set matplotlib color cycle to something prettier
		matplotlib.rcParams['axes.color_cycle'] = ['#ffaaa5','#a8e6cf','#dcedc1','#ff8b94','#ffd3b6']
	
	def addOps(self,num):
		self.numOps += num

	# start timer
	def start(self):
		self.startTime = time.time()

	# stop timer 
	def stop(self):
		self.stopTime = time.time()

	# show report and show plots
	def report(self):
		elapsedTime = int((self.stopTime-self.startTime))
		if self.numOps > 1e9:
			numOpsStr = str(int(self.numOps/1e9))+'G'
		elif self.numOps > 1e6:
			numOpsStr = str(int(self.numOps/1e6))+'M'
		elif self.numOps > 1e3:
			numOpsStr = str(int(self.numOps/1e3))+'k'
		else:
			numOpsStr = str(self.numOps)

		print('performed %s operations in %d seconds' % (numOpsStr,elapsedTime))
		
		# show plots
		plt.show()

	# @param2 (optional): title string
	def plot(self,varsToPlot,*args):
		
		# create plot
		plt.figure(self.pltCounter)
		self.pltCounter += 1

		# check if legend labels are present
		labels = []
		if len(args)>1:
			labels = args[1]

		# plot variables
		if isinstance(varsToPlot, list):
			for i in range(len(varsToPlot)):
				varToPlot = varsToPlot[i]
				if len(labels)>0:
					plt.hist(varToPlot.getData(), bins=30, label=labels[i])
				else:
					plt.hist(varToPlot.getData(), bins=30)

		else: # varsToPlot is one DataItem, not a list
			if len(labels)>0:
				plt.hist(varsToPlot.getData(), bins=30, label=labels)
			else:
				plt.hist(varsToPlot.getData(), bins=30)

		# set plot title if possible
		if len(args) > 0:
			titleStr = args[0]
			plt.title(titleStr)

		# show legend if necessary
		if len(labels) > 0:
			plt.legend()

