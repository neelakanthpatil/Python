#Python program to implement if else elif logic
#Let's Go

print("Welcome to the Roller coaster ...!!!")
height = int(input("What is your height in CM? "))
bill = 0
if height >= 120:
    print("You are allowed to ride Roller coaster...!!!")
    age = int(input("Enter your age for checking the ticket price... "))
    if age < 12:
        bill = 5
        print("Please pay $5 and Enjoy Roller Coaster Ride")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Please pay $7 and Enjoy Roller Coaster Ride")
    elif age >= 45 and age <= 55:
        print("You are in Midlife Crisis and You will get free Ticket...Yaaaaayyyyyyyyy")
    else:
        bill = 12
        print("Please pay $12 and Enjoy Roller Coaster Ride")

    wants_photo = input("Do you want your photo be captured during the ride ? Y or N ")
    if wants_photo == "Y":
        bill += 1
    print(f"You Total for this ride is ${bill}.")

else:
    print("Sorry, You are not allowed to ride Roller coaster since your height is less than 120CM")

