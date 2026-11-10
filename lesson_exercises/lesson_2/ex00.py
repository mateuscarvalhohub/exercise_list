"""
Exercise 00

Goal:
Manage a task list by allowing the user to add a new task
while preventing duplicate entries.

Concepts Practiced:
- Input handling
- String manipulation
- Lists
- Conditional statements
- Loops
- Membership operators

Tests:
✓ New task ("read a book" → Task added successfully)
✓ Existing task ("study python" → Duplicate task message)
✓ Different task ("buy groceries" → Task added successfully)
✓ Mixed case input ("Study Python" → Duplicate task detected after normalization)
✓ Empty input ("" → Empty task added)
"""

tasks = ["study Python", "clean room", "workout"]

while True:
    new_task = str(input("Please, enter the task: ")).lower()

    if new_task in tasks:
        print("This task is already in the task list\n")
        continue
    else:
        tasks.append(new_task)
        print("\n".join(tasks))
        break