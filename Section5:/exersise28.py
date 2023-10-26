
list_a=[1,2,3,4]
list_b=[1,2,3,4]

x=[]

for i in list_a:
    if i in list_b:
        x.append(i)

print(x)
