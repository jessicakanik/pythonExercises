# find the frequency of values in a dictionary
my_dict = {
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 }
freq_dict={}

array=[]
# getting all the values from a dictionary
for i in (my_dict.values()):
    array.append(i)

print(array)

for i in range (0,len(array)):
    if i==0:

