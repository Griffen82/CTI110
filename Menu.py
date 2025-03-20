opt = 'y'
while (opt == 'y'):
    print("Menu")
    print("Progam 1")
    print("Progam 2")
    print("Progam 3")
    print("Exit")
    #opt = input("Do you want to run the program again? y/n ")
    value = int(input("Please enter your choice "))
    #print("Exiting the program")
    if value == 1:
        print("You chose Program 1")
    elif value == 2:
        print("You chose Program 2")
    elif value == 3:
        print("You chose Program 3")
    elif value == 4:
        print("You chose to exit the program.")
        print("Goodbye")
        opt = 'n'
    else:
        print("You chose an incorrect response.")
        print("Press any key to continue.")
