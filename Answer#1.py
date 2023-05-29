"""
1. Write a Python script to display the
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week 
"""
import datetime
current_datetime=datetime.datetime.now()
print(current_datetime)
print("current year:",current_datetime.year)
print("current Month:",current_datetime.month)
print("current Week number of the year:", current_datetime.strftime("%W"))
print("current Weekday of the week:", current_datetime.strftime("%w"))
print("current Day of year:", current_datetime.strftime("%j"))
print("current Day of the month:", current_datetime.strftime("%d"))
print("current Day of the Week:", current_datetime.strftime("%A"))






