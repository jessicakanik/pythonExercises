s ="Hello World"
new_s=''

words_list=s.split(" ")

for words in words_list:
    lowercase_word=words.lower()
    sorted_word= ''.join(sorted(lowercase_word))
    new_s+=sorted_word +" "

new_s.rstrip()
print(new_s)