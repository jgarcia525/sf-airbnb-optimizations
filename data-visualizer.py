import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

df = pd.read_csv('airbnb-sep-2017/listings.csv', usecols=[60])
df = df.replace('[\$,]', '',regex=True).astype(float)
priceList = df.values.tolist()

# making a new list because priceList is a list of lists
# containing one float and I only want a list of floats
priceList2 = list()

for x in range(1000):
	dollar = priceList[x]
	dollar = dollar[0]

	if (dollar < 2000.0):
		priceList2.insert(x, dollar)

style.use('fivethirtyeight')
csfont = {'fontname':'Fantasy'}

plt.hist(priceList2, bins = 1000)
plt.title('Frequency of Prices in San Francisco', **csfont)
plt.ylabel('Frequency', **csfont)
plt.xlabel('Prices', **csfont)
plt.show()