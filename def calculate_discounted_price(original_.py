def calculate_discounted_price(original_price, discount1, discount2):

    discounted_price = original_price * (1 - discount1 / 100) * (1 - discount2 / 100)
    return round(discounted_price, 2)

# Example usage:
original_price = 150
discount1 = 80
discount2 = 20
final_price = calculate_discounted_price(original_price, discount1, discount2)
print(final_price}")
