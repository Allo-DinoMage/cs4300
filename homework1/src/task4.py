def calculate_discount(price, discount):
    # Check if they're numeric types
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number!")
    
    if not isinstance(discount, (int, float)):
        raise TypeError("Discount must be a number!")
    
    #apply the math
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    
    return final_price


if __name__ == "__main__":
    # Demo the function working
    print(f"$100 with 10% discount: ${calculate_discount(100, 10)}")
    print(f"$50.50 with 20% discount: ${calculate_discount(50.50, 20)}")
    print(f"$75 with 15.5% discount: ${calculate_discount(75, 15.5)}")