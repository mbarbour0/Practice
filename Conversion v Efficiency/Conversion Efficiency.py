import pandas as pd
from matplotlib import pyplot as plt

clt_cog = pd.read_excel('clt cog.xlsx')
orl_cog = pd.read_excel('orl cog.xlsx')
ls_cog = pd.read_excel('ls cog.xlsx')
twd_cog = pd.read_excel('twd cog.xlsx')
apt_101 = pd.read_excel('October Appointments 10-1 to 10-20(1).xlsx')
apt_1022 = pd.read_excel('October Appointments 10-22 to 10-31.xlsx')
apt_111 = pd.read_excel('October Appointments 11-1 to 11-10.xlsx')
apt_1111 = pd.read_excel('October Appointments 11-11 to 11-20.xlsx')
apt_1121 = pd.read_excel('October Appointments 11-21 to 11-30.xlsx')
apt_121 = pd.read_excel('October Appointments 12-1 to 12-31.xlsx')

apt = pd.concat([apt_101, apt_1022, apt_111, apt_1111, apt_1121, apt_121])

# October Appointments 10-22 to 10-31
# print(clt_cog.head())
# print(ls_cog.head())
# print(orl_cog.head())
# print(twd_cog.head())

print(apt.head())
