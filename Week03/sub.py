# sub.py - Week3
# This program reads in 2 numbers and subtracts the first from the 2nd.
# Author: David Scally

#input reads in a string so we need to convert it inot an int
# so we can perform math operations

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
answer = x-y
print(' {} minus {} is {}'.format(x, y, answer))