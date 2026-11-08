"""
Chalenge

Goal:
Simulate a secure access control system by validating
user identity, role, access credentials, 
and security rules.

Concepts Practiced:
- Input handling
- Input validation
- String manipulation
- Sets
- Tuples
- Dictionaries
- Lists
- Conditional statements
- Nested loops
- Authentication logic
- Access control
- Custom exceptions
- Exception handling

Tests:
✓ Active manager with access card ("ana-gerente" → Access granted)
✓ Active technician with access card ("bruno_tech" → Access granted)
✓ User not found ("mateus" → User not found)
✓ Blocked user ("dr_evil" → Restricted user alert)
✓ Trainee access attempt ("trainee" position → Access denied)
✓ Valid master password (Card = No → Access granted)
✓ Invalid master password (3 failed attempts → Access denied)
✓ Invalid position ("developer" → Invalid position)
✓ Invalid card option ("Maybe" → Error message)
"""

class AuthenticationError (Exception):
    pass

#System database
bloked_users = {"hakerman", "dr_evil","py.robot"}
active_staff = ("ana-gerente", "bruno_tech", "carla_diretora")
biometric_keys = {"setor_a": "digital_ok", "setor_b": "iris_ok"}
position_list = ["manager", "technician", "trainee"]
card_option = {"Yes": True, "No": False}
master_password = ("M@sTerP@ssword")

while True:
    try:
#data entry
        user = str(input("Please, enter your name: ")).lower().strip()
        if user not in active_staff:
            raise AuthenticationError("User not found\n")
        
    except AuthenticationError as e:
            print(e)
            continue

    try:
        if user in bloked_users:
            raise AuthenticationError("\n🚨 ALERT: User on the restricted list! 🚨\n")

    except AuthenticationError as e:
        print(e)
        exit()

    while True:
        try:
            position = str(input("Please, enter your position: ")).lower().strip()
            if position not in position_list:
                raise AuthenticationError("Invalid position")
            elif position == position_list[2]:
                raise AuthenticationError("You do not have permission for this access. Access denied.")
            
        except AuthenticationError as e:
            print(e)
            exit()

        while True:
            try:
                card = str(input(f"Do you have a card ?\n"  f"\n{', '.join(card_option.keys())}\n  \nOption: ")).capitalize()
                card = card_option[card]

                if card:
                    for biometric in biometric_keys.values():
                        for i in range(3):
                            print(".\n")
                        print(biometric, "\n")

                elif not card:
                    password_attempts = 0
                    max_attempts = 3
                    while password_attempts < max_attempts:
                        password = str(input("Please, enter the master password: "))
                        if password == master_password:
                            break
                        else:
                            password_attempts += 1  
                            print("\nIncorret password!\n")  
                            if password_attempts >= max_attempts:
                                raise AuthenticationError("Access denied. Please try later.\n")
                            continue

            except AuthenticationError as e:
                print(e)
                exit()
        
            print(f"Access granted!\nWelcome {user}\n")
            break
        break
    break