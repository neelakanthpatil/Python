#Python Program to check if its Head or Tail incase if you dont have the toss coin
#Lets Rock
import random

head_tail = random.randint(0,1)
if head_tail == 0:
    print("Hey, its Tail...!!!")
else:
    print("Hey, its Head...!!!")