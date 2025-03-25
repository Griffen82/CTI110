# Michael Urbi
# March 25, 2025
# P4Lab2
# Make a program that uses both a for and while loop.

r_agn = "yes"

while r_agn.lower() == "yes":

    nmbr = int(input("Enter an integer: "))
    print()
    
    if 0 <= nmbr:
        for i in range(1, (12 + 1)):
            print(f'{nmbr} * {i} = {nmbr*i}')
            
    else:
        print("This program does not handle negative numbers.")
    print()
    r_agn = input("Would you like to run the program again? (yes/no): ")
    print()

print("Exiting program...")
