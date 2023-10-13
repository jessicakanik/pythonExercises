import string

s = ("Hello")

is_pangram=True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False

print(is_pangram)



