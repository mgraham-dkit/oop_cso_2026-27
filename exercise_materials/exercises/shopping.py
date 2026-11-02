from exercise_materials.exercises.shopping_exercises import calculate_basket_price


def calculate_item_price(item_dict):
    return item_dict["price"]*item_dict["quantity"]

def calc_basket_price(basket_list):
    total = 0
    for item in basket_list:
        total += calculate_item_price(item)

def print_receipt(basket_list):
    print("Thank you for shopping with us")
    for item in basket_list:
        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]

        subtotal= price * quantity

        print(f"{name:<20} {quantity:>2}x £{price:>5.2f} = £{subtotal:>6.2f}")

if __name__ == "__main__":

    basket = [
    {"name": "Yogurt", "price": 1.79, "quantity": 4},
    {"name": "Bread", "price": 1.80, "quantity": 1},
    {"name": "Milk", "price": 1.59, "quantity": 2}
    ]

    print(f"The total price is: {calculate_basket_price(basket)}")

    print_receipt(basket)