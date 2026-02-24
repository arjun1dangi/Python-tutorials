# it is used to directly use a mathematical formula as a function
#this is an example of recursion

def radius(circumference):
    
    return circumference/6.283

circumference = float(input("enter your circumference"))
print(f"the radius of the given number is: {radius(circumference)}") 