from employee import Employee
employees = {
}
for i in range(2):
    print("Employee", i+1)

    user_id = int(input("Please enter the employee ID:"))

    while user_id in employees:
        print("ID already exists")
        user_id = int(input("Add another employee ID"))

    firstname = input("Please enter first name: ")
    lastname = input("Please enter last name: ")
    salary = float(input("Please enter salary: "))
    jobtitle = input("Please enter job title: ")

    employee = Employee(user_id, firstname, lastname, salary, jobtitle)
    employees[user_id] = employee

    employee.display()
    print(f"Monthly net pay:{employee.calc_net_pay():.2f}")
    print(f"Bonus pay: {employee.calc_bonus():.2f}")



    highest = None
    lowest = None

    for employee in employees.values():

        if highest is None or employee.calc_bonus() > highest.calc_bonus():
            highest = employee

        if lowest is None or employee.calc_net_pay() < lowest.calc_net_pay():
            lowest = employee

    print("Employee with lowest net pay:")
    lowest.display()
    print(f"Net pay: {lowest.calc_net_pay():.2f}")

    print("Employee with highest bonus pay:")
    highest.display()
    print(f"Bonus pay: {highest.calc_bonus():.2f}")