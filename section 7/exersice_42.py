#print the max sum of values

my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}
max=0
for values in my_dict.values():
    x=(sum(values))

    if x>max:
        max=x

print(x)