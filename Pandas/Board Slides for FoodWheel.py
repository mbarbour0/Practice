from matplotlib import pyplot as plt
import pandas as pd

restaurants = pd.read_csv('restaurants.csv')
cuisine_options_count = restaurants.cuisine.nunique()
cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()
cuisines = cuisine_counts.cuisine
counts = cuisine_counts.name


print(restaurants)
print(cuisine_options_count)
print(cuisine_counts)

plt.pie(counts, labels = cuisines, autopct='%d%%')
plt.axis = 1
plt.show()
