# using walrus operator

if (n := len([1,2,3,4,5,6])) > 4:
    print(f"List is too long({n} elements, expected <=4)")
