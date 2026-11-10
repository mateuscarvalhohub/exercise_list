"""
Exercise 01

Goal:
Authenticate a user by validating a username and password
against predefined administrator credentials.

Concepts Practiced:
- Input handling
- Tuples
- Conditional statements
- Loops
- String comparison
- Authentication logic

Tests:
✓ Valid credentials ("admin", "12345" → Access granted)
✓ Invalid username ("user", "12345" → Access denied)
✓ Invalid password ("admin", "00000" → Access denied)
✓ Invalid username and password ("user", "00000" → Access denied)
✓ Empty username ("", "12345" → Access denied)
✓ Empty password ("admin", "" → Access denied)
"""

admin_acces = ("admin", "12345")

while True:
    user = str(input("Please, enter your user: "))
    pass_ = str(input("Please, enter yout password"))

    if user == admin_acces[0] and pass_ == admin_acces[1]:
        print("Acess granted")
        break
    else:
        print("usear and password incorrects")
        continue