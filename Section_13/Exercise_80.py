# counting vowels

vowels = ["a","e","o","i","u"]

total=0
def vowel_count (word):

    for i in word:
        for j in vowels:
            if i == j :
                total+=1

print(total)

vowel_count("python")

def count_vowels (string):
    string = string . lower()

    if not string:
        return 0
    elif string [0] in ("a","e","o","i","u"):
        return 1+ count_vowels(string[1:])
    else:
        return count_vowels(string[1:])
        





