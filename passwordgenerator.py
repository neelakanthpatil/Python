#Python Program to generate a complex password
#Let's Python

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ''
new_password = ''
random_password = ''
for num in range(1, nr_letters+1):
    num_let = random.randint(0,len(letters)-1)
    password += letters[num_let]

for num in range(1, nr_numbers+1):
    num_num = random.randint(0,len(numbers)-1)
    password += numbers[num_num]

for num in range(1, nr_symbols+1):
    num_sym = random.randint(0,len(symbols)-1)
    password += symbols[num_sym]

for i in range(1, len(password)+1):
    temp_num = random.randint(0,len(password)-1)
    new_password += password[temp_num]
    print(random.shuffle(password))
    #random_password += random.shuffle(new_password)


print(password)
print(new_password)
print(random_password)