# store the multiplication table generated in python 3 in a file named tables.txt


n = int(input("Enter the number"))

tables = [n*i for i in range(1,11)]
with open("tables.txt", "a" )as f:
    f.write(str(tables) + "\n")