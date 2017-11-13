import panda as pd
import matplotlib.pyplot as plt

df = pd.read_excel("listings.csv", "Sheet1")
priceList = df['price'].values.tolist()

plt.hist(priceList, bins = 1000)
plt.title('Frequency of Prices in San Francisco')
plt.ylabel('Frequency')
plt.xlabel('Prices')
plt.show()

