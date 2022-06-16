import random

print("Hello, welcome to the coin toss program.")
coin_flip = random.randint(0, 1)
# print(coin_flip)
if coin_flip == 0:
    print("You got Tails.")
else:
    print("You got Heads")
