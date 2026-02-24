n = int(input("Enter a number: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f"The sum of numbers from 1 to {n} is {sum}")

for i in range(1, 200):
    if i % 2 == 0:
        print(i)

string = input("Enter a string: ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print(f"The reversed string is: {reversed_string}")

n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial:", factorial)

n = int(input("Enter your number: "))

sum_n = 0

for i in range(1, n + 1):
    sum_n += i
print(f"the sum of the given number is{n}: {sum_n}")

count = 0
while True:  # Infinite loop
    print("Looping...")
    count += 1
    if count == 3:  # Stop after 3 iterations
        break  # Exit  the loop


for i in range(5):
    if i == 3:
        continue  # Skip when i is 3
    print(i)

# Infinite loop (make sure to stop manually)
#while True:
#    print("This will run forever!")


for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

for i in range(0,11,2):
    print(i)
    
for i in range(1,11):
    if i % 2== 0:
        print(i)
        
n = int(input("enter the number"))
total_sum = 0
i = 1
while i <= n:
    total_sum += i
    i += 1
print("sum", total_sum)
    

i = 100
while i >= 1:
    print(i)
    i -= 1

n = int(input("Enter your number"))
i = 1
while i <= 10:
    print(n * i)
    i += 1

nums = (1,2,3,4,5,6,7,8,93,2,4,8)

x = 7
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("found at idx", i)
        i =+ 1

while True:
    print("This will print only once.")
    break  # Exit the loop unconditionally


nums = (1,2,3,4,5,6,7,79,5,2,74)
x = 79

idx = 0
for el in nums:
    if(el == x):
        print("found at idx", idx)
    idx += 1

names = ["Alice", "Bob", "Charlie"]
ages = [24, 25, 26]
for name, age in zip(names, ages):
    print(name, age)


 
number = [-1,5,-6,-8,-9,5,7,6,-6]
positive_number_count = 0
for num in number:
    if num > 0:
        positive_number_count += 1
print(f"Final count of positive number is: ",positive_number_count)


n = int(input("enter the number"))
sum_even = 0

for i in range(1, n + 1):
    if i%2 == 0:
        sum_even += 1

print(f"sum of even numbes is:",sum_even)


n = int(input("Enter the number"))

for i in range(1,11):
    if i == 5:
        continue
    print(n, '*',i, '=', n*i )

n = int(input("Enter your number"))
even_count = 0
odd_count = 0

for i in range(1, n):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        # or odd_count = even_count + 1

print(even_count)
print(odd_count)        


n = int(input("enter the number"))

reversed_number = 0

while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n //= 10

print("Reversed number:", reversed_number)


n = int(input("Enter the number"))
is_prime = True

if n > 1:
    for i in range(2, n):
        if(n % i) == 0:
            is_prime = False
            break

print(is_prime)



items = [1,4,8,7,4,4,8,1,6,9,5,8,4,2]

unique_item = set()
duplicate = set()

for item in items:
    if item in unique_item:
        duplicate.add(item)
    else:
        unique_item.add(item)
        
print("Duplicate:", duplicate)



