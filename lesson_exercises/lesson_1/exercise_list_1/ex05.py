"""
Exercise 05

Goal:
Calculate a salary adjustment based on predefined 
salary ranges and display  the updated salary.

Concepts Practiced:
- Input handling 
- Type conversion
- Arithmetic operations
- Conditional statements
- Variable assignment
- Exception handling

Tests:
✓ Salary up to 2000 (1500)
✓ Salary between 2000.01 and 5000 (3500)
✓ Salary above 5000 (6000)
✓ Decimal salary (2500.50)
✓ Zero salary (0)
✓ Invalid input ("abc")
"""

while True:
    try:
        salary = float(input("Please, "
        "enter your salary: "))
        break 

    except ValueError:
        print("Please, enter numbers only.")
        continue 

if salary <= 2000:
    percentage = 15
    new_salary = salary + (salary * percentage / 100)
elif salary > 2000.01 and salary <= 5000:
    percentage = 10
    new_salary = salary + (salary * percentage / 100)
else:
    percentage = 5
    new_salary = salary + (salary * percentage / 100)

print(f"\nYou have received a {percentage}% salary increase."
      f"\nYour new salary is: {new_salary:.2f}€\n")