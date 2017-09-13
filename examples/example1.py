# appropriate imports
from columbus.simulator import FINESSE,STD,SKEWNESS,Simulator
from columbus.datatypes import Scalar, Normal, Skewed

# initiate simulator 
sim = Simulator(int(1e4),2e6) # simulator parameter specifies how fine grained the simulation will be, 1e4 is a reasonable value
sim.start()

# usage of a normal distribution
chancePassengerBuysIceCream = Normal(sim, 0.05, 0.04)

# usage of a skewed distribution																																							
numberOfPassingPeoplePerHour = Skewed(sim, 300, SKEWNESS.SMALL, 'right')

# usage of a scalar
numberOfHoursSelling = Scalar(sim, 8)

iceCreamsSoldPerHour = chancePassengerBuysIceCream.mul(numberOfPassingPeoplePerHour)
iceCreamsSoldPerHour = iceCreamsSoldPerHour.floor(0)
iceCreamsSoldTotal = iceCreamsSoldPerHour.mul(numberOfHoursSelling)
																												
# plot the result
sim.plot(iceCreamsSoldTotal,'Number of sold icecreams','a label')

# end of simulation
sim.stop()
sim.report()																																																																							
