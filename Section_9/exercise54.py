# solve the quadratice equation
import math

a=1
b=2
c=1

discriminant = b**2-4*a*c

if discriminant <0:
    print("Complex roots")
elif discriminant ==0:
    r=-b/(2*a)
    print(r)
else:
    r1=(-b - math.sqrt(discriminant))/(2*a)
    r2 = (-b + math.sqrt(discriminant)) / (2 * a)
    print(r1,r2)