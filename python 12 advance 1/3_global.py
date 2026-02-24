# global keyword changes the global variable

a = 75
def fun():
    global a
    a = 45
    print(a)
fun()

# don't know what is this about:

# from typing import list, tuple, dict, union

# numbers : list[int] = [1,2,3,4,5,6]

# person : tuple[str, int] = ("Alice", 20)

# scores : dict[str, int] = {"Alice" : 90, "bob": 85}

# identifier : union[int, str] = "ID123"

# identifier = 12345