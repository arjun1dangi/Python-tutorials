marks = {
    "Arjun": 45,
    "Aryan": 45,
    "Arya": 54,
    "Arsh": 64,
    0: "Arjun"
}
print(marks.keys())
print(marks.values())

marks.update({"Arjun":97})
print(marks) 

print(marks.get("Arjun"))
print(marks["Arjun"])

# There are many more methods in dictionary 
