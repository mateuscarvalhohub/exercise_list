
"""
Exercise 02 

Goal: 
Authenticate a user by validating 
the provide username and password 
against predefined credentials. 

Concepts Practiced:
- Input handling 
- Conditional statements
- Custom exceptions
- Exception handling 
- Authentication logic
- Loops

Tests:
✓ Valid credentials ("admin", "1234")
✓ Valid user with invalid password ("admin", "0000")
✓ Invalid user ("mateus", "1234")
✓ Empty username ("", "1234")
✓ Empty password ("admin", "")
"""

class AuthenticationError(Exception):
    pass

while True:
    try:

        user = input("Please enter yor user id: ")

        password = str(input("Please, enter your password: "))

        if user == "admin" and password == "1234":
            print("\nAcess granted: Welcome, administrator!\n")
            break
        elif user == "admin" and password != "1234":
            raise AuthenticationError("\nIncorret password!\n")
        else:
            raise AuthenticationError("\nUser not recognized. Access denied.\n")
          

    except AuthenticationError as e:
        print(e)