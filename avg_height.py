student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
sum_of_heights = 0
number_of_heights = 0
for height in student_heights:
    # print(height)
    sum_of_heights = sum_of_heights + height
    number_of_heights = number_of_heights + 1
print(f"Number of heights: {number_of_heights}, Sum of heigths: {sum_of_heights}")

average = sum_of_heights / number_of_heights
average_whole_number = round(average)
print(f"The average height is {average_whole_number}.")
