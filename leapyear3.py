#Python Program to check if entered year is Leap Year or Not.
#Let's Start

year = int(input("Please enter a year for checking if it's leap year or not "))
print(f"The User Entered year is {year}")

if year % 4 == 0:
    print("Checking further")
    if year % 100 != 0:
        print(f"The Entered Year {year} is a leap year..!!")
    elif year % 400 == 0:
        print(f"The Entered Year {year} is a leap year..!!")
    else:
        print(f"The Entered Year {year} is not a leap year..!!")
else:
    print(f"The Entered Year {year} is not a leap year..!!")