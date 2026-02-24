# to input name, marks and phone nummber of a student and formate it using the formate function

name = input("Enter name: ")
marks = int(input("Enter your marks: "))
phone = int(input("Enter your contact number"))

s = "The nam of the student is{}, his marks are{}, and contact number is{}".format(name,marks,phone)

print(s)