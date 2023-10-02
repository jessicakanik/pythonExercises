file_name = " basic_file.txt "

# append the items in the file into the array

file_content=[]

with open (file_name) as file:
    for line in file:
        file_content.append(line)

print(file_content)


