set1={1,2,3,4}
set2={4,5,6}

inter=set()

for i in set1:
    if i in set2:
        inter.add(i)

print(inter)