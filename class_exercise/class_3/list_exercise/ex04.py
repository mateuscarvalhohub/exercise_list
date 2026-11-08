"""
Exercise 04

Goal:
Retrieve and display server error messages based on
an error code, while allowing unknown codes to be
registered with a default message.

Concepts Practiced:
- Input handling
- Input validation
- Data sanitization
- Type conversion
- Dictionaries
- Dictionary methods
- Conditional statements
- Loops
- Exception handling

Tests:
✓ Known code (404 → Not Found)
✓ Known code (500 → Internal Server Error)
✓ Known code (401 → Unauthorized)
✓ Unknown code (999 → Unknown error code)
✓ Code with separators ("4,0,4" → 404)
✓ Code with separators ("4.0.4" → 404)
✓ Invalid input ("abc" → Error message)
"""

error_codes = {
    404: "Not found",
    500: "Internal Server Error",
    401: "Unauthorized",
    503: "Service Unavailable",
    504: "Gateway Timeout"
}

while True:
    try:
        user_code = (input("Please, enter a code number: "))

        if "." in user_code or "," in user_code: 
            user_code = user_code.replace(".", "")                     
            user_code = user_code.replace(",", "")
        
        code = int(user_code)

        if code in error_codes:
            print(code, error_codes[code])
        else:
            default_unknow_code = error_codes.setdefault(code,"Unknown error code")

            print(default_unknow_code)

    except ValueError:
            print("Please, enter integer numbers only.")
    continue