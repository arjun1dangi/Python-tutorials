# # Input number
# num = int(input("Enter a number: "))

# # Conditional check
# if num > 0:
#     print(f"{num} is positive.")
# elif num < 0:
#     print(f"{num} is negative.")
# else:
#     print(f"{num} is zero.")


# a = int(input("Enetr your number"))
# b = int(input("Enetr your number"))
# c = int(input("Enetr your number"))

# if a > b and a>c:
#     print(f"the largest number is {a}")
# elif b > c:
#     print(f"the largest number is {b}")
# else:
#     print(f"the largest number is {c}")

# year = int(input("Enter the year: "))

# if (year % 4== 0 and year % 100 != 0) or (year % 400 ==0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year")
    
    
# n = int(input("Enter your number"))
    
# if n > 0:
#         if n %2 == 0:
#             print(f"{n} is positive and even")
#         else:
#             print(f"{n}is positive and odd")
            
# elif n < 0:
#     if n %5 == 0:
#         print(f"{n} is negative and odd and divisible by 5.")
#     else:
#         print(f"{n} is negative and not divisible by 5.")
# else:
#     print(" The number is zero")
        
        
# # Input units consumed
# units = int(input("Enter the number of units consumed: "))

# # Conditional to calculate the bill
# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = (100 * 5) + (units - 100) * 7
# else:
#     bill = (100 * 5) + (100 * 7) + (units - 200) * 10

# print(f"Your electricity bill is ₹{bill}.")


# # Input income
# income = float(input("Enter your annual income: "))

# # Calculate tax based on slabs
# if income <= 250000:
#     tax = 0
# elif income <= 500000:
#     tax = (income - 250000) * 0.05
# elif income <= 1000000:
#     tax = 12500 + (income - 500000) * 0.20
# else:
#     tax = 112500 + (income - 1000000) * 0.30

# print(f"Your income tax is ₹{tax:.2f}")


# # Input three side lengths
# a = float(input("Enter the first side: "))
# b = float(input("Enter the second side: "))
# c = float(input("Enter the third side: "))

# # Conditional check for triangle type
# if a == b == c:
#     print("The triangle is Equilateral.")
# elif a == b or b == c or a == c:
#     print("The triangle is Isosceles.")
# else:
#     print("The triangle is Scalene.")


# # Input account balance and withdrawal amount
# balance = float(input("Enter your account balance: ₹"))
# withdrawal = float(input("Enter the withdrawal amount: ₹"))

# # Conditional check for valid withdrawal
# if withdrawal <= balance:
#     balance -= withdrawal
#     print(f"Withdrawal successful! Your new balance is ₹{balance:.2f}")
# else:
#     print("Insufficient balance.")




# # Input two numbers
# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# # Try to convert to float, else check if it contains 'j' (complex part)
# try:
#     real_num1 = float(num1)
#     real_num2 = float(num2)
#     print(f"The sum of the numbers is {real_num1 + real_num2}.")
# except ValueError:
#     if 'j' in num1 or 'j' in num2:
#         print("Complex numbers not supported.")

# correct_pin = "1234"
# attempts = 0

# pin = input("Enter your PIN: ")
# if pin == correct_pin:
#     print("Access granted.")
# else:
#     attempts += 1
#     pin = input("Enter your PIN: ")
#     if pin == correct_pin:
#         print("Access granted.")
#     else:
#         attempts += 1
#         pin = input("Enter your PIN: ")
#         if pin == correct_pin:
#             print("Access granted.")
#         else:
#             print("Account locked.")
            
#             # Input age and citizenship status
# age = int(input("Enter your age: "))
# citizenship = input("Are you an Indian citizen? (yes/no): ")

# # Conditional check for voting eligibility
# if age < 18:
#     print("Not eligible to vote.")
# else:
#     if citizenship.lower() == "yes":
#         print("Eligible to vote.")
#     else:
#         print("Not eligible to vote.")


