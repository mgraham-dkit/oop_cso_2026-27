
from orders import Pizza

def expensive_pizza(order):
    most_expensive_name = None
    most_expensive_pizza = None
    highest_price = 0
    for nickname in order:
        pizza =order[nickname]
        price = pizza.calc_price()

        if price > highest_price:
            highest_price = price
            most_expensive_name = nickname
            most_expensive_pizza = pizza
    return most_expensive_name,most_expensive_pizza

def main():


    order = {}

    username = input("please enter your username:")

    while True:
        answer = input("Would you like to order a pizza? yes enter(Y/y) or any key for no: ").lower()

        if answer != "y":
            break

        nickname = input("Enter a nickname for your pizza:")

        while nickname in order:
            print("nickname already in use, please enter a different nickname:")
            nickname = input("Enter a different nickname:")

        size = input("Enter the pizza size:")
        size = size.lower()

        toppings = []
        print("Enter 1 topping at a time:")
        print("Press enter to finish")

        while True:
            topping = input("Enter a topping:").strip()

            if topping == "":
                break

            toppings.append(topping)

        if len(toppings) == 0:
            toppings = ["tomato sauce","cheese"]

        pizza = Pizza(toppings, size)

        print("Pizza Details")
        print("Nickname:",nickname)
        print("Size:", size)
        print("Toppings:",",".join(toppings))

        order[nickname]=pizza
        print("Pizza added to your order")

    print("Order summary for",username)
    total = 0
    for nickname in order:
        pizza = order[nickname]
        price = pizza.calc_price()
        print(f"{nickname}€{price}")
        total = total+price
    if len(order) == 0:
        print("You havent ordered any pizzas")
    else:
        nickname, pizza = expensive_pizza(order)
        print("Most expensive pizza:")
        print("Pizza nickname:",nickname)
        pizza.display()
        print(f"Price:€{pizza.calc_price()}")

    print(f"{username}'s total bill is € {total:.2f}")
if __name__ == "__main__":
    main()