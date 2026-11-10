"""
Exercise 01

Goal:
 

Concepts Practiced:
- Input handling
- Input validation
- 
- 
- 
-  
-  

Tests:
✓ 
✓  
✓ 
✓ 
✓ 
✓ 

"""

"""Peça ao usuário um número de início e um de
fim. O programa deve percorrer esse intervalo e imprimir apenas os números pares.
Se o número for múltiplo de 5, o programa deve exibir uma mensagem
personalizada ao lado do número."""

while True:
    try:
        raw_starting_number = input("Please, enter the first number "
                                "in the range to be traversed: ").strip()
                
        if not raw_starting_number:
            raise ValueError("You've forgotten to enter the number. "
                             "Try again!")
        elif "," in raw_starting_number and "." in raw_starting_number:
            if raw_starting_number.find(",") < raw_starting_number.find("."):
                raise ValueError("Invalid format.")
            integer_part = raw_starting_number.split(",")[0]
            groups = integer_part.split(".")
            for group in groups[1:]:
                if len(group) != 3:
                    raise ValueError("Invalid format")
                
            clean_first_number = raw_starting_number.replace(".", "")
            clean_first_number = clean_first_number.replace(",", ".")
            starting_number = float(clean_first_number)

        else:
            starting_number = float(
            raw_starting_number.replace(",", ".")
        )

        break

    except ValueError:
        print("Please, enter a valid number.")

while True:
    try:
        raw_final_number = input("Please, enter the final number "
                                        "in the range to be traversed: ").strip()
                        
        if not raw_final_number:
            raise ValueError("You've forgotten to enter the number. "
                                "Try again!")
        elif "," in raw_final_number and "." in raw_final_number:
            if raw_final_number.find(",") < raw_final_number.find("."):
                raise ValueError("Invalid format.")
            integer_part = raw_final_number.split(",")[0]
            groups = integer_part.split(".")
            for group in groups[1:]:
                if len(group) != 3:
                    raise ValueError("Invalid format.")
            clean_final_number = raw_final_number.replace(".", "")
            clean_final_number = clean_final_number.replace(",", ".")
            final_number = float(clean_final_number)

        elif "." in raw_final_number and "," not in raw_final_number:
            groups = raw_final_number.split(".")
            for group in groups[1:]:
                if len(group) != 3:
                    raise ValueError("Invalid format.")
            clean_final_number = raw_final_number.replace(".", "")
            final_number = float(clean_final_number)

        else:
            final_number= float(
            raw_final_number.replace(",", ".")
        )

        break
        
    except ValueError:
        print("Please, enter a valid number.")

pairs_list =[]

if starting_number < final_number:
    for number in range(int(starting_number), int(final_number)):
        if number % 2 == 0:
            pairs_list.append(number)

elif starting_number > final_number:
    for number in range(int(starting_number), int(final_number), -1):
            if number % 2 == 0:
                pairs_list.append(number)


print(">>> Even numbers <<<")
for even in pairs_list:
    if even % 5 == 0:
        print(f"{even} - multiple of 5")
    else:
        print(f"{even}")