# adding key values pair only if the key is not in the dictionary
my_dic={"January":45,"February":56,"March":67}
new_key={"April":67}

if new_key.key() in my_dic.key():
    print("true")
else:
    print("false")