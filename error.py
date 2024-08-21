try:    
    a = int(input("Enter a Number :"))
except Exception as error:
    print("User Error:" + str(error))