import random

word_list= ["camel", "ardvark", "baboon"]
chosen_word= random.choice(word_list)
word_length= len(chosen_word)

print(f"The chosen word is {chosen_word}")


# Create Blanks
display=[]
for _ in range(word_length):
        display+="_"

end_of_game=False

while not end_of_game:
    guess= input("Guess a letter!\n").lower()

    # check guessed letter
    for position in range(word_length):
            letter=chosen_word[position]
            if letter==guess:
                display[position]=letter
    print(display)

    # check if there are any blanks left
    if "_" not in display:
        end_of_game=True
        print("You Win")