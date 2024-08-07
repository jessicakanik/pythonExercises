# body max index

print("Welcome to the body max index calculator")

height = float (input (" please enter your height (cm): "))

weight = float (input("Now enter your weigh (kg): "))

height_m = height / 100

BMI = round (weight/(height_m ** 2),2 )

print(f"BMI: {BMI}")

print ("Your result is:", end=" ")

if BMI <18.5:
    print("Underweight")
elif (BMI == 18.5 ) or (BMI <= 24.9) :
    print("normal")
elif 25<BMI <= 29.9 :
    print ("Overweight ")
else:
    print("obesity")

