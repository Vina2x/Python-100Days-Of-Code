student_heights = input("Input a list of student heights \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height=0
for height in student_heights:
  total_height+=height

total_students=0
for students in student_heights:
  total_students+=1


avg_height= round(total_height/total_students)

print(avg_height)