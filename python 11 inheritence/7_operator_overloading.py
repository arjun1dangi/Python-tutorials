class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)


# co do this one also

class Number:
    def __init__(self, n):
        self.n = n

    def add(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

# Manually calling the add method instead of using +
result = n.add(m)
print(result)  # Output: 3
