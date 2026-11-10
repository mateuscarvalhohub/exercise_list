"""
Exercise 07 

Goal:
Perform basic arithmetic operations between two 
numbers based on the operator selected by the user.

Concepts Practiced:
- Input handling
- Input validation
- Type conversion
- Arithmetic operations
- Conditional statements
- Lists
- Loops
- Exception handling

Tests:
✓ Addition (10 + 5)
✓ Subtraction (10 - 5)
✓ Multiplication (10 * 5)
"""

while True:
    try:
        first_number = float(input(
            "Please, enter the first number: "
            ))
        break
    
    except ValueError:
        print("\nPlease, enter numbers only")

while True:
    try:
        second_number = float(input(
            "Please, enter the second number: "
        ))
        break

    except ValueError:
        print("\nPlease, enter numbers only")

math_operation = ["+", "-", "*", "/"]

while True:
    try:
        operation = (input(f"\nPlease, "
        f"choose the operator ( {' , '.join(math_operation)} ): ")).strip()

        if operation not in math_operation:
            raise ValueError

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number == 0:
                raise ZeroDivisionError
            result = first_number / second_number

        print(f"{first_number} {operation}"
              f"{second_number} = {result:.2f}\n")
        break

    except ValueError:
        print(f"(Please, enter a valid operator:\
               [ {'  '.join(math_operation)} ] )")
    except ZeroDivisionError:
        print("Cannot divide by zero.")