from dataitem import DataItem
import numpy as np
import math

# normal distribution
class Normal(DataItem):
	
	# constructor
	def __init__(self, simulator, mu, sigma):
		super(Normal, self).__init__(simulator, np.random.normal(mu, sigma, simulator.finesse))

# scalar number
class Scalar(DataItem):
	
	# constructor
	def __init__(self, simulator, scalar):
		super(Scalar, self).__init__(simulator,[scalar])

# skewed log normal distribution
class Skewed(DataItem):
	
	# constructor
	def __init__(self, simulator, median, skewness, tailDirection):
		if tailDirection not in ['right','left']:
			raise ValueError("tail direction must be either left or right")

		mu = math.log(max(abs(median),0.001)) # NEED max is nu omdat anders faalt op median = 0
		sigma = skewness
		samples = np.random.lognormal(mu, sigma, simulator.finesse)
		if tailDirection == 'left': # mirror samples around median
			samples = np.subtract(2*abs(median),samples)		
		if np.sign(median) == -1: # move samples to negative median
			samples = np.subtract(samples,2*abs(median))

		super(Skewed, self).__init__(simulator, samples)

# uniform distribution
class Uniform(DataItem):
	
	# constructor
	def __init__(self, simulator, lo, hi):
		super(Uniform, self).__init__(simulator, np.random.uniform(lo, hi, simulator.finesse))
