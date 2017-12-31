import pandas as pd

inventory = pd.read_csv('inventory.csv')

staten_island = inventory[inventory['location'] == 'Staten Island']

product_request = staten_island['product_description']

seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

inventory['in_stock'] = inventory['quantity'].apply(lambda x: True if x > 0 else False)

inventory['total_value'] = inventory.apply(lambda row: row['quantity'] * row['price'], axis = 1)

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)
  
print inventory
