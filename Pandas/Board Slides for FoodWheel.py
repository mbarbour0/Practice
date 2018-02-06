from matplotlib import pyplot as plt
import pandas as pd

restaurants = pd.read_csv('restaurants.csv')
cuisine_options_count = restaurants.cuisine.nunique()
cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()

print(restaurants)
print(cuisine_options_count)
print(cuisine_counts)
