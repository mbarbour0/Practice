import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.notnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(index = 'utm_source', columns = 'is_click', values = 'user_id').reset_index()
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[False] + clicks_pivot[True])

exp_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
exp_clicks = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
exp_pivot = exp_clicks.pivot(columns = 'is_click', index = 'experimental_group', values = 'user_id').reset_index()
exp_pivot['percent'] = exp_pivot[True] / (exp_pivot[True] + exp_pivot[False])

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'].reset_index()
a_click_group = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
a_pivot = a_click_group.pivot(index = 'day', columns = 'is_click', values = 'user_id').reset_index()
a_pivot['percent'] = a_pivot[True] / (a_pivot[False] + a_pivot[True])

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'].reset_index()
b_click_group = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
b_pivot = b_click_group.pivot(index = 'day', columns = 'is_click', values = 'user_id').reset_index()
b_pivot['percent'] = b_pivot[True] / (b_pivot[False] + b_pivot[True])

print(a_pivot)
print(b_pivot)
