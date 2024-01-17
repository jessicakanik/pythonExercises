# check if a leap year

year=2005

if (year % 4)!=0:
    print("Its a commen year")
elif (year % 100) != 0:
    print("It is a leap year")
elif (year % 400) != 0:
    print("Its a commen year")
else:
    print("Its a leap year")