# testTypes.py - Week3
# This program returns the type of five different variables
# Author: David Scally

i = 5
fl = 5.5
isa = True
memo = 'That would be an ecumenical matter'
lots = []

#Comment: Reviewed sample code in lab3.1 , reviewed vs Chat Gpt and find the below version easier to read.
#Issue: It is not dynamic for string text if variable i changes.
#print (f'variable i is of type:{type(i)} and value: {i}') 
#print (f'variable fl is of type:{type(fl)} and value: {fl}')
#print (f'variable isa is of type:{type(isa)} and value: {isa}')
#print (f'variable memo is of type:{type(memo)} and value: {memo}')
#print (f'variable lots is of type:{type(lots)} and value: {lots}')

#Will add dynamic version per lab notes
print("Variable {} is of type: {} and value: {}".format(i, type(i), i))
print("Variable {} is of type: {} and value: {}".format(fl, type(fl), fl))
print("Variable {} is of type: {} and value: {}".format(isa, type(isa), isa))
print("Variable {} is of type: {} and value: {}".format(memo, type(memo), memo))
print("Variable {} is of type: {} and value: {}".format(lots, type(lots), lots))