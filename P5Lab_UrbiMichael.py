# Michael Urbi
# April 8, 2025
# P5Lab
# Incorperate P3Lab as a function to give change to a random float

# Add modules

import random

# Secondary function

def dispense_change
    if money==0:
    print("No change")
    
    dollars = money//100
    quarters = (money - (dollars*100))

    if dollars > 0:
        print(dollars, end=' ')
        if dollars == 1:
            print("Dollar")
        else:
            print("Dollars")

    quarter = quarters//25
    dimes = (quarters - (quarter*25))

    if quarter > 0:
        print(quarter, end=' ')
        if quarter == 1:
            print("Quarter")
        else:
            print("Quarters")

    dime = dimes//10
    nickels = (dimes - (dime*10))

    if dime > 0:
        print(dime, end=' ')
        if dime == 1:
            print("Dime")
        else:
            print("Dimes")

    nickel = nickels//5
    pennies = (nickels - (nickel*5))

    if nickel > 0:
        print(nickel, end=' ')
        if nickel == 1:
            print("Nickel")
        else:
            print("Nickels")

    penny = pennies//1

    if penny > 0:
        print(penny, end=' ')
        if penny == 1:
            print("Penny")
        else:
            print("Pennies")


# Primary function

def change():
    # Print how much the user owes

    owe = round(random.uniform(0.01, 100.00), 2)
    f_owe = float(owe)
    s_owe = str(owe)
    print("You owe $" +s_owe+ ".")
    
    # Ask user how much they will pay

    pay = float(input("How much will you pay? "))
    change = pay - f_owe
    r_change = round(change, 2)
    s_change = str(r_change)
    print("Your change is: $" +s_change)
    print()
    dispense_change()
change()
