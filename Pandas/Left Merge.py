import pandas as pd

store_a = pd.read_csv('store_a.csv')
store_b = pd.read_csv('store_b.csv')
store_a_b_left = pd.merge(store_a, store_b, how='left')
store_b_a_left = pd.merge(store_b, store_a, how='left')

print(store_a)
print(store_b)
print(store_a_b_left)
print(store_b_a_left)
