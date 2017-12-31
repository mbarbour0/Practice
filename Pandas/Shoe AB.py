import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

utm_views = ad_clicks.groupby('utm_source')['user_id'].count().reset_index()

ad_clicks['is_click'] = ad_clicks['ad_click_timestamp'].apply(lambda x: 'True' if pd.notnull(x) else 'False')

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id')

clicks_pivot['percent_clicked'] = (clicks_pivot['True'] / (clicks_pivot['False'] + clicks_pivot['True'])) * 100

# Experimental pivot based on percentage clicked of type 'A' or 'B'
experimental_group = ad_clicks.groupby(['experimental_group', 'is_click']).count().reset_index()

experimental_pivot = experimental_group.pivot(columns = 'is_click', index = 'experimental_group', values = 'user_id')

experimental_pivot['percent_clicked'] = (experimental_pivot['True'] / (experimental_pivot['False'] + experimental_pivot['True'])) * 100

# A vs. B depending on day of the week
a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A']
b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B']

a_day = a_clicks.groupby(['day', 'is_click']).count().reset_index()

a_day_pivot = a_day.pivot(columns = 'is_click', index = 'day', values = 'user_id')

a_day_pivot['percent'] = (a_day_pivot['True'] / (a_day_pivot['False'] + a_day_pivot['True'])) * 100

b_day = b_clicks.groupby(['day', 'is_click']).count().reset_index()

b_day_pivot = b_day.pivot(columns = 'is_click', index = 'day', values = 'user_id')

b_day_pivot['percent'] = (b_day_pivot['True'] / (b_day_pivot['False'] + b_day_pivot['True'])) * 100

print a_day_pivot
