# #methods for list

# my_list = ["Arjun","Arya","Aryan",59,"Arsh",False]
# print(my_list)

# my_list.append(95)
# print(my_list)

# my_list.insert(4,6)
# print(my_list)

# my_list.remove(95)
# print(my_list)

# element = my_list.pop(3)
# print(element)

# index = my_list.index("Arjun")
# print(index)


# my_list.sort()
# print(my_list)  # it will show an error as it can't show output betweeen int and str

# #methods for tuples

# my_tuple = (1,2,3,4,"Arjun",12.41,False)
# print(my_tuple)

# count = my_tuple.count(4)
# print(my_tuple)

# index = my_tuple.index(4)
# print(index)



# set1 = {1, 2, 3} 
# set2 = set1.copy() 
# set2.add(4) 
# print(set1) 

# set1 = {1,2,3}
# set2 = {4,5,6}
# print(len(set1+set2))


# A = {0, 2, 4, 6, 8}; 
# B = {1, 2, 3, 4, 5}; 

# print(A | B) 



# a = [10,20,30,40,50,60]
# b = [1,2,3,4,5,6]

# subtracted = list()
# for a, b in zip(a, b):
#     item = a -b
#     subtracted.append(item)

# print(subtracted)


# def addToList(listcontainer):
#     listcontainer += [10]
# mylistcontainer = [10,20,30,40]
# addToList(mylistcontainer)
# [print(len(mylistcontainer))]


# list = [1,2,3,None,(1,2,3,4,5),['Geeks','for','Geeks']] 

# print(len(list))

# list = ['python', 'learning','@','Geeks','for','Geeks']
# print(list[0:6:2])



# data = [2, 3, 9] 
# temp = [[x for x in[data]] for x in range(3)] 
# print (temp) 



# data = [x for x in range(5)] 
# temp = [x for x in range(7) if x in data and x%2==0] 
# print(temp) 



# temp = 'Geeks 22536 for 445 Geeks'
# data = [x for x in (int(x) for x in temp if x.isdigit()) if x%2 == 0] 
# print(data) 


# L1 = []
# L1.append([1, [2, 3], 4]) 
# L1.extend([7, 8, 9]) 
# print(L1[0][1][1] + L1[2]) 


# L1 = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True] 
# val1, val2 = 0,'' 
# for x in L1: 
# 	if(type(x) == int or type(x) == float): 
# 		val1 += x 
# 	elif(type(x) == str): 
# 		val2 += x 
# 	else: 
# 		break
# print(val1, val2) 


# L1 = [1, 2, 3, 4] 
# L2 = L1 
# L3 = L1.copy() 
# L4 = L1
# L1[0] = [5] 
# print(L1, L2, L3, L4) 


# L = [1, 3, 5, 7, 9] 
# print(L.pop(-3), end = ' ') 


# def REVERSE(L): 
# 	L.reverse() 
# 	return(L) 
# def YKNJS(L): 
# 	List = [] 
# 	List.extend(REVERSE(L)) 
# 	print(List) 

# L = [1, 3.1, 5.31, 7.531] 
# YKNJS(L) 


# Concatenate lists
# list1 = [1, 2]
# list2 = [3, 4]
# combined = list1 + list2
# print(combined)
# Create a list
#  always remember that append adds only a single digit but extend adds multiple digits
# my_list = [1, 2, 3, 4, 5]

# print(my_list[0])  
# print(my_list[-1])  

# my_list.extend([6,7,8,9])
# my_list.extend(['a','r','j',"un"])
# my_list.insert(2, 'a')
# my_list.remove(5)
# my_list.sort()
# print(my_list)

# # Convert list to tuple
# my_tuple = tuple(my_list)
# print(my_tuple)
# # Filter the list to only include even numbers
# filtered_list = [x for x in my_list if x % 2 == 0]
# print(filtered_list)



# # Map each element to its square
# squared = list(map(lambda x: x**2, my_list))
# print(squared)

# # Sum all elements in the list (reduce)
# from functools import reduce
# sum_elements = reduce(lambda a, b: a + b, my_list)  
# print(sum_elements)


# # Access nested lists
# nested_list = [[1, 2, 3], [4, 5, 6]]
# print(nested_list[0][1])  # Access element 2


# # Flatten a nested list
# flat_list = [item for sublist in nested_list for item in sublist]
# print(flat_list)
