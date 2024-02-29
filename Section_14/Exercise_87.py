file_path = "words.txt"

with open (file_path) as file:
    lines = file.readlines()
x=[]
for i in lines:
     x.append((i.strip("\n")))

dup= []
#
# for i in x:
#     for j in x:
#         if i == j :

fequ_dict = {}
