
list= [1,2,3,4]

user= input("enter the value you want to remove")
x=False
if list:
    for i in list:
        if str(i) == user:
            list.remove(i)
            x=True
    if x ==False:
        print("not in list")
else:
    print("empty")

print(list)
