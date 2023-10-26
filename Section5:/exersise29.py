my_list=[1,2]

# sort the list then find the second to last item

if len(my_list)>1:
    sorted_list=sorted(my_list)
    print(sorted_list[-2])
else:
    print("None")
