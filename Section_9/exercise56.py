# calculator

a=int(input("Enter a number"))
b=int(input("Enter a number"))

operation=int(input("1-add, 2-subtraction, 3-multiplication, 4-division, 5-integer division, 6-modulus"))

if operation == 1:
    print(a+b)
elif operation == 2:
    print(a-b)
elif operation == 3:
    print(a*b)
elif operation == 4:
    print(a/b)
elif operation == 5:
    print(a//b)
elif operation == 6:
    print(a%b)
else:
    print("please choose a valid operation")