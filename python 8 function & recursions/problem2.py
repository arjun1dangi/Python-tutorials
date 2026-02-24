#  to convert celcius to fahrenheit using function

def celcius_to_fahrenheit(celcius):
    return (celcius*9/5)+32

celcius = int(input("Enter the temperature in celcius:"))
print(f"{celcius_to_fahrenheit(celcius)} degree celcius")
