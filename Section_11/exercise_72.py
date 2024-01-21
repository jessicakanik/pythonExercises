n=7

if n % 2 == 0:
    print("Choose another number")
else:
    mid=(n+2)//2

    for i in range ( mid):
        print(" " * (mid-i), "*" * (i*2 +1)  )

    for i in range (mid -2,-1,-1):
        print(" " * (mid - i), "*" * (i * 2 + 1))
