# flat file

xlist=[1,2,3],[4,5,6],[7,8,9]

x=[]

for i in xlist:
    if isinstance(i,list):
        for j in i:
            x.append(j)
    else:
        x.append(i)
print(x)