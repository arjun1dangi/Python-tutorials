# myList = [1,2,4,5,9,7,89,789]


user_input = (input("Enter number seperated by spaces: "))
myList = list(map(int, user_input.split()))


# squaredList = []
# for item in myList:
#     squaredList.append(item*item)
# this can be simplified using comprehension

squaredList = [i*i for i in myList]

print("squared list: ", squaredList)