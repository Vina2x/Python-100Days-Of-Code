import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list= ["camel", "ardvark", "baboon"]
chosen_word= random.choice(word_list)
word_length= len(chosen_word)
lives=6
end_of_game=False


print(f"The chosen word is {chosen_word}")


# Create Blanks
display=[]
for _ in range(word_length):
        display+="_"


while not end_of_game:
    guess= input("Guess a letter!\n").lower()

    # check guessed letter
    for position in range(word_length):
            letter=chosen_word[position]
            if letter==guess:
                display[position]=letter


    # taking lives // or subracting it out of 6
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You Loose")

    # check if there are any blanks left
    if "_" not in display:
        end_of_game=True
        print("You Win")


    print(stages[lives])        