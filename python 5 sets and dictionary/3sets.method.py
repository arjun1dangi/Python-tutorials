s = set()

set = {1,2,3,4,8,9}
set.add(7)# add element
set.update([5,6,7])#update element adds multiple elements
set.remove(4)# removes a specific elements
element = set.pop() #removes and returns an arbitary element from the set
set.clear()# clear all the elements
# there is an union method also which combine values of two different sets
# there are many more methods other then these

print(set)
# union(), intersection(), difference(), symmetric_difference(), etc, these are some common operations that we can perform on sets.
