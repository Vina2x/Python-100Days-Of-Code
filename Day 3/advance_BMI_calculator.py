print("Welcome to the BMI calculator!!!")
height= float(input("Enter your height in m:\n"))
weight= float(input("Enter your weight in kg:\n"))
bmi= weight/(height**2)
new_bmi= float("{:.2f}".format(bmi))
if new_bmi<18.5:
    print(f"Your BMI is:{new_bmi}, You are underweight.")
elif new_bmi<25:
    print(f"Your BMI is:{new_bmi}, You have healthy weight.")
elif new_bmi<30:
    print(f"Your BMI is:{new_bmi}, You are overweight.")
elif new_bmi<35:
    print(f"Your BMI is:{new_bmi}, You are obese.")
else:
    print(f"Your BMI is:{new_bmi}, You are clinically obese.")