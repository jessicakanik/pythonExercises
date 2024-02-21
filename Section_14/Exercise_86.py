file_path = "basic_file.txt"

# with open (file_path) as file :
#     lines = file.readlines()
# x=[]
# for i in lines:
#     x=+i.strip("\n")
#
# for i in (0,len(x)+1):



longest_word = " "

with open (file_path) as file :
     for word in file:
         if len(word) > len (longest_word):
             longest_word = word

print(longest_word)
