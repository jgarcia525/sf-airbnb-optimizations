import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


# makes a new list containing only floats, not lists that 
# contain lists with only one element/value
def removeListComplexity(currentList, rangeNum, maxValue):
	newList = list()

	for x in range(rangeNum):
		value = currentList[x]
		value = value[0]
		if (value < maxValue):
			newList.insert(x, value)

	return newList



prices = pd.read_csv('airbnb-sep-2017/listings.csv', usecols=[60])
# removes dollar sign and commas from price
prices = prices.replace('[\$,]', '',regex=True).astype(float) 
priceList = prices.values.tolist()
priceList = removeListComplexity(priceList, 1000, 2000.0)

# style and font for the graphs
style.use('fivethirtyeight')
csfont = {'fontname':'Fantasy'}


# Frequency of prices graph
plt.hist(priceList,  bins = 1000)
plt.title('Frequency of Prices in San Francisco', **csfont)
plt.ylabel('Frequency', **csfont)
plt.xlabel('Prices', **csfont)
plt.show()

# need to make price list again because some listings do not have 
#reviews
prices = pd.read_csv('airbnb-sep-2017/listings.csv', usecols=[60])
# removes dollar sign and commas from price
prices = prices.replace('[\$,]', '',regex=True).astype(float) 
priceList = prices.values.tolist()

# reviews are out of 100
reviews = pd.read_csv('airbnb-sep-2017/listings.csv', usecols=[79])
reviewList = reviews.values.tolist()
# reviewList = removeListComplexity(reviewList, 1000, 101)

priceList2 = list()
reviewList2 = list()

for x in range(1000):
	priceValue = priceList[x]
	priceValue = priceValue[0]
	reviewValue = reviewList[x]
	reviewValue = reviewValue[0]

	if (reviewValue != "nan"):
		priceList2.insert(x, priceValue)
		reviewList2.insert(x, reviewValue)

# Price and review corelation
plt.plot(reviewList,  bins = 1000)
plt.title('Price and Review Corelation', **csfont)
plt.ylabel('Review (out of 100)', **csfont)
plt.xlabel('Prices', **csfont)
plt.show()

