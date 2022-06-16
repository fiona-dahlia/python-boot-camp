print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
choice_one = input("You are at a fork. Do you want to turn 'left' or 'right': ")
choice_one_low = choice_one.lower()
if choice_one_low == "left":
    choice_two = input('You crossed the road. It lead you to a river. Do you want to "swim" or "wait": ')
    choice_two_low = choice_two.lower()
    if choice_two_low == "swim":
        print("As you were swimming, a current swept you out into the ocean. GAME OVER.")
    elif choice_two_low == "wait":
        choice_three = input(
            'You find a boat and get to the other side. There, you see three doors. Do you wish to open '
            'the "blue", "red", or "yellow" door: ')
        choice_three_low = choice_three.lower()
        if choice_three_low == "blue":
            print("You walked in and a tiger stared you down. GAME OVER.")
        elif choice_three_low == "red":
            print("You walked into a room of fire. GAME OVER.")
        elif choice_three_low == "yellow":
            print("You walked in and found a treasure chest full of gold coins and diamonds. YOU WIN!")
        else:
            print("Invalid response. GAME OVER.")
    else:
        print("Invalid response. GAME OVER.")
elif choice_one_low == "right":
    print("You were walking and ran into a dead end. A group of people kidnapped you. GAME OVER.")
else:
    print("Invalid response. GAME OVER.")

print("End of game, hope you enjoyed!")
