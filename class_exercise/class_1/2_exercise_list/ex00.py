
name = input("Please, enter your name: ")
age = int(input("Please, enter your age: "))

if age < 18:
    print(f"{name} ,you are minor.")
elif age <= 65:
    print(f"{name} ,you are an adult.")
else:
    print(f"{name} ,you are retired.") 