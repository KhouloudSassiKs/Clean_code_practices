"""
This script calculates the total cost of an item purchase.

Update note:
The total price (unit_price * quantity) is now calculated outside the 
`calculate_total()` function and passed as an argument.
"""

def main():
    item_price = 12.50
    quantity = 4
    discount_rate = 0.10
    tax_rate = 0.08
    
    # Total price is now calculated here and passed into the function
    total_cost = calculate_total(item_price * quantity, discount_rate, tax_rate)
    print(f"Total Cost: {total_cost:.2f}")

    
def calculate_total(total_price, discount_rate, tax_rate):
    """
    Calculate the final price after applying discount and tax.
    """
    discount = total_price * discount_rate
    price_after_discount = total_price - discount
    tax_amount = price_after_discount * tax_rate
    final_price = price_after_discount + tax_amount
    return final_price


if __name__ == "__main__":
    main()
