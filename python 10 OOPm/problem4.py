class bullet:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year  = year

    def bullet_info(self):
        print(f"The bullet{self.brand} of model{self.model} manufactured in {self.year}")

    def is_old(self):
        return self.year<2019
    

my_bullet = bullet("JAWA", 42, 2019)

my_bullet.bullet_info()
print("Is the bullet old?", my_bullet.is_old())