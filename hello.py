## This is my first python program
## As per software industry rituals i am also starting with "Hello World" program.

import sys

def main():
  if len(sys.argv)<2:
    fname = 'No Parameters'
  else:
    fname = sys.argv[1]
    
  if len(sys.argv)<2:
    lname = 'Passed'
  else:
    lname = sys.argv[2]
    
  print ("The script Name is", sys.argv[0])
  print ('Hello,', fname, lname)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
