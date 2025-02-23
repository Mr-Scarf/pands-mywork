#randomFruit2.py - Week3
# This program prints out a random fruit
# Author: David Scally

import random

fruits = ('Apple', 'Orange', 'Banana' ,'Pear')

#we want a random number between 0 and leng
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print('A Random Fruit: {}'. format (fruit))