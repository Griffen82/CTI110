#Michael Urbi
#Febuary 25, 2025
#P2Lab2
#creating dictionaries

#create dictionary
cars = {"Camero" : 18.21,
        "Prius" : 52.36,
        "Model S" : 110,
        "Silverado": 26
        }

#display all keys in the dictionary

keys = cars.keys()
print(keys)
print()

cars_input=input("Enter a vehicle to see it's MPG: ")
print()

mpg_output=cars[cars_input]

print("The", (cars_input), "gets", (mpg_output), "mpg.")
print()

dist = float(input(f"How many miles will you drice the {cars_input}? "))
print()

fuel = dist/mpg_output

print(f"{fuel:.2f} gallon(s) of gas are needed to drive the {cars_input} {dist:.1f} miles.")
