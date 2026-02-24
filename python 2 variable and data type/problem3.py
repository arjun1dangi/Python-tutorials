# to check the type of variable assigned using input function
# a = int(input("Enter the value of a:"))
# print(type(a))

a = input("Enter a value: ")

# Checking for integer
if a.isdigit():
    a = int(a)
elif a.replace(".", "", 1).isdigit() and a.count(".") == 1:
    a = float(a)

print("Value:", a)
print("Type:", type(a))
