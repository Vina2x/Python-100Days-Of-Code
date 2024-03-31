import random
print("Welcome to the Russian Roulette!!!")
name_string= input("Give me Everybody's name, seperated by an inverted comma.\n")
names= name_string.split(", ")
random_name= random.choice(names)

print(f"{random_name} is going to buy the Meal today :)")