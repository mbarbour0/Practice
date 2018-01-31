import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
df['Is taxed?'] = 'Yes'
df['Revenue'] = df['Price'] - df['Cost to Manufacture']

# df['Lowercase Name'] = df['Name'].apply(lower)


mylambda = lambda x: x[0] + x[-1]


mylambda = lambda x: 'Welcome to BattleCity!' if x >= 13 else "You must be over 13"


print(df.head())

"""get_last_name = lambda x: x.split(' ')[-1]
df['last_name'] = df['name'].apply(get_last_name)


total_earned = lambda row: row['hourly_wage'] * 40 + ((row['hours_worked'] - 40) * 1.5 * row['hourly_wage']) \
    if row['hours_worked'] > 40 else row['hourly_wage'] * row['hours_worked']
df['total_earned'] = df.apply(total_earned, axis = 1)


df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
df.rename(columns={'name': 'movie_title'}, inplace=True)

shoe_source = lambda row: 'vegan' if row['shoe_material'] != 'leather' else 'animal'
orders['shoe_source'] = orders.apply(shoe_source, axis=1)

salutation = lambda row: 'Dear Mr. ' + row['last_name'] if row['gender'] == 'male' else 'Dear Ms. ' + row['last_name']
orders['salutation'] = orders.apply(salutation, axis=1)"""
