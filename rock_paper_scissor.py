import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ascii_list = [rock, paper, scissors]
ROCK = 0
PAPER = 1
SCISSOR = 2
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

print("Your choice: \n")
print(ascii_list[player_choice])

computer_choice = random.randint(0, 2)
print("Computer's choice: \n")
print(ascii_list[computer_choice])

if player_choice > 2 or player_choice < 0:
    print("Invalid choice, you lost.")
else:
    print("Your choice: \n")
    print(ascii_list[player_choice])

    if computer_choice == ROCK and player_choice == SCISSOR:
        print("You lost.")
    elif computer_choice == SCISSOR and player_choice == PAPER:
        print('You lost.')
    elif computer_choice == PAPER and player_choice == ROCK:
        print("You lost.")
    elif computer_choice == player_choice:
        print("It was a draw.")
    else:
        print("You win!")

