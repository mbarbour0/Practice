import calendar

user_inp = input("Please enter MM/DD/YYYY: \n>>>").split("/")
year = int(user_inp[2])
day = int(user_inp[1])
month = int(user_inp[0])

a = calendar.weekday(year, month, day)
print(calendar.day_name[a].upper())