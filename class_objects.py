"""
class Computer:
    def config(self):
        print("Ram:16 gb  Disk:1T ")
com1=Computer()
com1.config()

class Employee:
    count=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.count+=1

    def disply_employ(self):
        print("Name",self.name, "\nSalary :",self.salary)
    def count_employee(self):
        print("total employee",Employee.count)

emp1=Employee("Rana",200000)
emp1.disply_employ()
emp1.count_employee()

emp2=Employee("Sima",100000)
emp2.disply_employ()

"""
class Parent:
    def parentmthod(self):
        print("Calling the parent method")

class Child(Parent):
    def childmethod(self):
        print("Calling the child method")
ch=Child()
ch.parentmthod()
ch.childmethod()