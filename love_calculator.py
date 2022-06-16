# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

both_names = name1.lower() + ' ' + name2.lower()

# true - count
t_count = both_names.count("t")
r_count = both_names.count("r")
u_count = both_names.count("u")
e_count = both_names.count("e")
total_true = t_count + r_count + u_count + e_count

# love - count
l_count = both_names.count("l")
o_count = both_names.count("o")
v_count = both_names.count("v")
total_love = l_count + o_count + v_count + e_count

score = str(total_true) + str(total_love)
print(score)
score_integer = int(score)

if score_integer < 10 or score_integer > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score_integer <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")