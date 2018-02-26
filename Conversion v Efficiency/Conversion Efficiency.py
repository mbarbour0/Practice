import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.style as style
style.use('fivethirtyeight')


# Reading Cognos Reports, Concatonating, and Writing to CSV
""" clt_cog = pd.read_excel('clt cog.xlsx')
orl_cog = pd.read_excel('orl cog.xlsx')
ls_cog = pd.read_excel('ls cog.xlsx')
twd_cog = pd.read_excel('twd cog.xlsx')
hours_by_agent = pd.concat([clt_cog, orl_cog, ls_cog, twd_cog])
hours_by_agent.to_csv('hours_by_agent.csv', index=False)
print(hours_by_agent.head()) """
# hours_by_agent = pd.read_csv('hours_by_agent.csv')


# Reading Unavailable Reason Code and Looking Up Hours Worked
""" hour_work = pd.read_excel('URC 10-15 to 12-7.xlsx')
hours_worked = hour_work.groupby('Agent Name')['Hours Worked'].sum().reset_index()
# print(hours_worked.head())
hours_worked.to_csv('hours_worked.csv', index=False) """

# Reading Hours Worked
""" hours_work_result = pd.read_csv('hours_worked.csv')
# print(hours_work_result.head()) """


# Reading Appointment Reports, Concatonating, and Writing to CSV
apt_1015 = pd.read_excel('October Appointments 10-15 to 10-20.xlsx')
apt_1022 = pd.read_excel('October Appointments 10-22 to 10-31.xlsx')
apt_111 = pd.read_excel('October Appointments 11-1 to 11-10.xlsx')
apt_1111 = pd.read_excel('October Appointments 11-11 to 11-20.xlsx')
apt_1121 = pd.read_excel('October Appointments 11-21 to 11-30.xlsx')
apt_121 = pd.read_excel('October Appointments 12-1 to 12-7.xlsx')
apt = pd.concat([apt_1015, apt_1022, apt_111, apt_1111, apt_1121, apt_121])
count_by_agent = apt.groupby(['Agent_Location', 'Agent_Name']).Textbox20.count().reset_index()
count_by_agent.to_csv('count_by_agent_location.csv', index=False)

# Reading Count by Agent
""" count_by_agent = pd.read_excel('count_by_agent.xlsx')
# print(count_by_agent.head()) """

# Reading Rankings and Saving Conversion to a Spreadsheet
""" ranking = pd.read_excel('Rankings.xlsx')
conversion = ranking.groupby('Agent')['Tableau Conversion'].sum().reset_index()
conversion.to_csv('conversion.csv', index=False)
print(conversion.head()) """

# Reading Conversion and Merging All Tables and Saving CSV
""" conversion_result = pd.read_csv('conversion.csv')
print(conversion_result.head())
conversion_v_hours = pd.merge(conversion_result, hours_work_result, how='left', left_on='Agent', right_on='Agent Name').reset_index()
print(conversion_v_hours.head())
conversion_v_hours_v_appointments = pd.merge(conversion_v_hours, count_by_agent, left_on='Agent', right_on='Agent_Name').reset_index()
print(conversion_v_hours_v_appointments.head())
conversion_v_hours_v_appointments.to_csv('conversion_v_hours_v_appointments.csv', index=False) """

# Run After Updating Conversion v Hours v Appointments
"""con_hour_app = pd.read_csv('conversion_v_hours_v_appointments.csv')
print(con_hour_app.head())"""

# Plotting
"""con_hour_app.plot(kind='scatter', x="Conversion", y="Appointments")
plt.tight_layout()
plt.savefig('Conversion by Appointment.png')

con_hour_app.plot(kind='scatter', x="Conversion", y="Hours", color='#ff7856')
plt.tight_layout()
plt.savefig('Conversion by Hours.png')

con_hour_app.plot(kind='scatter', x="Appointments", y="Hours", color='#42b73c')
plt.tight_layout()
plt.savefig('Appointments by Hours.png')
plt.show()
"""