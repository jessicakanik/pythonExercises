file_path = "text.txt"

count = 0

with open (file_path) as file:
    for line in file:
        count += len (line.replace(' ',"").strip("\n"))

print(count)