# checking if a number is prime

n=1
x=0

for i in range (1,n+1):
    if n % i == 0:
        x+=1

if x == 2:
    print("Prime")
else:
    print("Not Prime")