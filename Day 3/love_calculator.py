print("WELCOME TO THE LOVE CALCULATOR!!!")
name1= input("What is your name?\n")
name2= input("What is their name?\n")
name1_lower= name1.lower()
name2_lower= name2.lower()
combined_names= name1_lower+name2_lower
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
sumTrue= t+r+u+e
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
sumLove= l+o+v+e
True_Love = str(sumTrue)+str(sumLove)
Love_score= int(True_Love)

if Love_score<10 or Love_score>90:
    print(f"Your Love Score is {Love_score}, You go together like Coke and Mentos.")
elif Love_score>=40 and Love_score<=50:
    print(f"Your Love Score is {Love_score},You are alright together.")
else:
    print(f"Your Score is {Love_score}.")