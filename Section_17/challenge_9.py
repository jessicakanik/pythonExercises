import datetime

date_input = input ("enter the first date: ")
date2_input = input ("enter the second date: ")

date_list = date_input.split(" ")
year_1 = int (date_list[0])
month1 = int (date_list [1])
day1 = int (date_list[2])

date1_object = datetime.date(year_1,month1,day1)

date2_list = date2_input.split(" ")
year_2=int(date2_list[0])
x