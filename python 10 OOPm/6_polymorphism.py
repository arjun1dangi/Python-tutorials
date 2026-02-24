
class Animal:
    def speak(self):
        return "Some generic animal sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

my_cat = Cat()
print(my_cat.speak()) 
