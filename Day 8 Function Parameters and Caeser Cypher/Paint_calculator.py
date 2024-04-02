import math
# input height and width of the wall and change it to int
inp_height= int(input("Enter the height of the wall: "))
inp_width= int(input("Enter the width of the wall: "))
coverage=5;
# coverage is the amount of bucket or cans you'll need to paint the wall, e.g here a can of paint can cover 5 sqaure meters of wall!

# function to calculate the number of cans needed
def cans_needed(height, width, cover):
     print(f"You will need {math.ceil((height*width)/cover)} cans to paint the wall!")

# using keyword arguments to pass the desired data to the function parameters.
cans_needed(height=inp_height, width=inp_width, cover=coverage)