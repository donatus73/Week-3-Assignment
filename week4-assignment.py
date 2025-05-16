def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage.
    
    Returns:
    - float: The final price after applying the discount or the original price if discount < 20%.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount)

    # Display the result
    if discount >= 20:
        print(f"The final price after {discount}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: ${original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
