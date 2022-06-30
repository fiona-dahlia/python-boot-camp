# Write your code below this line 👇

def prime_checker(number):
    factors = 0
    for i in range(2, number):
        if number % i == 0:
            # print(f"{i} is a factor of {number}")
            factors += 1
    print(factors)
    if factors == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
