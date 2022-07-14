from random import choice
from art import logo, vs
from game_data import data

# Print the logo.
print(logo)
# Use random.choice to pick a someone for choice a and choice b.
choice_a = choice(data)
choice_b = choice(data)
print(f"""choice a: {choice_a}
{vs}
choice b: {choice_b}""")
# Use the vs art from art.py in between the two choices.
# Let the player type a or b to choice who they think has more followers.
# If they're correct let them know and show them their current score.
# If they're wrong say that they're wrong and print their final score.
# While they haven't gotten any wrong, continue asking making choice b into choice a and picking a new person for the new choice b.
