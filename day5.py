import random

fruits = ['Apple', 'Peach', 'Pear']

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

index = random.randint(0, len(fruits) - 1)
print(index)
print(fruits[index])

print(random.choice(fruits))
