def calculate_discount(total_amount):
    if total_amount >= 100000:
        discount = 0.20 * total_amount
    elif 50000 <= total_amount < 99999:
        discount = 0.10 * total_amount
    elif 10000 <= total_amount < 49999:
        discount = 0.05 * total_amount
    else: 
        discount = 0
    
    amount_payable = total_amount - discount
    return amount_payable, discount


total_amount = float(input("Enter total amount of goods purchased: "))
amount_payable, discount = calculate_discount(total_amount)
print(f"Discount: {discount}")
print(f"Amount payable: {amount_payable}")  