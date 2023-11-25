# Checking vowels and Consonants
text = "Score: 36"
vowels=["a","e","i","o","u"]
if not text:
    print("Empty String")
else:
    for char in text.lower():
        if char in ("a","i"'"o',"u","e"):
            print(f"{char} is a vowel")
        elif not char.isalpha():
            print(f"{char} is not a letter")
        else:
            print(f"{char} is a consonant")

