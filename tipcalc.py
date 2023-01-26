#Python Program to Calculate the tip based on total amount, Tip and Number of People.
#Let's Start

print("Welcome to the tip calculator ...!!!\n")
amt = input("What was the total bill? $")
amt_float = float(amt)
tip = input("What percentage tip would you like to give? 10, 12 or 15 ")
tip_float = float(tip)
people = input("How many people to split the bill? ")
people_int = int(people)
each_per_contri = round(((amt_float * (1 + tip_float / 100)) / people_int), 2)
bill_per_person = "{:.2f}".format(each_per_contri)
print(f"Each person should pay: ${bill_per_person}")