#Michael Urbi
#Febuary 11, 2025
#P1HW1
#Using Python to collect, process, and display information.

print("-"*5,"Calculating Exponents","-"*5)
print()
print()

base = int(input("Enter an integer as the base value: "))

exp = int(input("Enter an integer as the exponent: "))

ans = pow(base, exp)

print()
print()

print(base, "raised to the power of", exp, "is", ans, "!!")

print()
print()

print("-"*5, "Addition and Subtraction", "-"*5)

print()
print()

sta = int(input("Enter a starting integer: "))

add = int(input("Enter an integer to add: "))

tra = int(input("Enter an integer to subtract: "))

value = sta+add-tra

print()
print()

print(sta, "+", add, "-", tra, "is equal to", value)
