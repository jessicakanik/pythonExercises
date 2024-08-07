# print calender

import calendar

print("welcome to your python calender")

year = int(input("enter the year (with this format YYYY): "))
month = int (input("now wnter the month(1-12): "))

print(calendar.month(year,month))

