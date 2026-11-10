"""
Exercise 02
 
Goal:
Classify support tickets based on customer category,
issue type, and waiting time to determine priority
and estimated response time.
 
Concepts Practiced:
- Input handling
- Input validation
- Type conversion
- Dictionaries
- Conditional statements
- Logical operators
- String formatting
- Loops
- Exception handling
 
Tests:
✓ Premium + Critical Error (Priority: Critical | Time Limit: 24 hours)
✓ Standard + Critical Error + 30 hours open (Priority: Critical | Time Limit: 24 hours)
✓ Premium + Question (Priority: High | Time Limit: 4 hours)
✓ Educational + Critical Error (Priority: High | Time Limit: 4 hours)
✓ Standard + Question (Priority: Medium | Time Limit: 8 hours)
✓ Educational + Question (Priority: Medium | Time Limit: 8 hours)
✓ Premium + Suggestion (Priority: Medium | Time Limit: 8 hours)
✓ Standard + Suggestion (Priority: Low | Time Limit: 24 hours)
✓ Invalid category (Error message)
✓ Invalid issue type (Error message)
✓ Invalid hours open (Error message)
"""

while True:
    try:
        client_id = int(input("\nEnter your ID Number: "))
        break

    except ValueError:
        print("\n(Please, enter a valid number)\n")

print("\n--- Categories ---\n")

categories = {
    1: "Premium",
    2: "Standard",
    3: "Educacional"
}

category_options = "\n".join(
    f"{key} - {value}"
    for key, value in categories.items()
)
# print(categories.keys())

while True:
    try:
        client_category = int(input(f"Indicate your category (enter the correspondent number):\n \n{category_options}\n \nCategory: "))

        if client_category not in categories:
            print("\ninvalid option.\n"
                "Erro: Inexistent category.\n"
                "(Please, enter 1, 2 or 3)")
            continue
        break

    except ValueError:
        print("Please, enter only numbers.")

issue_type = {
    1: "Critical Error",
    2: "Question",
    3: "Suggestion"
}

options = "\n".join(
    f"{key} - {value}"
    for key, value in issue_type.items()
)
while True:
    try:
        issue = int(input(f"\nChoose an error type:\n \n{options}\n \nOpition: "))

        if issue not in issue_type:
            print("\ninvalid option.\n"
            "Erro: Invalid issue type. (Please, enter 1, 2 or 3)")
            continue
        break

    except ValueError:
        print("Please, enter numbers only.")
        
while True:
    try:
        hours_open = float(input("\nNumber of hours the ticket has been awaiting: "))

        if hours_open <= 0:
            print("hours open cannot be negative.")
            continue
        break

    except ValueError:
        print("Please, enter numbers only.")

priority_and_time_limit = {
    "Low": "24 hours",
    "Medium": "8 hours",
    "High": "4 hours",
    "Critical": "24 hours" 
}

if client_category == 1  and issue == 1 \
or client_category == 2 and issue == 1 and hours_open > 24 \
or client_category == 2 and issue == 1 and hours_open > 24:
    priority_case = "Critical"

elif client_category == 1 and issue == 2 \
or client_category == 2 and issue == 1 and hours_open <= 24 \
or client_category == 3 and issue == 1:
    priority_case = "High"

elif client_category == 1 and issue == 3 \
or client_category == 2 and issue == 2 \
or client_category == 3 and issue == 2:
    priority_case = "Medium"

else:
    priority_case = "Low"

print("\nResult (Priority:", f"{priority_case}","|", "Time limit:", f"{priority_and_time_limit[priority_case]})")

print("\n--- Ticket Triage Report ---")
print(f"Client ID: {client_id}")
print(f"Category:", f"{categories[client_category]}")
print(f"Issue Type: {issue_type[issue]}")
print(f"Hours open :", f"{hours_open:}")

print("\n>>> Final Ticket Classification <<<")
print(f"Priority: {priority_case}")
print(f"Estimated Response Time: {priority_and_time_limit[priority_case]}")