# bank account == owner, acc n.o, balance, history
from datetime import date, datetime


class Client:
    def __init__(self, names, kra_pin, dob, gender):
        self.names = names
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(self.names)
        print(self.kra_pin)

    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        age = today.year - birth_date.year
        return age



class BankAccount:
    def __init__(self, owner:Client , acc_no:str, balance:int):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + abs(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance = self.balance - abs(amount)

    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("------------")


jane = Client('Jane Chege', 'A001', '2005-09-09', 'F')
ahmed = Client('justine kimai', 'A003', '2005-08-09', 'M')

acc1 = BankAccount(jane, "23144", 99000)
acc2 = BankAccount(ahmed, "23144", 888_000)
acc3 = BankAccount(jane, "23144", 199_000)

acc1.deposit(30000)
acc1.deposit(17000)

acc1.print_details()
acc1.withdraw(30000)
acc1.withdraw(17000)
acc1.print_details()

print( "jane's age is", jane.calc_age())
print( "ahmed's age is", ahmed.calc_age())

print(acc1.owner.names,acc1.owner.calc_age())
print(jane.names,jane.calc_age())




# dob = '2005-08-09'
# today = date.today()
# print(today.year,today.month,today.day)
# print(f"{today.year}-{today.month}-{today.day}")
# convert string to date
# birth_date = datetime.strptime(dob, "%Y-%m-%d")

# age = today.year - birth_date.year
# print(age)
