"""
Exercise 09 

Goal:
Simulate an ATM withdrawal system by 
distributing the requested amount using 
available banknotes.

Concepts Practiced:
- Input handling 
- Input validantion
- Type conversion
- Lists
- Dictionaries
- Loops
- Conditional statements
- Arithmetic operations
- Exception handling

Tests:
✓ €80 → 4 × €20
✓ €150 → 7 × €20, 1 × €10
✓ €320 → 1 × €50, 13 × €20, 1 × €10
✓ €100 → 10 × €10
✓ Invalid amount (0 → Error message)
✓ Invalid input ("abc" → Error message)
"""

while True:
    try:
        amount = (input("Please, enter the amount you would like to withdraw: €"))

        if amount <= 0:
                raise ValueError
        break
    
    except ValueError:
        print("Invalid amount! Please enter whole numbers only.")

notes = [50, 20, 10]
banknotes = {}

for note in notes:

    while amount > 300:
        banknotes[50] = banknotes.get(50, 0) + 1
        amount -= 50

    if amount < 300 and amount > 100:
        quantity = amount // notes[1]
        banknotes[notes[1]]= quantity
        remaining = amount % 20
        amount = remaining
        if amount <= 0:
            break

    while amount > 100:
        banknotes[20] = banknotes.get(20, 0) + 1
        amount -= 20

    if amount <= 100:
        quantity = amount // notes[2]
        banknotes[notes[2] ]= quantity
        remaining = amount % 10
        amount = remaining
        if amount <= 0:
            break
    else:
        quantity = amount // note
        banknotes[note] = quantity
        remaining = amount % note
        amount = remaining

if amount == 0:
    print("\nWithdrawal completed successfully.\n")

    for notes, quantity in banknotes.items():
        if quantity > 0:
            print(f"${notes} banknotes: {quantity}\n")

else:
    print("\nThe withdrawal cannot be completed using the available banknotes.")