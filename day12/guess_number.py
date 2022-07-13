# Number Guessing Game Objectives:
import random
from art import logo
difficulty_levels = {
    'easy': 10,
    'hard': 5,
}

print(logo)

difficulty = input("Do you want to play on 'hard' mode or 'easy' mode?: ")
lives = difficulty_levels[difficulty]
print(f"You are playing on hard mode with {lives} lives.")

answer = random.randint(1, 100)


# print(answer)

def guess(correct_number, user_guess):
    if user_guess > correct_number:
        return "Too high."
    elif user_guess < correct_number:
        return "Too low."
    else:
        return f"You got it! The answer was {correct_number}."


while lives != 0:
    player_guess = int(input("Guess a number between 1, 100: "))
    compare = guess(answer, player_guess)
    if compare == 'Too high.' or compare == 'Too low.':
        lives -= 1
    elif compare == f"You got it! The answer was {answer}.":
        lives = 0
        print("You won!")
    print(compare)
    if lives != 0:
        print(f"You have {lives} lives remaining.")
    elif compare != f"You got it! The answer was {answer}." and lives == 0:
        print("You have no lives left.")
        print("You lost.")
