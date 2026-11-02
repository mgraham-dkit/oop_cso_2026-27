class Employee:
    def __init__(self,id,firstname,lastname,salary,jobtitle):
        self.firstname =firstname
        self.lastname = lastname
        self.id = id
        self._salary = salary
        self.jobtitle = jobtitle



    def display(self):
        print(f"Employee[ id: {self.id}, first name: {self.firstname}, last name: {self.lastname}, salary: {self._salary}] ")

    def calc_net_pay(self):
        tax = self._salary *0.42
        take_home = self._salary - tax
        month_take_home = take_home/12
        return month_take_home

    def calc_bonus(self):
        if self.jobtitle.lower() == "Manager":
            bonus = self.calc_net_pay() * 1.15
        elif self.jobtitle.lower() == "Intern":
            bonus = self.calc_net_pay() * 0.02
        else:
            bonus = self.calc_net_pay() * 0.06

        return bonus



