#Python program for the treasue island.
#Let's Rock
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************''')
print("Welcome to the Treasure Island...!!!")
print("Your mission is to find the treasure")

move = input("Do you want move towards right or left ? Enter Right or Left ").lower()
if move == 'left':
    wait_swim = input("Do you want to Swim or Wait ? Enter Swim or Wait ").lower()
    if wait_swim == 'swim':
        print("Its a Trap Man, How will you swim in sea with lots of Crocodiles, You Are Dead, Game Over :-(")
    else:
        door = input("Which Color Door You Prefer to be opened ? Enter Red or Yellow or Blue ").lower()
        if door == 'red':
            print("You opened the burning house, You are Dead, Game Over :-(")
        elif door == 'blue':
            print("You are into Blue Whales House, You are Dead, Game Over :-(")
        elif door == 'yellow':
            print("You are into Gold House, You won all the treasure, Yaaayyy, You are a winner ...!!! ")
        else:
            print("Game Over...!!!")
else:
    print("You are fallen into Sea with lots of Crocodiles, You are Dead :-(, Game Over")


