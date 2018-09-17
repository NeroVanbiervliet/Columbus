<img style="width:100%;" src="/github-banner.png">

# Columbus

Columbus is a python package to simulate a series of uncertain events, such as a company's business plan. 

Let's take a look at the following code snippets from [example 1](/examples). Suppose you want to estimate the number of ice creams you will sell on a certain day to people passing by. You can create variables using datatypes representing **Normal** and **Skewed** distributions, as well as **Scalar** numbers. Don't mind the *sim* for now. 

```python
# usage of a normal distribution
chancePassengerBuysIceCream = Normal(sim, 0.05, 0.04)

# usage of a skewed distribution, right is the direction of the tail
numberOfPassingPeoplePerHour = Skewed(sim, 300, SKEWNESS.SMALL, 'right')

# usage of a scalar
numberOfHoursSelling = Scalar(sim, 8)
```

You can read more about the different datatypes [below](#Data-types). The code snippet below illustrates operations on variables such as **mul()** and **floor()**.

```python
iceCreamsSoldPerHour = chancePassengerBuysIceCream.mul(numberOfPassingPeoplePerHour)
# only keep samples that are > 0
iceCreamsSoldPerHourPositive = iceCreamsSoldPerHour.floor(0)
iceCreamsSoldTotal = iceCreamsSoldPerHourPositive.mul(numberOfHoursSelling)
```

Other operations such as adding and subtracting are also possible. You can read more about the operations [below](#operations). The only thing left to explain is the **sim** variable used above. It is used to set the simulation level of detail and can be used to plot variables.

```python
# start of simulation
sim = Simulator(int(1e4), 2e6) # simulator parameter specifies how fine grained the simulation will be, 1e4 is a reasonable value. 2e6 is the max memory consumption in [kb]
sim.start()

# intermediate calculations...

# plot the result
sim.plot(iceCreamsSoldTotal,'Number of sold icecreams','a label')

# end of simulation
sim.stop()
sim.report() # prints the number of calculations performed and the elapsed time
```
The plot looks like this:

<div style="text-align:center"><img style="width:100%;" src="/plot-demo.png"></div>

Check out the complete script for example 1 [here](/examples). You can also find more examples there. 

## Contents

- [Installation, dependencies and usage](#installation-dependencies-and-usage)
- [Data types](#data-types)
- [Operations](#operations)
- [Plotting](#plotting)

## Installation, Dependencies and Usage

To install Columbus, download the source and run the python installation script. For unix systems: 

```bash
sudo python setup.py install

```
Once this is done, it can be used in any script on your system. Columbus needs the following preinstalled modules to function properly: 
* matplotlib
* numpy

To use the Columbus library in a script, use the following imports: 
```python 

from columbus.simulator import FINESSE,STD,SKEWNESS,Simulator
from columbus.datatypes import Scalar, Normal, Skewed

```
## Data types

Columbus has several data types. All these data types are subject to the same operations, as described [below](#Operations)

### Scalar

A scalar is a fixed scalar number. It can be initialised as following:
`Scalar(simulatorObject, scalarValue)`

### Normal

Simulates a normal distribution. Initialisation:
`Normal(simulatorObject, mean, sigma)`

### Skewed distribution

Simulates a skewed distribution. Initialisation:
`Skewed(simulatorObject, mean, skewness, tailDirection)`. 
For the `skewness` parameter, predefined values from the `SKEWNESS` object can be used: `SKEWNESS.SMALL, SKEWNESS.MEDIUM or SKEWNESS.LARGE`. `tailDirection' is a string equal to *left* or *right*, indicating if the tail is to the left or to the right of the mean. 

### Uniform

Implementation of a uniform distribution. Initialisation:
`Uniform(simulatorObject, low, high)`. The parameters `low` and `high` are respectively the minimum and maximum size of the sampling domain.

## Operations

Data items supports the following basic arithmatic operations: 

* `.add(dataItem)`
* `.sub(dataItem)`
* `.mul(dataItem)`
* `.div(dataItem)`

DataItems can also be modified to remove all samples above or below a certain value: 

* `.floor(value)` removes all values below `value`
* `.ceil(value)` removes all values above `value`

DataItems can also be inverted (`invert()`) or rounded to the nearest int (`toInt()`).

**Note:** All operations have no effect on the dataItem they were performed on, they **return the result**. 

## Plotting

Columbus can plot all above mentioned data types. The syntax is as following:
```python
sim.plot(vars,title,labels)
```
with 
* `vars` either one variable or a list of variables
* `title` *optional* the title of the plot
* `labels` *optional* either one string or a list of strings 

## Calculating key figures

Columbus offers multiple descriptive statistics

* `mean()`
* `median()`
* `percentageSmallerThan(value)`
* `percentageLargerThan(value)`
