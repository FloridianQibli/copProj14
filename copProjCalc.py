# calculator assigment!

import math
from fractions import Fraction
import sys

print("\n" + "~" * 35)
print("Welcome to the Python calculator!!!")
print("~" * 35)

# calc_mode = input("Type 'f' for fraction mode or 'n' for normal mode 's' for square root mode or 'a' for absolute value mode: ")
history = []
twoNumOps = ["+", "-", "/", "*", "**", "%"]
oneNumOps = ["sin", "cos", "tan"]
validOp = twoNumOps + oneNumOps


def find_val_num(num_prompt):
    while True:
        userinput = input(num_prompt).strip().lower()
        if userinput == "pi":
            return math.pi
        try:
            return float(userinput)
        except ValueError:
            print("Invalid input. Try again.")


while True:  # outer loop (whole program)

    print("Type \"f\" for fraction mode")
    print("Type \"n\" for normal mode")
    print("Type \"s\" for square root mode")
    print("Type \"a\" to for absolute value mode")
    print("Type \"h\" for calculation history")
    print("Type \"q\" to quit")

    calc_mode = input("->) ").strip().lower()
    if calc_mode == "q":
        print("Goodbye!")
        break

    elif calc_mode == "n":  # CALC MODE!
        print("\n ~~ Normal mode ~~")
        firstNum = find_val_num("Enter the first number (or \"pi\") \nEnter degree if trig equation is intended: ")

        while True:  # inner loop (math loop)
            skipOp = False

            while True:
                print("\nAvailable operators:")
                print("Basic: +, -, *, /, **(exponent), %(remainder)")
                print("Trig: sin, cos, tan (Your first number entered is your input in degrees)")
                operator = input("\nEnter your operator: ").lower().strip()
                if operator in validOp:
                    break
                print("Invalid operator. Try again.")

            if operator in twoNumOps:
                while True:
                    secondNum = find_val_num("Enter the second number: ")
                    if (operator == "/" or operator == "%") and secondNum == 0:
                        result = "Error"
                        skipOp = True
                        break
                    else:
                        break

            if not skipOp:  # if operators are not being skipped
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

                history.append(equation)  # saving whatever equation was saved into history
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
                sys.exit() #exits program

    elif calc_mode == "h": #HISTORY MODE
        print("\n ~~ Calculation History ~~")
        if len(history) == 0:
            print("No history yet. Go do some math and come back!.")
        else:
            for item in history:
                print(item)
        print("---------------------------")

    # This is a whole another fraction loop
    elif calc_mode == "f": #FRACTION MODE
        print("\n ~~ Fraction mode ~~")
        # This is just to clarify as like an example to make sure no wrong inputs are used.
        print("Enter fractions like this: 1/2")
        while True:
            try:
                # This line checks what you type in was actually a fraction
                f_num1 = Fraction(input("Enter first fraction: "))
                # This line makes clear what operators can be used for this equation
                f_op = input("Enter operator (+, -, *, /): ")
                f_num2 = Fraction(input("Enter second fraction: "))
                if f_op == "+":
                    f_result = f_num1 + f_num2
                elif f_op == "-":
                    f_result = f_num1 - f_num2
                elif f_op == "*":
                    f_result = f_num1 * f_num2
                elif f_op == "/":
                    f_result = f_num1 / f_num2
                else:
                    # If any other input is used it will ask for it again
                    print("Invalid input. Try again.")
                    continue
                    # Finally it will clarify with the user at the end to make sure that was the equation they put

                equation = f"Result: {f_num1} {f_op} {f_num2} = {f_result}"
                print(equation)
                history.append(equation)
            except ValueError:
                # Once again marking it as wrong if anything else is entered
                print("Invalid input. Try again.")
                # Will always ask to stay in the same mode
            cont = input("\n Stay in fraction mode? (y/n): ").lower()
            if cont != "y":
                break

    # This is the square root mode
    elif calc_mode == "s": #SQUARE ROOT MODE
        print("\n ~~ Square Root mode ~~")
        while True:
            try:
                val = float(input("Enter the number you want the square root of: "))
                # You can take the square root of all numbers besides zero
                if val < 0:
                    # If the input is invalid it will ask again
                    print("Invalid input. Try again.")
                else:
                    sqrt_result = math.sqrt(val)
                    # This is the general place where it finds the answer
                    print(f"The square root of {val} is {sqrt_result}")
                    equation = f"root of {val} = {sqrt_result}"
                    history.append(f"Result: {equation}")

            except ValueError:
                # This line will play if anything besides a number is placed
                print("Invalid input. Try again.")
                # Always ask if you want to stay in the mode
            cont = input("\n Stay in square root mode? (y/n): ").lower()
            if cont != "y":
                break

    elif calc_mode == "a": #ABSOLUTE VAL MODE
        print("\n ~~ Absolute Value mode ~~")
        print("This will turn any negative numbers into a positive one")
        while True:
            try:
                val = float(input("\nEnter the number you want the absolute value of: "))
                abs_result = abs(val)
                print(f"The absolute value of {val} is {abs_result}")

                equation = f"Absolute value of {val} = {abs_result}"
                history.append(equation)

            except ValueError:
                print("Invalid input. Please enter a number.")

            # Fixed indentation!
            cont = input("\nStay in absolute value mode? (y/n): ").lower()
            if cont != "y":
                break

    else:
        print("Invalid option. Please choose from the menu.")
