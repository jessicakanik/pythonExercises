
s = "Hello"
s.lower()
length = len(s)

con = False

for l in range (0,length):
    if s[l] == "a" :
        con = True


print(con)
