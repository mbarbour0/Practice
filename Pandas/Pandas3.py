import pandas as pd

orders = pd.read_csv('orders.csv')

most_expensive = orders.price.max()
num_colors = orders.shoe_color.nunique()

# """
print(most_expensive)
print(num_colors)
# """

# print(orders.head(10))
