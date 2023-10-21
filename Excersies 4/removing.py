
list= []

new_list=[]
user= input("enter the value you want to remove")
x=False
if list:
    for i in list:
        if str(i) == user:
            x=True
        else:
            new_list.append(i)
    if x ==False:
        print("not in list")
else:
    print("empty")

print(new_list)
