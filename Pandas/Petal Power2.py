import pandas as pd

inventory = pd.read_csv('inventory.csv')

staten_island = inventory[inventory.location == 'Staten Island']
product_request = staten_island.product_description.unique()
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)
inventory['total_value'] = inventory.price * inventory.quantity

inventory['full_description'] = inventory.apply(lambda row: '{} - {}'.format(row.product_type, row.product_description), axis = 1)

"""
print(product_request)

for i in product_request:
  print(i)

print(seed_request)
"""

print(inventory)
