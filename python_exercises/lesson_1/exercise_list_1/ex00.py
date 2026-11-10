"""
Exercise 00

Goal:
Check whether the number entered 
by the user is odd or even.

Concepts Practiced:
- Input handling 
- Data sanitization
- Type conversion
- Conditional statements
- Exception handling

Tests:
✓ Even integer (10)
✓ Odd integer (7)
✓ Decimal input with comma (10,0)
✓ Decimal input with period (5.5)
✓ Invalid input ("abc")
"""
while True:
    try:
        #Get and normalize user input
        raw_number = input("Please, enter an integer number: ").strip()

        #Data sanitization - standardize numeric format
        if "." in raw_number and "," in raw_number:
            clean_number = raw_number.replace(".", "")

            clean_number = clean_number.replace(",", ".")

        #Convert input to a numeric value
        number = float(raw_number)

        #check number parity
        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
        break

    except ValueError:
        #Handle invalid input
        print("Please, enter numbers only.")