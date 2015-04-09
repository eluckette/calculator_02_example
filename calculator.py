"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
exit_condition = False
while (exit_condition == False):
 
    input = raw_input("> ")
    tokens = input.split(" ")
    oper = tokens.pop(0)

    #tokens = [int(i) for i in tokens]
    for item in range(len(tokens)):
        tokens[item] = float(tokens[item])

    if oper == "+":
        print add(tokens[0], tokens[1])
    if oper == "-":
        print subtract(tokens[0], tokens[1])
    if oper == "*":
        print multiply(tokens[0], tokens[1])
    if oper == "/":
        print divide(tokens[0], tokens[1])
    if oper == "square":
        print square(tokens[0])
    if oper == "cube":
        print cube(tokens[0])
    if oper == "pow":
        print power(tokens[0], tokens[1])
    if oper == "mod":
        print mod(tokens[0], tokens[1])    
    if oper == "q":
        exit_condition = True
        break




