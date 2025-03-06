#Michael Urbi
#March 6, 2025
#P3Lab
#Program showing knowledge of branching

#Ask user to input an amount of money
mo = float(input("Enter the amount of money as a float: $"))
#print(mo)
change = float(f'{mo:.2f}')
#print(change)
fmoney = change*100
money = int(fmoney)
#print(money)

#Calculate the most efficient number of dollars, quarters, dimes, nickels, and pennies
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

