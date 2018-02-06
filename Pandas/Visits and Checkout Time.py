import pandas as pd

visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])
v_to_c = pd.merge(visits, checkouts)
v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time

print(visits)
print(checkouts)
print(v_to_c)
print(v_to_c.time.mean())
