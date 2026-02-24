class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is{self.name} and the company is{self.company}")

class  Coder:
    language = "Python"
    def printLanguages(self):
        print(f"out of all the language here is your language{self.language}")


class programmer(Employee, Coder):
    company = "ITC Ifotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
 
a = Employee()
b = programmer()

b.show()
b.printLanguages()
b.showLanguage