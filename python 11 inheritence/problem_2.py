# create  a class pets from a class animals and furthur create a class dog from pets Add a method bark to class dog

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bhow Bhow")


d = Dog()

d.bark()