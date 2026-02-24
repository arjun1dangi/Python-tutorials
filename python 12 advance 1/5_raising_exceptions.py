a = int(input("enter first number"))
b = int(input("Enter secod number"))

if(b == 0):
    raise ZeroDivisionError("hey our program is not meant to divide number by zero")

else:
    print(f"the divisoion a/b is {a/b}")
