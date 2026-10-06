from prettytable import PrettyTable

def generate_terminal_bill(customer_name, items):
    # Initialize the table and set column headers
    table = PrettyTable()
    table.field_names = ["Item Name", "Quantity", "Unit Price ($)", "Total ($)"]
    
    # Align text columns to the left, numeric to the right
    table.align["Item Name"] = "l"
    table.align["Quantity"] = "r"
    table.align["Unit Price ($)"] = "r"
    table.align["Total ($)"] = "r"
    
    subtotal = 0
    
    # Populate data rows
    for item in items:
        name = item["name"]
        qty = item["qty"]
        price = item["price"]
        item_total = qty * price
        subtotal += item_total
        
        table.add_row([name, qty, f"{price:.2f}", f"{item_total:.2f}"])
    
    # Calculate taxes and final total
    tax = subtotal * 0.08  # 8% Tax
    grand_total = subtotal + tax
    
    # Add summary rows
    table.add_row(["-"*15, "-"*8, "-"*12, "-"*10])
    table.add_row(["Subtotal", "", "", f"{subtotal:.2f}"])
    table.add_row(["Tax (8%)", "", "", f"{tax:.2f}"])
    table.add_row(["Grand Total", "", "", f"{grand_total:.2f}"])
    
    # Print the receipt
    print("\n" + "="*40)
    print(f"CUSTOMER: {customer_name.upper()}")
    print("="*40)
    print(table)
    print("="*40 + "\n")

# Example Usage
order_items = [
    {"name": "Wireless Mouse", "qty": 2, "price": 25.00},
    {"name": "Mechanical Keyboard", "qty": 1, "price": 89.99},
    {"name": "HDMI Cable", "qty": 3, "price": 7.50}
]

generate_terminal_bill("Alice Smith", order_items)
