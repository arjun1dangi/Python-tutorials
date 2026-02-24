# Program 1: Infinite Loop Fixed
my_string = "geeksforgeeks"
i = "i"
if i in my_string:
    print(i, end=" ")
print("\n")  # To separate outputs

# Program 2: Range with String Fixed
my_string = 'geeksforgeeks'
for i in range(len(my_string)):
    print(i)
print("\n")

# Program 3: Uppercase Conversion Fixed
my_string = 'geeksforgeeks'
result = ""
for i in range(len(my_string)):
    result += my_string[i].upper()
print(result)
print("\n")

# Program 4: Iterating Over Integer Fixed
a = 123
for i in str(a):
    print(i, end="")
print("\n")

# Program 5: Set Removes Duplicates
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print(set1)
print("\n")

# Program 6: Dictionary Instead of Tuple Fixed
dictionary = {}
dictionary[(1, 2, 4)] = 8
dictionary[(4, 2, 1)] = 10
dictionary[(1, 2)] = 12
_sum = 0
for k in dictionary:
    _sum += dictionary[k]
print(len(dictionary) + _sum)
print("\n")

# Program 7: Tuple Multiplication
tuple_str = ("check") * 3
print(tuple_str)
print("\n")

# Program 8: List and Tuple Calculation Fixed
L = [3, 1, 2, 4]
T = ("1", "2", "3", "4")
L.sort()
counter = 0
for x in T:
    L[counter] += int(x)
    counter += 1
print(L)
print("\n")

# Program 9: Palindrome Check (Fixed Misleading Name)
def is_palindrome(s):
    return s == s[::-1]

word = input("Enter a word to check for palindrome: ")
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")
