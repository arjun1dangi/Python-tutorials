# n = int(input("Enter the thing: "))



# class Car:
#     brand = None
#     model = None

# my_car = Car()
# print(my_car)



# for i in range(1, n + 1):
#     stars = '*' * i
#     spaces = ' ' * (n - i)
#     print(stars + spaces, ' ', spaces + stars, stars + spaces, ' ', spaces + stars)

# for i in range(n - 1, 0, -1):
#     stars = '*' * i
#     spaces = ' ' * (n - i)
#     print(spaces + stars, ' ', stars + spaces, spaces + stars, ' ', stars + spaces)



# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")

#     print(" " * (2 * (n - i)), end="")

#     for j in range(i, 0, -1):
#         print(j, end="")

#     print()



# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()



# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i, end="")
#     print()  


# for i in range(n):
#     for j in range(n - i):
#         print("*", end="")
#     print()


# for i in range(n):
#     for j in range(1, n - i + 1):
#         print(j, end="")
#     print()


# for i in range(n):
#     spaces = n -i - 1
#     stars = 2 * i + 1
#     print(" " * spaces + "*" * stars)     
# for i in range(n):
#     stars = 2 * (n - i) - 1
#     spaces = i
#     print(" " * spaces + "*" * stars)


# for i in range(n):
#     print("*" * i)

# for i in range(n-1,0,-1):
#     print("*" * i)


# for i in range(n):
#     for j in range(i + 1):
#         if(i + j) % 2 == 0:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()


# count = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(count, end="")
#         count += 1
#     print()





# for i in range(1, n+1):
#     for j in range(i):
#         print(chr(65 + j), end="")
#     print()


# ascii = 65

# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(ascii), end="")
#         ascii += 1
#     print()




# for i in range(n, 0, - 1):
#     for j in range(i ):
#         print(chr(65 + j),  end="")
#     print()



# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(64 + i), end="")
#     print()


# for i in range(1, n+1):
#     print(" " * (n - i), end="")

#     for j in range(1, i + 1 ):
#         print(chr(64 + j), end="")
        
#     for j in range(i - 1, 0, -1):    
#         print(chr(64 + j), end="")

#     print()



# for i in range(1, n + 1):
#     start = 64 + (n - i + 1)
#     for j in range(0, i - 1):
#         print (chr(start + j), end="")
#     print()
        


# for i in range(n):
#     stars = n - i
#     spaces = 2 * i
#     print("*" * stars + " " * spaces + "*" * stars)

# for i in range(n):
#     stars = i + 1
#     spaces = 2 * (n - i - 1)
#     print("*" * stars + " " * spaces + "*" * stars)




# for i in range(1, n + 1):
#     stars = '*' * i
#     spaces = ' ' * (2 * (n - i))
#     print(stars + spaces + stars)

# for i in range(n - 1, 0, -1):
#     stars = '*' * i
#     spaces = ' ' * (2 * (n - i))
#     print(stars + spaces + stars)

# rows = 9
# col = 12

# for i in range(rows):
#     if i == 0 or i == rows - 1:
#         print('*' * col) 
#     else:
#         print('*' + ' '* (col - 2) + '*')


# size = 2 * n - 1 
# for i in range(size):
#     for j in range(size):
#         val = n - min(i, j, size- 1 - i, size - 1 - j)
#         print(val, end=" ")
#     print()

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
    
#     for _ in range(n):
#         name, *marks = input().split()
#         marks = list(map(float, marks))
#         student_marks[name] = marks
    
#     query_name = input()
#     average = sum(student_marks[query_name]) / len(student_marks[query_name])
#     print(f"{average:.2f}")

# if __name__ == '__main__':
#     N = int(input())
#     my_list = []

#     for _ in range(N):
#         cmd = input().split()
#         operation = cmd[0]

#         if operation == 'insert':
#             i, e = int(cmd[1]), int(cmd[2])
#             my_list.insert(i, e)
#         elif operation == 'print':
#             print(my_list)
#         elif operation == 'remove':
#             e = int(cmd[1])
#             my_list.remove(e)
#         elif operation == 'append':
#             e = int(cmd[1])
#             my_list.append(e)
#         elif operation == 'sort':
#             my_list.sort()
#         elif operation =='pop':
#             my_list.pop()
#         elif operation =='reverse':
#             my_list.reverse()




# def split_and_join(line):
#     words = line.split(" ")
#     result = "-".join(words)
#     return result
    
    
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)




# def swap_case(s):
#     return s.swapcase()

# if __name__ == '__main__':
#     s = input()            
#     result = swap_case(s) 
#     print(result)         




# def mutate_string(string, position, character):
#     lst = list(string)
#     lst[position] = character
#     modified_string = ''.join(lst)
#     return modified_string

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)




# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string) - len(sub_string) + 1):
#         if string[i:i+len(sub_string)] == sub_string:
#             count += 1

#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#     print(count_substring(string, sub_string))