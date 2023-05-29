# Write a Python program to subtract five days from current date
from datetime import timedelta,date
t1=date.today()
t2=timedelta(5)
t=t1-t2
print("Today is:",t1)
print("five days before current date:",t)