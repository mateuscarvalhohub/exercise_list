"""
Exercise 06

Goal:
Update a smartphone price history, display the updated
price list, and identify the highest and lowest prices.

Concepts Practiced:
- Input handling
- Data sanitization
- String manipulation
- Type conversion
- Dictionaries
- Lists
- List methods
- Loops
- Enumeration
- Built-in functions (max, min)
- Exception handling

Tests:
✓ Valid price update (1800 → Highest: 1800, Lowest: 1200)
✓ Decimal price with comma (1.750,50 → Converted to 1750.50)
✓ Decimal price with period (1750.50 → Converted correctly)
✓ Price lower than all previous values (1100 → Highest: 1500, Lowest: 1100)
✓ Price higher than all previous values (2000 → Highest: 2000, Lowest: 1200)
✓ Invalid input ("abc" → Error message)
"""

smartphone = {
"Iphone": [1200, 1500, 1300, 1650]
}

while True:
    try:
        price_update = input("Please, insert the new price: ").strip()

        if "." in price_update and "," in price_update:
            price_update = price_update.replace(".", "")

        clean_price = price_update.replace(",", ".")
        price = float(clean_price)

        smartphone["Iphone"].pop()
        smartphone["Iphone"].append(price)

        print("\n>>> Price List <<<")
        for position, price in enumerate(smartphone["Iphone"],\
             start = 1):
             print(f"{position}º - {price}")

        biggest_price_rise = max(smartphone["Iphone"])
        smallest_price_rise = min(smartphone["Iphone"])
    except ValueError:
            print("Please, enter numbers only.")

    print(f"\nThe biggest rise is {biggest_price_rise}")
    print(f"The smallest rise is {smallest_price_rise}")
    break