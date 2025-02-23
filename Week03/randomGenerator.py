# randomGenerator.py - Week3
# This program prints out a random number between 1 & 10
# Author: David Scally

import random

#number = random.randint(1,10)
#print('here is a random number {}'. format (number))

# User inputs the range
x = int(input('Enter first number in range: '))
y = int(input('Enter second number in range: '))
number = random.randint(x,y)
print('here is a random number {}'. format (number))
