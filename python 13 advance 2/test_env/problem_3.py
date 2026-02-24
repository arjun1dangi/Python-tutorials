# write a program to filter a list of numbers which are divisible by 5
def divisible5(n):
    if(n%5 == 0):
        return True
    return False
a = [1,2,385,789,629541,741,46,74,45,852]

f = list(filter(divisible5,a))
print(f)