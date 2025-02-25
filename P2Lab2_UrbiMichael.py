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

print("The (cars_input) gets (mpg_output) mpg.""/n")
