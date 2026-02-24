# to find the greatest of three numbers using functions

a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the third number"))

def find_greatest(a, b, c):
    return max(a, b, c)

print(f"the greatest of three numbers is, {find_greatest(a, b, c)}")

# # well! we can solve the same  by the if else statement
