def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Return price after applying discount
        return price - discount_amount
    else:
        # Return original price if discount is less than 20%
        return price

# Get input from user
try:
    original_price = float(input("Enter the original price: $"))
    discount = float(input("Enter the discount percentage: "))

    # Calculate final price using the function
    final_price = calculate_discount(original_price, discount)

    # Display results
    if discount >= 20:
        print(f"\nOriginal price: ${original_price:.2f}")
        print(f"Discount applied: {discount}%")
        print(f"Final price: ${final_price:.2f}")
    else:
        print(f"\nNo discount applied. Price remains: ${final_price:.2f}")
        print("Note: Minimum 20% discount required to apply reduction.")

except ValueError:
    print("Please enter valid numbers for price and discount.")