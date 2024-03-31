age= int(input("What is your current age:"))
remaining_age= 90-age
remaining_days= 365*remaining_age
remaining_weeks= 52*remaining_age
remaining_months= 12*remaining_age
message=(f"You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left.")
print(message)
