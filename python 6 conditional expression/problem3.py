""" a spam cooment is defined as a text containing following keyword :
"make a lot of money", "buy now","subscribe this", "click this". Write a programm to ditect these spams"""


p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"

message = input("Enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is an spam")

else:
    print("This is an safe comment")