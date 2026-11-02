class Pizza:
    size_and_price = {
        "small" :10,
        "medium" :12,
        "large" : 14,
        "x_large" :16
    }

    __topping = {}


    def __init__(self,topping, size="Medium"):
        self.__topping = topping

        if size in self.size_and_price:
            self.__size = size
        else:


            self.__size = "Medium"

    def display(self):
        if len(self.__topping) == 0:
            print(f"{self.__size} pizza with no toppings")
        else:
            print(f"{self.__size} pizza with {",".join(self.__topping)} toppings")

    def get_size(self):
        return self.__size
    def set_size(self,new_size):
        if new_size in self.size_and_price:
            self.__size = new_size
            return True
        else:
            return False
    def get_num_topping(self):
        return len(self.__topping)

    def add_topping(self,new_topping):
        self.__topping.append(new_topping)
        return True

    def remove_topping(self, topping):
        for existing_topping in self.__topping:
            if existing_topping.lower()== topping.lower():
                self.__topping.remove(existing_topping)
                return True
        return False
    def calc_price(self):
        base = self.size_and_price[self.__size]
        topping_price = self.get_num_topping()*0.85
        return base + topping_price

