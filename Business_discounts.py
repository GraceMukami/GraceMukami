def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price -(price * (discount_percent /100))
        return discounted_price
    else:
        return price
    
    # Prompting the user for input
    original_price = float(input("Enter the original pricr of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculating the funal price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Output the redult
    if final_price != original_price:
        print("final price after discount: {:.2f}".format(final_price))
    else:
        print("No discount applied.Original price: {:.2f}".format(fianl_price))
        
        