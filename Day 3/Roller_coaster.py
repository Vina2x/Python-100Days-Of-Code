print("Welcome to the Rollercoaster!!!")
height= int(input("Enter your height in cm:\n"))
if height>=120:
    print("You can ride the Rollercoaster.")
    age= int(input("Enter your age:\n"))
    if age<12:
        print("PLease pay $5.")
    elif age<=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you can't ride the Rollercoaster.")
    