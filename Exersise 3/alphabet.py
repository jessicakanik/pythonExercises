import string

s = "The quick brown fox jumped over the lazy dog"

is_pangram=True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False

print(is_pangram)



