# string Exersises

# finding the length of a string
'''
s="Hello"
print(len(s))
'''
# print character at specific index
'''
s= "Hello"
i= 2

if len(s)==0 :
    print("Empty string ")
elif i < len(s):
    print(s[i])
else:
    print(" i is out of range")
'''
# printing the reverse

s="Hello"

# find the length of the list you take the last item in
# the string and then store it into new variable                                                                o

'''
my attempt

for i in range (len(s)) :
    x = len(s)-i
    y = ""
    y. append (s[x-1])
    print(y)
'''

'''
solutions
s="hello"
print(s[::-1])

they were using start stop and step method
'''
# first and last character string
# probalbly use the step rule

s= "Amazing"
if len(s)<6:
    print("")
else:
    print(s[0:3:1]+s[len(s)-3::1])




