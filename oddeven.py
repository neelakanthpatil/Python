#Python to check if entered number is odd or even
#Let's Go

print("Program to check odd even number...!!! ")
number = int(input("Enter the number for checking if its odd or even "))
odd_even = number % 2

if odd_even == 1:
    print(f"The entered number is {number} and it's odd")
else:
    print(f"The Entered number is {number} and it's even")