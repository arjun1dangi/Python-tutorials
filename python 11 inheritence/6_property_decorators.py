# class Employee:
#     a = 1

#     @classmethod
#     def show(cls):
#         print(f"the class attribute of a is{cls.a}")

#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
    
#     @name.setter
#     def name (self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# e = Employee()
# e.a = 45

# e.name = "Arjun Dnagi"
# print(e.fname, e.lname)

# e.show()



# here's an another program



class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):
        print("Setting name...")
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

# Create an instance
person = Person("Alice")

# Access the property (triggers getter)
print(person.name)  # Output: Getting name... Alice

# Set a new value (triggers setter)
person.name = "Bob"  # Output: Setting name...

# Delete the property (triggers deleter)
del person.name  # Output: Deleting name...
