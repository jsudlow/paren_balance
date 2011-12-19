#!/usr/bin/python

#Jon Sudlow 2011 - Restudying of Data Structures
#this progrma uses a stack implementation to check a program for balanced parenthesis. It reads in a program and tells you if it is balanced.

from stack import Stack

#make a new stack
stack = Stack()

#get a lines string to add to
lines = ''

#use sexy with to auto open/close file and read in contents to our var
with open('./program_test.py', 'r') as f: 
    lines = f.read()

#iterate over the lines and perform stack pushing/popping logic. If the stack gets 'popped off' meaning the amount of elements in stack is 0 and a POP attempt occurs, then you know an imbalance has occured.
#the program breaks from the loop and prints out the line number and the data around the error to give the user a reference
for lineno,char in enumerate(lines):
    if char == '(':
        stack.push(char)
    if char == ')':
        char_returned = stack.pop()
        if char_returned == 'god-signal':
           print "Char Number in string: ", lineno,char 
           print 'PARENTHESIS UNBALENCED', 'near the following: ', lines
           break



