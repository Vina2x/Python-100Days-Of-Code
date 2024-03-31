print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print('''Welcome to the Treasure Island!!!
Your mission is to find the Treasure.
      ''')
choice1= input('''You're at a cross road, where do you want to go? Type "left" or "right"\n''').lower()

if choice1=="left":
    choice2= input('''You've come to a lake,There is an island in the middle of the lake. Type "wait" to wait for a Boat or type "swim" to swim across\n''').lower()
    if choice2=="wait":
        choice3= input('''You've reached the island unharmed, There is a house with 3 Doors.One red, One yellow and One blue. Which color do you want to choose?\n''').lower()
        if choice3=="red":
            print("It's a Room full of Fire. GAME OVER!!!")
        elif choice3=="yellow":
            print("Congrats You found the Treasure, YOU WIN!!!")
        elif choice3=="blue":
            print("You entered a Room full of Beasts, GAME OVER!!!")
        else:
            print("You chose a door that doesn't exist, GAME OVER!!!")
     
    else: 
        print("You got eaten by Sharks, GAME OVER!!!")
else:
    print("You fell into a hole, GAME OVER!")