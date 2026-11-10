"""
Exercise 00

Goal:
Classify a person based on their age as a minor,
adult, or retired.

Concepts Practiced:
- Input handling
- Type conversion
- Conditional statements
- String formatting
- Variables

Tests:
✓ Minor (John, 15 → Minor)
✓ Adult (John, 30 → Adult)
✓ Retired (John, 70 → Retired)
✓ Boundary age (18 → Adult)
✓ Boundary age (65 → Adult)
✓ Boundary age (66 → Retired)
"""

name = input("Please, enter your name: ")
age = int(input("Please, enter your age: "))

if age < 18:
    print(f"{name} ,you are minor.")
elif age <= 65:
    print(f"{name} ,you are an adult.")
else:
    print(f"{name} ,you are retired.") 