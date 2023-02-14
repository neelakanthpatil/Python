#Python program to find who is going to pay the bill
#Let's Start.
import random
names = input("Give me everybody's names, Separated by a comma(,) \n")
print(names)

names_list = names.split(", ")
length = len(names_list)

index = random.randint(0,length-1)

print(f"Today's bill will be paid by {names_list[index]}")