class Employee:
    language = "python"
    salary = 600000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is{self.salary}")

Arjun = Employee()
Arjun.language = "Java"


Arjun.getInfo()
Employee.getInfo(Arjun)

  