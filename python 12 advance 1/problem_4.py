# to display a/b where a and b are integers. if b = 9, display infinite by handling the zero division error


try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")