# make a dictionary from a nested list

nested=[["a", 1], ["b", 2], ["c", 3], ["d", 4]]

my_dict={}
for i in nested:
    my_dict[i[0]]=i[1]
print(my_dict)