def calculate_item_price(item_dict):
    return item_dict["price"]*item_dict["quantity"]

def calculate_basket_price(basket_list):
    total = 0
    for item in basket_list:
        total += calculate_item_price(item)

    return total

def print_receipt(basket_list):
    print("Receipt")
    print("Thank you for shopping with us")
    for item in basket_list:
        name = item["name"]
        quantity = item["quantity"]
        price = item["price"]

        subtotal = price * quantity

        print(f"{name:<20} {quantity:>2} x £{price:>5.2f} £{subtotal:>4.2f}")


def find_item(basket_list,item_name):
    for item in basket_list:
        if item["name"].lower() == item_name.lower():
            return item

    return None

def change_quantity(basket_list, item_name, new_quantity):
    if new_quantity < 0:
        print("Cant be a negative number")
        return False

    item = find_item(basket_list,item_name)

    if item is not None:
        item["quantity"] = new_quantity
        return True
    else:
        return False


def calc_total(basket_list):
    basket_total = calculate_basket_price(basket_list)
    if basket_total >= 50:
        discount = basket_total * .1
        basket_total = basket_total - discount

    return basket_total


if __name__ == "__main__":
    basket = [
        {"name": "Yogurt", "price": 1.79, "quantity": 4},
        {"name": "Bread", "price": 1.80, "quantity": 1},
        {"name": "Milk", "price": 1.59, "quantity": 2}
    ]

    print(f"The total price is: {calculate_basket_price(basket)}")

    print_receipt(basket)

    print("searching for item")
    bread = find_item(basket,"Bread")
    print(f"Result for bread: {bread}")

    print("Searching for 'Banana'")
    banana = find_item(basket, "banana")
    print(f"Search result for 'banana' (No match should be found): {banana}")

    print("Updating quantity for 'yogurt' - increasing to 5")
    updated = change_quantity(basket, "Yogurt", 5)
    if updated:
        print("'Yogurt' quantity updated!")
        print(find_item(basket,"Yogurt"))
    else:
        print("Could not update quantity for 'Yogurt'")

    print(f"Total price for normal basket: €{calc_total(basket)}")

    expensive_basket = [
        {"name": "Cheerios", "price": 7.80, "quantity": 3},
        {"name": "Coke Zero", "price": 12.00, "quantity": 4},
    ]
    print(f"Total price for expensive basket: €{calc_total(expensive_basket)}")

