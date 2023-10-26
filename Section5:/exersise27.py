
from math import sqrt

point_a=[1,2,3]
point_b=[1,2,3]

x=(point_a[0]-point_b[0])^2
y=(point_a[1]-point_b[1])^2
z=(point_a[2]-point_b[2])^2

distance=sqrt(x+y+z)

print(distance)