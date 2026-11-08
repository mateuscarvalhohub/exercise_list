"""
Exercise 03 

Goal:
Calculate Body Mass Index (BMI) based 
on the user's height and weight, then 
classify the result.

Concepts Practiced:
- Input handling
- Input validation
- Type conversion
- Arithmetic operations
- Conditional statements
- Loops
- Exception handling

Tests:
✓ Healthy weight (70 kg, 1.75 m)
✓ Underweight (50 kg, 1.75 m)
✓ Overweight (90 kg, 1.75 m)
✓ Invalid height (0, -1, 4)
✓ Decimal input (1.75, 70.5)
✓ Invalid input ("abc")
"""

while True:
    try:

        height = float(input("Please, "
        "enter your height in meters (e.g., 1.70): "))

        if height <= 0 or height >= 4:
            print("\nInvalid height.\n")
            continue

    except ValueError:
            print("Please, enter only numbers.\n")
            continue
    break

while True:
    try:

        weight = float(input("Please, "
        "enter your weight (kg): "))

        imc = weight / (height ** 2)
        imc = round(imc, 2)
        print(f"\nIMC = {imc}")

        if imc < 18.5 :
            print("\nUnderweigth!\n")
        elif imc >= 18.5 or imc <= 24.9:
            print("\nHealthy weight!\n")
        elif imc >= 25:
            print("\nOverweight!\n")
            continue
        break

    except ValueError:
        print("Please, enter only numbers.\n")