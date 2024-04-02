import random

word_list= ["camel", "ardvark", "Baboon"]

chosen_word= random.choice(word_list)

guess= input("Enter a letter you want to check!\n").lower()

for letter in chosen_word:
    if letter==guess:
        print("Right")
    else:
        print("Wrong")