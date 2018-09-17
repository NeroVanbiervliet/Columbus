import numpy as np
import random
import math

class DataItem(object):
	
	# constructor
	# dataArray is reduced in size if too large
	def __init__(self, simulator, dataArray):
		self.sim = simulator
		self.data = self.reduce(np.array(dataArray),self.sim.finesse)

	# get data array
	def getData(self):
		return self.data

	# adds an other data item to this data item and returns the result in a new data item
	def add(self, otherDataItem):
		otherData = otherDataItem.getData()
		selfData = self.data
		if len(otherData)*len(selfData) > self.sim.finesse:
			otherData = self.root(otherData)
			selfData = self.root(selfData)
		self.sim.addOps(len(selfData)*len(otherData)) # log operations
		outputData = []
		for i in range(len(otherData)):
			outputData.extend(np.add(selfData,otherData[i]))

		return DataItem(self.sim, outputData)

	# subtracts an other data item from this data item and returns the result in a new data item
	def sub(self, otherDataItem):
		return self.add(otherDataItem.invert())

	# multiplies an other data item with this data item and returns the result in a new data item
	def mul(self, otherDataItem):
		otherData = otherDataItem.getData()
		selfData = self.data
		if len(otherData)*len(selfData) > self.sim.finesse:
			otherData = self.root(otherData)
			selfData = self.root(selfData)
		self.sim.addOps(len(selfData)*len(otherData)) # log operations
		outputData = []
		for i in range(len(otherData)):
			outputData.extend(np.multiply(self.data,otherData[i]))

		return DataItem(self.sim, outputData)
	
	# divided this data item by an other data item and returns the result in a new data item
	def div(self, otherDataItem):
		otherData = otherDataItem.getData().astype(float)
		selfData = self.data
		if len(otherData)*len(selfData) > self.sim.finesse:
			otherData = self.root(otherData)
			selfData = self.root(selfData)
		self.sim.addOps(len(selfData)*len(otherData)) # log operations
		outputData = []
		for i in range(len(otherData)):
			outputData.extend(np.divide(self.data,otherData[i]))

		return DataItem(self.sim, outputData)

	# removes all values lower than the given value
	def floor(self, floorValue):
		return DataItem(self.sim, [s for s in self.data if s >= floorValue])

	# removes all values higher than the given value
	def ceil(self, ceilValue):
		return DataItem(self.sim, [s for s in self.data if s <= ceilValue])

	# converts all floats to nearest ints
	def toInt(self):
		return DataItem(self.sim, np.add(self.data,[0.5]*len(self.data)).astype(int))

	def invert(self):
		return DataItem(self.sim, np.multiply(self.data,-1))

	def mean(self):
		return np.mean(self.data)

	def median(self):
		return np.median(self.data)
	
	# returns the percentage of samples smaller then a reference value
	def percentageSmallerThan(self, value):
		return int(float((self.data < value).sum())/len(self.data)*100)

	def percentageLargerThan(self, value):
		return int(float((self.data > value).sum())/len(self.data)*100)
		

	# AUXILIARY FUNCTIONS
	
	def reduce(self, dataArray, finesse):
		if len(dataArray) > finesse:
			np.random.seed(0) # make choice pseudorandom
			return np.random.choice(dataArray, finesse)
		return dataArray

	def root(self, dataArray):
		if len(dataArray) > 1:
			return self.reduce(dataArray, int(math.sqrt(len(dataArray))))
		return dataArray

	
