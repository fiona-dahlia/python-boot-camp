# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age_int = int(age)

years_left = 90 - age_int
print(f"You have years left: {years_left}")

weeks_left = years_left * 52
print(f"You have weeks left: {weeks_left}")

months_left = years_left * 12
print(f"You have months left: {months_left}")

days_left = years_left * 365
print(f"You have days left: {days_left}")