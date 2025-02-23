# div.py - Week3
# This program reads in 2 numbers and divides the first one by the second and gives the integer result
# Author: David Scally

#input reads in a string so we need
# so we can perform math operations

x = int(input('Enter first number :'))
y = int(input('Enter the number you want to divide by :'))
answer = int(x//y) # // gives the int division
remainder =x%y

print('{} divided by {} is {} with reaminder {}' . format(x, y, answer, remainder))