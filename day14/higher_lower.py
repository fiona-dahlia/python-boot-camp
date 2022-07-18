import random

import game_data
from art import logo, vs

# Print the logo.
print(logo)


# Use random.choice to pick a someone for choice a and choice b.
def data_layout_a(person):
    l_name = person["name"]
    l_description = person["description"]
    l_country = person["country"]
    # print(f'{l_name} has {person["follower_count"]}M followers.')
    return f'{l_name} is a {l_description}, from {l_country} with {person["follower_count"]}M followers'


def data_layout_b(person):
    l_name = person["name"]
    l_description = person["description"]
    l_country = person["country"]
    # print(f'{l_name} has {person["follower_count"]}M followers.')
    return f"{l_name} is a {l_description}, from {l_country}"


def choose_person(data):
    return random.choice(data)


def check(player_guess, choice_a_followers, choice_b_followers):
    if choice_a_followers > choice_b_followers:
        return player_guess == "a"
    else:
        return player_guess == "b"


def game():
    score = 0
    should_continue = True
    # While they haven't gotten any wrong, continue asking making choice b into choice a
    # and picking a new person for the new choice b.
    while should_continue:
        if score == 0:
            choice_a = choose_person(game_data.data)
        choice_b = choose_person(game_data.data)

        while choice_a == choice_b:
            choice_b = choose_person(game_data.data)

        print(f"Choice A: {data_layout_a(choice_a)}.")
        print(vs)
        print(f"Choice B: {data_layout_b(choice_b)}.")

        # Let the player type a or b to choice who they think has more followers.
        guess = input("Who do you think has more followers? Type 'A' or 'B': ").lower()
        a_followers = choice_a["follower_count"]
        b_followers = choice_b["follower_count"]
        is_it_correct = check(guess, a_followers, b_followers)

        # If they're correct let them know and show them their current score.
        print(f"Choice B: {data_layout_a(choice_b)}.")
        if is_it_correct:
            score += 1
            print(f"You're right! Your score is: {score}.")
            if guess == "b":
                choice_a = choice_b
        # If they're wrong say that they're wrong and print their final score.
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
        print("--------------------------------------------------------------------")


game()
