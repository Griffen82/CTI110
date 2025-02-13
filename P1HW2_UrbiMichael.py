#Michael Urbi
#Febuary 11, 2025
#P1HW2
#Simple budget calculations from user input

print("This program calculates and displays travel expenses")
print()
bud = int(input("Enter Budget: "))
print()
Dest = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
acc = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()

exp = gas + acc + food

change = bud - exp

print("-"*12, "Travel Expenses", "-"*12)
print("Location:", Dest)
print("Initial Budget:", bud)
print()
print("Fuel:", gas)
print("Accomodation:", acc)
print("Food:", food)
print()
print("Remaining Balance:", change)

#Psudocode
#Input budget(bud)
#Input destination(Dest)
#Input fuel expenditure (gas)
#Input accomodations expenditure (acc)
#Input food expenditure (food)
#Add all expenses(exp) (gas+acc+food)
#Subtract expenses from budget (bud-exp)
#Display Inputs and Remaining Balance
