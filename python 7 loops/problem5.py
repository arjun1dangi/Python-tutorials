# to find the sum of first n natural numbers using whil

n = int(input("Enter a number:"))

i = 0
sum = 0
while(i<=n):
    sum += i
    i += 1

print(f"The sum of first {n} natural number is, {sum}")


