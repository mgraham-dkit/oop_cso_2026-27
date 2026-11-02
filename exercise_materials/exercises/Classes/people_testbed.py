from people import Person

person_1 = Person()
if person_1.left_handed == True:
    print(person_1.first_name + " " + person_1.last_name)
else:
    print(person_1.first_name.upper() + " " + person_1.last_name.upper())
print("Age:",person_1.age)

person_2 = Person()
f_name = input("Enter the first name:")
l_name = input("Enter the last name:")
person_age = int(input("Enter the age:"))
person_left_handed = input("Enter whether they are left handed: (Y/y if yes or ant key if no)")
if person_left_handed.lower() == "y":
    person_left_handed = True
else:
    person_left_handed = False


person_2.first_name = f_name
person_2.last_name = l_name
person_2.age = person_age

if person_2.left_handed == person_left_handed:
    print(person_2.first_name + " " + person_2.last_name)
else:
    print(person_2.first_name.upper() + " " + person_2.last_name.upper())

print("Age:",person_age)
