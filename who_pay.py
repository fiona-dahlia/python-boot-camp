import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
length = len(names) - 1
random_number = random.randint(0, length)
person = names[random_number]
print(f"{person} will buy the meal today!")
