import random

word_list= ["camel", "ardvark", "Baboon"]

chosen_word= random.choice(word_list)

print(f"The chosen word is {chosen_word}")



display=[]
word_length= len(chosen_word)

for _ in range(word_length):
    display+="_"
print(display)
guess= input("Guess a letter!\n").lower()
for position in range(word_length):
    letter=chosen_word[position]
    if letter==guess:
        display[position]=letter
        print(display)