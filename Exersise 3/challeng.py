s= "Hello world"

word_list=s.split(" ")

new_s=" "

for word in word_list:
    reversed_word="".join(reversed(word))
    swapped_case= reversed_word.swapcase()
    new_s+=swapped_case + " "

