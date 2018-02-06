import pandas as pd

bakery = pd.read_csv('bakery.csv')
ice_cream = pd.read_csv('ice_cream.csv')
menu = pd.concat([bakery, ice_cream])

print(bakery)
print(ice_cream)
print(menu)
