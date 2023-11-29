# four seasons

season_num=["Spring","Summer","Fall","Winter"]

user_input=(int(input("Chose a number between 1 -4")))
user_input=user_input-1
if user_input<0 or user_input>4:
    print("Out of range")
else:
    print(season_num[user_input])