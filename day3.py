print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age: "))
    if age <= 12:
        bill = 5
        print("Your ticket costs $5.")
    elif age <= 18:
        bill = 7
        print("Your ticket costs $7.")
    elif age <= 45 and age >= 55:
        bill = 0
        print('Your ticket is free.')
    elif age > 18:
        bill = 12
        print("Your ticket costs $12.")

    photo = input("Do you want a photo? Type 'Y' or 'N': ")
    if photo == "Y":
        bill += 3
    print(f"Your bill is ${bill}.")
else:
    print("You have to grow taller before you can ride.")
