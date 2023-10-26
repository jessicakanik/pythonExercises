list_a=[1,2,3,4]
list_b=[1,2]

# check if items in list a are in list b
output=[]

for i in list_a:
    if i not in list_b:
        output.append(i)

print(output)