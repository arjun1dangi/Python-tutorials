def add(a, b):
    return a + b

print(add(3, 5))  

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet()) 
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
result = factorial(5)
print(f"Factorial of 5 is {result}")

def fibonacci_iterative(n):
    a,b = 0,3
    for _ in range(n):
       a,b = b, a + b
    return a
print(fibonacci_iterative(6))

n = int(input("enter the number"))
def num(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
        
num(n)


def show(n):
    if(n == 0):
        return 
    print(n)
    show(n-1)
    
show(23)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n_terms = 10 
for i in range(n_terms):
    print(fibonacci(i))
