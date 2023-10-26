my_list=["a","a","b","c","a","b"]

freq_dic={}

for i in my_list:
    if i not in freq_dic:
        freq_dic[i]=1
    else:
        freq_dic[i]+=1

print(freq_dic)
