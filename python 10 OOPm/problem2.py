# wirte a calss "calculator" capable of finiding squares, cube and square root of a number

class calculator:
    def __init__ (self,n):
        self.n = n

    def square(self):
        print(f"the square is {self.n*self.n}")


    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

    def squareRoot(self):
        print(f"the squareRoot is {self.n**0.5}")



n = int(input("enter your number"))
a = calculator(n)
a.square()
a.cube()
a.squareRoot() 