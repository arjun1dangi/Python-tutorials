marks = {"Arjun": 100,
         "Aryan": 99,
         "Arya" : 88}


print(marks,type(marks))

marks.copy()
print(marks)

'''marks.clear()
print(marks)

'''

print(marks.get("Arjun"))

print(marks.items())


for key in marks.keys():
    print(key)




my_dict = {"name":"Arjun","age":19, "city": "Indore"}  
my_dict["email"] = "@arjunqwerty.com"
print(my_dict["name"])
age = my_dict.get("age", "Not Found")
print(age)
print(my_dict)  


# Iterate over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")


# Create and access a nested dictionary
nested_dict = {"person": {"name": "Arjun", "age": 19}}
print(nested_dict["person"]["name"])


# Create a list of tuples (name, age)
people = [("Shawn", 30), ("Liam", 25), ("Charlie", 35)]

# Create a dictionary from the list of tuples
people_dict = dict(people)
print("Dictionary:", people_dict)

# Convert the keys (names) of the dictionary into a set to ensure unique names
unique_names = set(people_dict.keys())
print("Unique names as a set:", unique_names)

# Access a tuple from the list and modify the list
print("Tuple from list:", people[0])
people.append(("David", 28))
print("Updated List:", people)

# Iterate over the dictionary and access elements
for name, age in people_dict.items():
    print(f"{name} is {age} years old")


n = [1,2,3,4,5,6,7,8,9]
result = 1
for num in n:
    result *= num
print(result)



