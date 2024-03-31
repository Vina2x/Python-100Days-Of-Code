import random
Love_score= random.randint(1,100)

if Love_score<10 or Love_score>90:
    print(f"Your Love Score is {Love_score}, You go together like Coke and Mentos.")
elif Love_score>=40 and Love_score<=50:
    print(f"Your Love Score is {Love_score},You are alright together.")
else:
    print(f"Your Love Score is {Love_score}.")