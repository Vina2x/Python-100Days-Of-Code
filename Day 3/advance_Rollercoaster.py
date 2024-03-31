print("Welcome to the Rollercoaster!!!")
height= int(input("Enter your height in cm:\n"))
bill=0
if height>=120:
    print("You can ride the Rollercoaster.")
    age= int(input("Enter your age:\n"))
    if age<12:
        bill=5
        print("Child tickets are $5.")
    elif age<=18:
        bill=7
        print("Youth tickets are $7.")
    elif age>=45 and age<=50:
        print("The ticket is on us")
    else:
        bill=12
        print("Adults tickets are $12.")
    want_photos= input("Do you want a photo taken? Y or N.\n")
    if want_photos=="Y":
        bill+=3
    print(f"Your final bill is ${bill}.")

else:
    print("Sorry you can't ride the Rollercoaster.")