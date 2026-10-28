
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