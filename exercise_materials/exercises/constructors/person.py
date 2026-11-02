class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(self.name,self.age,self.address)

if __name__ == "__main__":
    name = input("Enter name:")
    age = int(input("Enter age:"))
    address = input("Enter address:")


person1 = Person(name,age,address)
print("Person")
person1.display()
