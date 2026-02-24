# create a class "programmer" for storing information of few programmers working at microsoft

class programmer:
    company =  "microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("Arjun", 1200000, 48394)
print(p.name,p.salary,p.pin,p.company)

r = programmer("Aryan", 1200000, 48394)
print(r.name,r.salary,r.pin,r.company)