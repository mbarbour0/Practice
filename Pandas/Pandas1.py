import pandas as pd

clothes = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print(clothes)

cities = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=['Store ID', 'Location', 'Number of Employees'])

print(cities)

# df = pd.read_csv('sample.csv')
# df = pd.read_csv('imdb.csv')
# print(df.head())
# print(df.info())

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df.clinic_north
clinic_north_south = df[['clinic_north', 'clinic_south']]
march = df.loc[2]
april_may_june = df.loc[3:6]
january = df[df.month == 'January']
march_april = df[(df.month == 'March') | (df.month == 'April')]
january_february_march = df[df.month.isin(['January', 'February', 'March'])]
df2 = df.loc[[1, 3, 5]]
df2.reset_index(inplace = True, drop = True)
