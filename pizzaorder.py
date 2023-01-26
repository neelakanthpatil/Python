#Python Program to caluclate total pizza bill based on your input
#Let's Rock

print("Welcome to Python Pizza Deliveries...!!!")
size = input("Whats the Pizza Size you want to prefer ? S or M or L ")
add_pepperoni = input("Do you want Pepperoni ? Y or N ")
extra_cheese = input("Do you want extra Cheese ? Y or N ")
bill = 0

if size == 'S':
   bill = 15
   if add_pepperoni == 'Y':
       bill += 2
#   if extra_cheese == 'Y':
#       bill += 1
elif size == 'M':
    bill = 20
    if add_pepperoni == 'Y':
        bill += 3
#    if extra_cheese == 'Y':
#        bill += 1
else:
    bill = 25
    if add_pepperoni == 'Y':
        bill += 3
#    if extra_cheese == 'Y':
#        bill += 1

if extra_cheese == 'Y':
    bill += 1

print(f"You final bill is ${bill}.")