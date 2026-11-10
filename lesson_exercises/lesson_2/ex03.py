"""
Exercise 03

Goal:
Check a student's grade in a selected subject and
display their academic status.

Concepts Practiced:
- Input handling
- String manipulation
- Dictionaries
- Conditional statements
- Loops
- Membership operators

Tests:
✓ Approved ("math" → Grade: 8.5 → Approved)
✓ Remedial ("english" → Grade: 5.0 → Remedial)
✓ Failed ("physics" → Grade: 4.3 → Failed)
✓ Subject not found ("biology" → Subject not found)
✓ Mixed case input ("Math" → Approved)
✓ Empty input ("" → Subject not found)
"""

report_card = {
    "math": 8.5,
    "english": 5.0,
    "physics": 4.3
}

while True:
    subject = str(input("Please, enter the subject: ")).lower()

    if subject in report_card:
        if report_card[subject] >= 7:
            print(f"You are approved in {subject}")
        elif report_card[subject] >= 5 and report_card[subject] <= 6.9:
            print(f"You are remedial in {subject}")
        elif report_card[subject] < 5:
            print(f"You have failed in {subject}")
        break

    else:
        print("Subject not found")
        continue