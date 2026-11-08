"""
Exercise 02

Goal:
Control access to a VIP lounge by validating whether
the guest's name is included in the VIP guest list.

Concepts Practiced:
- Input handling
- String manipulation
- Sets
- Conditional statements
- Membership operators
- Loops

Tests:
✓ VIP guest ("Mateus" → Welcome to the VIP lounge!)
✓ VIP guest with lowercase input ("mateus" → Welcome to the VIP lounge!)
✓ VIP guest ("Eduarda" → Welcome to the VIP lounge!)
✓ Special guest ("Boss" → Welcome, Boss!)
✓ Non-VIP guest ("João" → Access by Invitation Only)
✓ Empty input ("" → Access by Invitation Only)
"""

vip_guests = {"Mateus", "Ricardo", "Eduarda", "Guilherme"}

while True:
    guest_name = str(input("Please enter your name: ")).capitalize()

    if guest_name in vip_guests:
        print("\nWelcome to the VIP lounge!\n")
        break
    elif guest_name == "Boss":
        print("\nWelcome, Boss!\n")
        break
    else:
        print("Access by Invitation Only")
        continue