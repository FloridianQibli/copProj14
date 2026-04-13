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

    if (operator == "/" or operator) == "%" and secondNum == 0:
        print("You cannot use this operator with zero being you second number. Try again.")
    else:
        print("test complete")
        break


# at the end of your calculation logic
choice = input("\nType 'clear' to reset or press Enter to continue: ").lower()
if choice == "clear":
    clear_screen()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
while True: # Main app loop
# 1. get first number
# 2. get operator
# 3. get second number
# 4. show result
reset = input("Type 'c' to clear screen and restart, or 'q' to quit: ")
if reset.lower() == "c":
    clear_screen()
# continue # restarts the loop from the top