import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

# makes a new list containing only floats, not lists that 
# contain lists with only one element/value
def removeListComplexity(currentList):
	newList = list()

	for x in range(len(currentList)):
		value = currentList[x]
		value = value[0]
		newList.insert(x, value)

	return newList

# Given the geo-location (latitude and longitude) of a new property, 
# estimates the weekly average income the homeowner can make with Airbnb.
def calculatePriceEstimation(currentLat, currentLong, 
	latitudeList, longitudeList, priceList):

	counter = 0
	priceTotal = 0
	for x in range(len(priceList)):
		if (currentLat + .005 >= latitudeList[x] and currentLat - .005 <= latitudeList[x]):
			if (currentLong + .005 >= longitudeList[x] and currentLong - .005 <= longitudeList[x]):
				counter += 1
				priceTotal += priceList[x]
	return (priceTotal * 7) / counter


latitudes = pd.read_csv('airbnb-sep-2017/listings.csv', usecols=[48])
latitudes = latitudes.astype(float)
latitudeList = latitudes.values.tolist()
latitudeList = removeListComplexity(latitudeList)

longitudes = pd.read_csv('airbnb-sep-2017/listings.csv', usecols=[49])
longitudes = longitudes.astype(float)
longitudeList = longitudes.values.tolist()
longitudeList = removeListComplexity(longitudeList)

prices = pd.read_csv('airbnb-sep-2017/listings.csv', usecols=[60])
prices= prices.replace('[\$,]', '',regex=True).astype(float)
priceList = prices.values.tolist()
priceList = removeListComplexity(priceList)

currentLat = 37.7562881782509
currentLong = -122.408737659274

priceEstimate = calculatePriceEstimation(currentLat, currentLong, latitudeList, longitudeList, priceList)
print(priceEstimate)






