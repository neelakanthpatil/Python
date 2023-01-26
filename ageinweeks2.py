#Python program to calculate remaining age in Days, Weeks and Months
#User need to enter the current age

curr_age = input("Enter Your Current Age : ")
age = int(curr_age)
rem_age_years = 90 - age
rem_age_days = rem_age_years * 365
rem_age_weeks = rem_age_years * 52
rem_age_mts = rem_age_years * 12
print(f"You have {rem_age_days} days, {rem_age_weeks} weeks, and {rem_age_mts} months left")