# adding key values pair only if the key is not in the dictionary
my_dic={"January":45,"February":56,"March":67}
# new_key={"April":67}
#
# if new_key.key() in my_dic.key():
#     print("true")
# else:
#     print("false")

new_key="April"
new_value=67

if new_key not in my_dic:
    my_dic[new_key]=new_value
print(my_dic)
