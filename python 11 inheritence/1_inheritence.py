class Employee:
    company = "ITC" 
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")



class programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"the name is{self.name} and the salary is {self.salary}")


    def shoawLanguage(self):
        print(f"Thte name is {self.name} and is good with {self.language} language")


# we can do the same by using inheritence as;


class programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and is good in {self.language} language")

a = Employee()
b = programmer()

print(a.company, b.company)
