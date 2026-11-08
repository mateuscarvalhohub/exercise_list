"""
Exercise 00

Goal:
Register products, identify duplicate entries, and
display a list of unique products along with duplicates found.

Concepts Practiced:
- Input handling
- String manipulation
- Lists
- Sets
- Loops
- Conditional statements
- Data deduplication

Tests:
✓ New products ("milk", "bread", "eggs" → All products registered)
✓ Duplicate product ("milk", "bread", "milk" → Duplicate: milk)
✓ Multiple duplicates ("milk", "bread", "milk", "bread" → Duplicates: milk, bread)
✓ Exit command ("exit" → Registration finished)
✓ Mixed case input ("Milk", "milk" → Duplicate detected after normalization)
✓ Empty input ("" → Empty product registered)
"""

products_list = []

while True:
    try:
        products_to_register = str(input("Please, register the product (Enter one product at a time and press Enter./"
                                          "Once you have finished write exit): ")).lower()

        if products_to_register == "exit":
            break
        
        products_list.append(products_to_register)

        print(", ".join(p.strip() for p in products_list))

    except ValueError:
        print("Please, enter only the name of the product.")

    list_set = set()
    unique_products = []
    
for product in products_list:
    if product in unique_products:
        list_set.add(product)
    else:
        unique_products.append(product) 

    products_list = unique_products
    
print("\n --- List ---\n", " | ".join(p.strip() for p in products_list))
print("\n --- Duplicates ---\n", " - ".join(s.strip() for s in list_set), "\n")