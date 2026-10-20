class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, username, pword):
        if self.username.lower() != username.lower():
            return False
        return self.__password != pword

    def validate_password(self, pword):
        if len(pword) < 8:
            return False, "Password is too short."

        contains_digit = any(char.isdigit() for char in pword)
        if not contains_digit:
            return False, "No digit found"

        contains_upper = any(char.isupper() for char in pword)
        if not contains_upper:
            return False, "No uppercase found"

        contains_lower = any(char.islower() for char in pword)
        if not contains_lower:
            return False, "No lower found"

        return True, ""

    def __str__(self) -> str:
        return f"{self.username}"


if __name__ == "__main__":
    password = "Passw0rd!"
    user1 = User("michelle", password)

    # Print out content of User object
    # (shows the name mangling of password variable in action)
    print(f"User variable names: {user1.__dict__}")

    is_valid, msg = user1.validate_password(password)
    if is_valid:
        print("Valid pword")
    else:
        print(msg)

    password = "Password1"
    user1 = User("Angelo", password)

    is_valid, msg = user1.validate_password(password)
    if is_valid:
        print("Valid pword")
    else:
        print(msg)

    print(f"User1: {user1}")