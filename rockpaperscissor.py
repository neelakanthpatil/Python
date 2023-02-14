rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
user_option = int(input("What do you want to Select. Type 0 for Rock, 1 for Paper or 2 for Scissors "))
print(user_option)

#if(user_option != 0 and user_option !=1 and user_option != 2):
#    print(f"You have to enter either 0 or 1 or 2 only, You have entered {user_option}")
#    print("Exiting the Program, Run the program again")
#    exit(1)
rock_paper_scissors = [rock,paper,scissors]
computer_option = random.randint(0,2)
print(computer_option)
if(user_option != 0 and user_option !=1 and user_option != 2):
    print(f"You have to enter either 0 or 1 or 2 only, You have entered {user_option}")
else:
    print(f"Nishita Chose {rock_paper_scissors[user_option]}")
    print(f"Papa Chose {rock_paper_scissors[computer_option]}")
    if(user_option == computer_option) :
        print("Both of you have selected the same item, so its a tie...!!! Play Again ")
    elif(user_option == 0 and computer_option == 1):
        print("Papa Wins")
    #    print(f"Papa Selected paper {paper}")
    #    print(f"Nishita Selected rock {rock}")
    elif(user_option == 0 and computer_option == 2):
        print("Nishita Wins")
    #    print(f"Papa Selected scissors {scissors}")
    #    print(f"Nishita Selected rock {rock}")
    elif(user_option == 1 and computer_option == 0):
        print("Nishita Wins")
    #    print(f"Papa Selected rock {rock}")
    #    print(f"Nishita Selected paper {paper}")
    elif(user_option == 1 and computer_option == 2):
        print("Papa Wins")
    #    print(f"Papa Selected scissors {scissors}")
    #    print(f"Nishita Selected paper {paper}")
    elif(user_option == 2 and computer_option == 0):
        print("Papa Wins")
    #    print(f"Papa Selected rock {rock}")
    #    print(f"Nishita Selected scissor {scissors}")
    elif(user_option == 2 and computer_option == 1):
        print("Nishita Wins")
    #    print(f"Papa Selected paper {paper}")
    #    print(f"Nishita Selected scissors {scissors}")
