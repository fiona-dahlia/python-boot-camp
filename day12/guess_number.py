#Number Guessing Game Objectives:
import random
from art import logo
lives = -1
print(logo)
difficulty = input("Do you want to play on 'hard' mode or 'easy' mode?: ")
if difficulty == 'easy':
    lives = 10
    print(f"You are playing on easy mode with {lives} lives.")
else:
    lives = 5
    print(f"You are playing on hard mode with {lives} lives.")

answer = random.randint(1, 101)
# Allow the player to submit a guess for a number between 1 and 100.
def guess(correct_number, user_guess, amount_of_lives):
    if user_guess > correct_number:
        amount_of_lives -= 1
        return "Too high"
    elif user_guess < correct_number:
        amount_of_lives -= 1
        return "Too low"
    else:
        return "You got it!"

player_guess = int(input("Guess a number between 1, 100: "))
compare = guess(answer, player_guess, lives)
print(compare)
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.