""" 
Exercise 06 

Goal:
Determine whether three measurements can form
a triangle and identify its type.

Concepts Practiced:
- Input handling
- Input validation
- Type conversion
- Conditional statements
- Logical operators
- Loops
- Exception handling

Tests:
✓ Equilateral triangle (5, 5, 5)
✓ Isosceles triangle (5, 5, 8)
✓ Scalene triangle (3, 4, 5)
✓ Invalid triangle (1, 2, 5)
✓ Decimal measurements (3.5, 4.5, 5.5)
✓ Invalid input ("abc")
"""

while True: 
    try:
        first_measurement = float(input("Please, enter the first measurement: "))
        break

    except ValueError:
        print("Please, enter numbers only.\n")
        continue

while True:
    try:
        second_measurement = float(input("Please, enter the second measurement: "))
        break

    except ValueError:
        print("Please, enter numbers only.\n")
        continue

while True:
    try:
        third_measurement = float(input("Please, enter the third measurement: "))
        break

    except ValueError:
        print("Please, enter numbers only.\n")
        continue

if first_measurement < second_measurement + third_measurement \
    and second_measurement < first_measurement + third_measurement \
    and third_measurement < first_measurement + second_measurement:
    triangle = True
else:
    triangle = False
    print("\nThe measurements cannot form a triangle.\n")

if triangle == True:
    if first_measurement == second_measurement == third_measurement:
        print("\nThe measurements can form an Equilateral triangle!\n")
    elif first_measurement == second_measurement or \
        first_measurement == third_measurement or \
        second_measurement == third_measurement:
        print("\nThe measurements can form an Isoceles triangle!\n")
    else:
        print("\nThe measurements can form a Scalene triangle!\n")