#<<< Exercise_01 >>> (number comparator)
#Objective: Compare two numbers and state wich is the greater or whether they are equal.

try:
#Concepts: Input handling
    raw_first = (input("Please, enter the first number: ")).strip().lower()
    raw_second = (input("Please, enter the second number: ")).strip().lower()

#Data sanitization - a step that will clear the number, as there is no type conversion.
    clean_first = raw_first.replace("€", "").replace("$", "").replace(" ", "")
    clean_second = raw_second.replace("€", "").replace("$", "").replace(" ", "")

#Conditional - sets the number so that it can be converted in the next step.
    if "." in clean_first and "," in clean_first: 
        clean_first = clean_first.replace(".", "")
    if "." in clean_second and "," in clean_second:
        clean_second = clean_second.replace(".", "")

    clean_first = clean_first.replace(",", ".")
    clean_second = clean_second.replace(",", ".")

#Conversion - the final number, following the previous steps,
#is converted to a float type to accommodate any number.
    first_number = float(clean_first)
    second_number = float(clean_second)

#Conditional - compare both values and display the highest one
    if first_number == second_number:
        print(f"{first_number} is equal to {second_number}")
    elif first_number > second_number:
        display_number = int(first_number) if first_number.is_integer() else first_number
        print(f"Highest number: {display_number}")
    else:
        display_number = int(second_number) if second_number.is_integer() else second_number
        print(f"Highest number: {display_number}") 

#Except(ERROR) - generates an error if the data entered is invalid for conversion 
except ValueError:
    print("Invalid! Please, enter numbers only")