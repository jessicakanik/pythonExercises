
list=[3,4,5,6]

s=""

for i in list:
    s+=str(i)

print(s)

# solution

for i in list:
    print(i, end=" ")

    # can use sep = ""