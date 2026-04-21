# calculator assigment!

import math
import os
from _pyrepl.commands import clear_screen
from math import radians
from pydoc import text
from fractions import Fraction


print("\n\nWelcome to the Python calculator!!!")
calc_mode = input("Type 'f' for fraction mode or 'n' for normal mode or 's' for square root mode: ")
history = []
twoNumOps = ["+", "-", "/", "*", "**", "%"]
oneNumOps = ["sin", "cos", "tan"]

validOp = twoNumOps + oneNumOps


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
            print("\nAvailable operators:")
            print("Basic: +, -, *, /, **(exponent), %(remainder)")
            print("Trig: sin, cos, tan")
            operator = input("\nEnter your operator: ")
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

        if not skipOp: #if operators are not being skipped
            if operator in twoNumOps:
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

                equation = f"{firstNum} {operator} {secondNum} = {result}\n\n"

            elif operator in oneNumOps:
                radians = math.radians(firstNum)

                if operator == 'sin':
                    result = math.sin(radians)
                elif operator == 'cos':
                    result = math.cos(radians)
                elif operator == 'tan':
                    result = math.tan(radians)

                result = round(result, 5)
                equation = f"{operator}({firstNum})= {result}\n\n"

        history.append(equation) #saving whatever equation was saved into history
        print(f"Result: {equation}")

        while True:
            if skipOp:
                action = (input("\nType \"n\" if you would like to start over; or \"q\" to quit: ")).lower()

            else:
                action = (input(
                    f"\nType \"y\" to continue with {result}, \"n\" if you would like to start over, or \"q\" to quit: ")).lower()
            if action in ["y", "n", "q"]:
                break
            else:
                print("Invalid input. Try again.")

        if action == "y" and not skipOp:
            firstNum = result
        elif action == "n":
            break
        elif action == "q":
            print("Goodbye!")
            progRunning = False
            break

while True:
    choice = input("Enter the first number (or type 'pi'): ").strip().lower()
    if choice == 'pi':
        firstNum = math.pi
        break
    try:
        firstNum = float(Fraction(choice))
        break
    except ValueError:
        print("Invalid input. Try again.")
# This is the square root mode
if calc_mode == "s":
    print("\n this is square root mode")
    while True:
        try:
            val = float(input("Enter the number you want the square root of: "))
            if val < 0:
                print("Invalid input. Try again.")
            else:
                sqrt_result = math.sqrt(val)
                print(f"The square root of {val} is {sqrt_result}")
        except ValueError:
            print("Invalid input. Try again.")
            cont = input("\n Stay in square root mode? (y/n): ").lower()
            if cont != "y":
                break
# This is a whole another fraction loop
if calc_mode == "f":
    print("\n This is Fraction mode")
    print("Enter fractions please: Ex, 1/2.")
    while True:
        try:
            f_num1 = Fraction(input("Enter first fraction please: "))
            f_op = input("Enter operator please (+, -, *, /): ")
            f_num2 = Fraction(input("Enter second fraction please: "))
            if f_op == "+":
                f_result = f_num1 + f_num2
            elif f_op == "-":
                f_result = f_num1 - f_num2
            elif f_op == "*":
                f_result = f_num1 * f_num2
            elif f_op == "/":
                f_result = f_num1 / f_num2
            else:
                print("Invalid input. Try again.")
                continue
            print(f"Result: {f_num1} {f_op} {f_num2} {f_result}")
        except ValueError:
            print("Invalid input. Try again.")
        cont = input("\n Stay in fraction mode? (y/n): ").lower()
        if cont != "y":
            break
