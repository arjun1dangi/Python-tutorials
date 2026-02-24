#  a list contains the multiplication table of any number . Write a program to convert it to a verticle  string of same
n = int(input("Enter the number"))
table = [str(n*i) for i in range(1,11)]

s = "\n".join(table)
print(s)