# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆
total_height=0
for height in student_heights:
  total_height+=height
# print(total_height)

total_students=0
for students in student_heights:
  total_students+=1
# print(total_students)

avg_height= total_height/total_students
print(f"The average height of the given list is {round(avg_height)}.")
  

#Write your code below this row 👇




