my_dict = {
	"a": [2, 3, 4],
	"b": [3, 5, 7],
	"c": [1, 9, 10],
	"d": [1, 3, 4]
}

for list_value in my_dict.values():
    list_value.sort()

print(my_dict)
