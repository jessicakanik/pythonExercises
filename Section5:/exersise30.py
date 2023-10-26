my_list=[1,3]

# sort the list then find the second smallest

if len(my_list)>1:
    sorted_list=sorted(my_list)
    print(sorted_list[1])
else:
    print("None")