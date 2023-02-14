#Python program to generate the Random number using Python's In Built function "Random()"
#Let's Start

import random

rand_int = random.randint(1,10)
print(rand_int)

rand_float = round(random.random(),2)
print(rand_float * 5)

love_score = random.randint(1,100)
print(f"Your Love Score is {love_score}.")