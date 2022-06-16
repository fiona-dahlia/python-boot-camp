# 🚨 Don't change the code below 👇
height = input("enter your height in inches: ")
weight = input("enter your weight in lb: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_float = float(height)
weight_float = float(weight)
bmi = weight_float / (height_float ** 2)
print(f"Your BMI is {bmi}.")

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

if bmi <= 18.5:
    print("You are underweight.")
elif bmi <= 25:
    print("You have a normal weight.")
elif bmi <= 30:
    print("You are slightly overweight.")
elif bmi <= 35:
    print("You are obese.")
else:
    print("You are clinically obese.")
