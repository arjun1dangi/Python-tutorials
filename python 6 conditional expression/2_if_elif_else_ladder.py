a = int(input("Enter your age:"))

if(a>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("you are entering an negative age")

elif(a==0):
    print("You are entering 0 which is invalid")    

else:
    print("you are below the age of consent")

print("End of program")