# calculator assigment!

import math
import os
from _pyrepl.commands import clear_screen
from pydoc import text

print("\n\nWelcome to the Python calculator!!!")
validOp = ["+", "-", "/", "*", "**", "%"]


def find_val_num(num_prompt):
    while True:
        userinput = input(num_prompt)
        try:
            return float(userinput)
        except ValueError:
            print("Invalid input. Try again.")


progRunning = True

while progRunning:  # outer loop (whole program)

    firstNum = find_val_num("Enter the first number: ")

    while True:  # inner loop (math loop)
        skipOp = False

        while True:
            operator = input("\nEnter your operator (+, -, /, *, **(exponent), %(remainder of / of two numbers)): ")
            if operator in validOp:
                break
            else:
                print("Invalid operator. Try again.")

        while True:
            secondNum = find_val_num("Enter the second number: ")

            if (operator == "/" or operator == "%") and secondNum == 0:
                result = "Error"
                skipOp = True
                break
            else:
                break

        if not skipOp:
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

        print(f"Result: {firstNum} {operator} {secondNum} = {result}\n\n")

        while True:
            if skipOp:
                action = (input("\nType \"n\" if you would like to start over, or \"q\" to quit: ")).lower()

            else:
                action = (input(f"\nType \"y\" to continue with {result}, \"n\" if you would like to start over, or"
                                f" \"q\" to quit: ")).lower()
            if action in ["y", "n", "q"]:
                break
            else:
                print("Invalid input. Try again.")


        if action == "y" and not skipOp:
            firstNum = result
            break
        elif action == "n":
            break
        elif action == "q":
            print("Goodbye!")
            progRunning = False
            break
