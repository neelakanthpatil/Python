import random

score = 0
randomNumber = random.randint(1,10)


while True:
    UserNumber = int(input("Enter Your Number :"))
    if UserNumber == randomNumber:
        print("You guessed the number correctly, Congratulations")
        print("Your guessed Number is : "  + str(UserNumber))
        print("Random Number generated is : " + str(randomNumber))
        score += 10
        print("Your score is :"  + str(score))
        break
    else:
        print("You guessed it wrongly, Better luck next time")
        print("Your guessed Number is : "  + str(UserNumber))
        print("Random Number generated is : " + str(randomNumber))
        score -= 10
        print("Your score is :"  + str(score))
