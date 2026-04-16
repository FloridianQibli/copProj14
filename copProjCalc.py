# calculator assigment!

import math
import os
from _pyrepl.commands import clear_screen
from pydoc import text

print("\n\nWelcome to the Python calculator!!!")
validOp = ["+", "-", "/", "*", "**", "%"]

while True:
    operator = input("\nEnter your operator (+, -, /, *, **(exponent), %(remainder of / of two numbers)): ")
    if operator in validOp:
        break
    else:
        print("Invalid operator. Try again.")


def find_val_num(num_prompt):
    while True:
        userinput = input(num_prompt)
        try:
            return float(userinput)
        except ValueError:
            print("Invalid input. Try again.")




firstNum = find_val_num("Enter the first number: ")

while True:
    secondNum = find_val_num("Enter the second number: ")

    if (operator == "/" or operator == "%") and secondNum == 0:
        result = "Error"
        continue
    else:
        break

if operator == '+':
    result = firstNum + secondNum
elif operator == '-':
    result = firstNum - secondNum
elif operator == '*':
    result = firstNum * secondNum
elif operator == '/':
    result = firstNum / secondNum
elif operator == '**':
    result = firstNum ** secondNum
elif operator == '%':
    result = firstNum % secondNum

print(f"Result: {firstNum} {operator} {secondNum} = {result}")
