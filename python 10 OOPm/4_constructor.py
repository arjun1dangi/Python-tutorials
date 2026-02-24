class Employee:
    lenguage = "python"
    salary = 12000000

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. Teh salary is{self.salary}")

        @staticmethod
        def greet ():
            print("Good Morning")

Arjun = Employee("Arjun", 13000000,"python")
print(Arjun.name, Arjun.salary, Arjun.language) 