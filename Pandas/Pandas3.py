import pandas as pd
import numpy as np

orders = pd.read_csv('orders.csv')

most_expensive = orders.price.max()
num_colors = orders.shoe_color.nunique()
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()
expensive_shoes = orders.groupby('shoe_type').price.apply(lambda x: np.percentile(x, 75))
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
shoe_counts = shoe_counts.rename(columns={'id': 'counts'})


# print(most_expensive)
# print(num_colors)
# print(pricey_shoes)
# print(type(pricey_shoes))
# print(cheap_shoes)
# print(expensive_shoes)
print(shoe_counts)


# print(orders.head(10))
