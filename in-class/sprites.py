class Enemy:
    def __init__(self, enemy_type, health, x_pos=0, y_pos=0):
        self.enemy_type = enemy_type
        self.health = health
        self.__x_pos = x_pos
        self.__y_pos = y_pos

    def get_x_pos(self):
        return self.__x_pos


    def display(self):
        print(f"type: {self.enemy_type}")
        print(f"health: {self.health}")
        print(f"x_pos: {self.__x_pos}")
        print(f"y_pos: {self.__y_pos}")

    def __str__(self) -> str:
        return f"{self.enemy_type} at ({self.__x_pos, self.__y_pos}) : {self.health} health left"


if __name__ == "__main__":
    first_enemy = Enemy("lightning", 100, 90, -100)

    print(f"enemy type: {first_enemy.enemy_type}")
    first_enemy.enemy_type = "fire"
    print(f"enemy type: {first_enemy.enemy_type}")

    first_enemy.display()

    second_enemy = Enemy("grass", 10, 4, 1)
    second_enemy.display()

    # required and optional parameters
    print("only required:")
    only_required = Enemy("fire", 5)
    only_required.display()

    print("no y pos:")
    no_y_pos = Enemy("water", 500, 88)
    no_y_pos.display()

    print(f"First enemy: {first_enemy}")