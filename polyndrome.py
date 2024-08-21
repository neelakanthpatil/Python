#This program is for checking if passed variable is polyndrome or not
#This program will accept only variable
#Developer - Neelakanth Patil 

import sys

def main():
    print("The script name is", sys.argv[0])
    if len(sys.argv) == 2:
      print("Only one parameter is passed and we are good to check for polyndrome")
      print("The argument for checking polyndrome is", sys.argv[1])
      a = len(sys.argv[1])
      s = sys.argv[1]
      print("The length of passed string is",a)
      x = sys.argv[1]
      w = ''
      for i in x:
        w = i + w
#      print(x)
#      print(w)
      if x == w:
        print("The passed argument",sys.argv[1]," is polyndrome.")
      else:
        print("The passed argument ",sys.argv[1]," is not polyndrome.") 
    else:
      print("No arguments passed or more than one argument passed which is not as expected")

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()