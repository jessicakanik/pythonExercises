# area  of a triangel

base= int(input ("enter the base"))
height =int(input ("enter the height"))

if base> 0 and height >0:
    area = round((base*height)/2,2)
    print (f"The are of a triangle with base { base} and height {height} is: {area}")
else:
    print("Please enter a valid value for base and height")


