print("Welcome to Python Pizza!!!")
size= input("What size of Pizza do you want? S, M or L\n")
add_pepperoni= input("Do you want to add pepperoni to it? Y or N\n")
extra_cheese= input("Do you want to add Extra cheese? Y or N\n")


bill=0


if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25

else:
    print("Enter a valid input.")

#ask weather they want to add pepperoni or not

if add_pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

#ask weather they want to add extra cheese or not

if extra_cheese=="Y":
    bill+=1


print(f"Your final bill is ${bill}.")