#Python program to calculate the BMI based on height and weight entered by User
#This will display the category based on the BMI Value.

height = float(input("Enter user height in meter... "))
weight = float(input("Enter user weight in kilogram... "))

bmi = round(weight / (height ** 2),1)
print(f"BMI for the entered height {height}m and weight {weight}kg is {bmi} ")

if bmi < 18.5:
    print("You are in Underweight Category.")
elif bmi < 25:
    print("You are in Normal Weight Category.")
elif bmi < 30:
    print("You are in Over Weight Category.")
elif bmi < 35:
    print("You are in Obese Category")
else:
    print("You are in Clinically Obese Category.")