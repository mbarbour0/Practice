import pandas as pd

sales = pd.read_csv('sales.csv')
targets = pd.read_csv('targets.csv')
sales_vs_targets = pd.merge(sales, targets)
crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]
men_women = pd.read_csv('men_women_sales.csv')
all_data = sales.merge(targets).merge(men_women)
results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

print(sales.head(3))
print(targets.head(3))
print(sales_vs_targets.head(5))
print(crushing_it.head(5))
print(men_women.head(3))
print(all_data.head(3))
print(results.head(5))
