# create a class 'employee' and add salalry and increment properties to it. Write a method 'salsaryAfterIncrement' method with a @property  decorator with a setter which changes the value of incriment based on the salary


class Employee:
    salary = 234
    increment = 30
    @property
    def salaryAfterIncrement(self):
        return (self.salary +self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100

e = Employee()
e.salaryAfterIncrement = 480
print(e.increment)