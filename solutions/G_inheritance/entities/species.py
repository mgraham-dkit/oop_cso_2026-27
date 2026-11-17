from datetime import date
from types import NotImplementedType


class Animal:
    def __init__(self, dob: date, weight: float | int, name: str = "Fido"):
        if not dob:
            print("Animal cannot have no date of birth")
            print("Defaulting to today")
            dob = date.today()

        if not isinstance(dob, date):
            print("Date of birth must be a datetime.date type")
            print("Defaulting to today")
            dob = date.today()

        if not isinstance(weight, int | float):
            print("Animal weight must be numeric")
            print("Defaulting to 5")
            weight = 5

        if weight <= 0:
            print("Animal cannot have no weight.")
            print("Defaulting to 5")
            weight = 5

        if not name:
            print("Animal cannot have no name")
            print("Defaulting to \"Fido\"")
            name = "Fido"

        self.dob = dob
        self.weight = weight
        self.name = name

    def display(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"{self.name} is {self.calc_age()} years old and weighs {self.weight}kg."

    def __repr__(self) -> str:
        # Note the way the class name is included
        # This will ensure the class name always reflects the actual type of the object
        # It's not hard-coded to only ever say Animal!
        return f"{self.__class__.__name__}{{name={self.name}, weight:{self.weight}, dob={self.dob}}}"

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Animal):
            return NotImplemented

        if self.dob != other.dob:
            return False

        if self.weight != other.weight:
            return False

        if self.name.lower() != other.name.lower():
            return False

        return True

    def calc_age(self) -> int:
        today = date.today()
        difference = today - self.dob
        return int(difference.days / 365)


class Dog(Animal):
    def __init__(self, dob: date, weight: float | int, breed:str, name: str = "Fido", personality: str = "Happy"  ):
        super().__init__(dob, weight, name)

        if not breed:
            print("Dog cannot have a breed")
            print("Defaulting to \"Labrador\"")
            breed = "Labrador"

        self.breed = breed
        self.personality = personality

    def display(self) -> None:
        print(self)

    def __str__(self) -> str:
        return f"{super().__str__()} {self.name} is a {self.breed} with a {self.personality.casefold()} personality"

    def __repr__(self) -> str:
        # super().__repr__()[0:-1] peels the closing } off the repr output for Animal,
        # so we can append the Dog-specific attributes
        return f"{super().__repr__()[0:-1]}, breed={self.breed}, personality={self.personality}}}"

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Dog):
            return NotImplemented

        if not super().__eq__(other):
            return False

        if self.breed.lower() != other.breed.lower():
            return False

        # Have to handle comparison differently due to case-insensitivity
        # on potentially None fields
        # If either one is None, compare without using lower()
        if not self.personality or not other.personality:
            return self.personality != other.personality

        # If both are real, compare actual data case-insensitively
        if self.personality.lower() != other.personality.lower():
            return False

        return True




if __name__ == "__main__":
    animal = Animal(date(2025, 10, 1), 0)
    print(animal.calc_age())

    dog = Dog(date(2021, 10, 13), 4, "poodle", "Celia", "Bubbly!")
    dog.display()

    print(repr(dog))