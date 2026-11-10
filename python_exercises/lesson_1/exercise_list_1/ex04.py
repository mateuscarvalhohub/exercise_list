"""
Exercise 04

Goal: 
Calculate a student's average grade 
and determine their academic status.

Concepts Practiced:
- Input handling
- Type conversion
- Arithmetic operations
- Conditional statements
- Loops
- Exceptions handling

Tests:
✓ Passed (8.0, 7.5, 9.0)
✓ Remedial (5.0, 6.0, 6.5)
✓ Failed (3.0, 4.5, 5.0)
✓ Decimal grades (7.5, 8.2, 6.8)
✓ Negative grades (-1.0, 7.0, 8.0)
✓ Invalid input ("abc")
"""

while True:
    try:

        first_grade = float(input("Please, enter your first grade: "))
        break

    except ValueError:
        print("Please, enter numbers only")
        continue

while True:
    try:
        second_grade = float(input("Please, enter your second grade: "))
        break
        
    except ValueError:
        print("Please, enter numbers only")
        continue

while True:
    try:
        third_grade = float(input("Please, enter your third grade: "))
        break
        
    except ValueError:
        print("Please, enter numbers only")
        continue

print(f"\nFirst Grade: {first_grade}"
      f"\nSecond Grade: {second_grade}"
      f"\nThird Grade: {third_grade}")

avarage = (first_grade + second_grade + third_grade) / 3

print(f"\nYour avarage is: {avarage:.2f}")

if avarage >= 7:
    print("\nPassed!\n")
elif avarage >= 5 or avarage <= 6.9:
    print("\nRemedial.\n")
else:
    print("\nFailed.\n")