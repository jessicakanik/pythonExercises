
s = "the quick brown fox jumped over the lazy fox"
s.lower()
length = len(s)

con = False

for l in range (0,length):
    if s[l] == "a" :
        con = True


print(con)
