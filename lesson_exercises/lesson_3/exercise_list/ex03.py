"""
Exercise 03

Goal:
Register delivery cities, organize them by distance,
and generate an optimized delivery route.

Concepts Practiced:
- Input handling
- Input validation
- Data sanitization
- String manipulation
- Type conversion
- Dictionaries
- Lists
- Sorting
- Loops
- Conditional statements
- Exception handling

Tests:
✓ Valid city names and distances (Route generated successfully)
✓ City name with spaces ("New York" → Accepted)
✓ Decimal distance with comma ("12,5" → Converted to 12.5)
✓ Decimal distance with period ("12.5" → Converted correctly)
✓ Invalid city name ("City123" → Error message)
✓ Invalid distance ("abc" → Error message)
✓ Five cities registered successfully
✓ Cities displayed in ascending order of distance
"""

delivery_cities ={}

for i in range(1, 6):
    print(f"\n{i}ª city\n")
    while True:
        try:
                
            city = input("Please, enter the name of the delivery city: ")
                    
            if not city.replace(" ", "").isalpha():
                    raise ValueError
            break
                    
        except ValueError:
                print("Please, enter the correct name.")

    while True:
        try:
            distance_km = input("Please, enter the distance in km from the delivery city: ")
                        
            if "." in distance_km and "," in distance_km: 
                 distance_km = distance_km.replace(".", "")
                                
            distance_km = distance_km.replace(",", ".")

            distance = float(distance_km)
            break

        except ValueError:
            print("Please, enter numbers only.")

    delivery_cities[i] = (city, (distance))

# print(delivery_cities)

distance_list = []

for city, distance in delivery_cities.values():
    distance_list.append(distance)

distance_list = sorted(distance_list)

# print(distance_list)

print("\n>>> CITIES BY DISTANCE >>>\nYour route is ready:") 
for i, distance in enumerate(distance_list):
    if i == 0:
        print("START ↓")

    elif i == len(distance_list) - 1:
        print("↓ FINAL DESTINATION ↓")

    else:
        print("↓ next city ↓")

    for city, city_distance in delivery_cities.values():
        if city_distance == distance:
            number = i + 1
            print(f"{number} -", city, f"{distance:.2f} km")