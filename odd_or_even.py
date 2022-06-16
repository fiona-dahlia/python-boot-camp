# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

remainder = number % 2
if remainder == 1:
    print(f"The number {number} is odd.")
else:
    print(f"The number {number} is even.")